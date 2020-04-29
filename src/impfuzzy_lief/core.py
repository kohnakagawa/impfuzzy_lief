import sys
import traceback
from typing import List, Optional

import lief
import ssdeep


def remove_ext(dllname: str) -> str:
    exts = ("ocx", "sys", "dll")
    parts = dllname.rsplit(".", 1)
    if len(parts) > 1 and parts[1] in exts:
        return parts[0]
    else:
        return dllname


def compute_impfuzzy_from_file(fpath: str) -> Optional[str]:
    try:
        with open(fpath, "rb") as fin:
            data = list(fin.read())
    except Exception as e:
        print(e, file=sys.stderr)
        return None
    return compute_impfuzzy(data)


def compute_impfuzzy(data: List[int]) -> Optional[str]:
    try:
        imports: List[str] = list()
        obj: lief.PE.Binary = lief.PE.parse(raw=data)
        if not obj.has_imports:
            return None
        for entry in obj.imports:
            dllname = entry.name.lower()
            dllname = remove_ext(dllname)

            # TODO: LIEF の実装が IAT から API 名の参照を行なっていることの確認
            # NOTE: INT から API 名の参照を行なっている場合だと、pyimpfuzzy の実装と違う可能性あり
            for api in entry.entries:
                imports.append(f"{dllname}.{api.name.lower()}")
        return ssdeep.hash(",".join(imports))
    except lief.bad_format as e:
        print(e, file=sys.stderr)
        return None
    except:
        print("System error occurs")
        print("Traceback")
        print(f"{traceback.format_exc()}")
        return None
