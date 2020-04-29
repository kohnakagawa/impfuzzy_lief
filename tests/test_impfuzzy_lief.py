import os
from typing import Optional

import pyimpfuzzy
import pytest

from impfuzzy_lief import compute_impfuzzy_from_file

_script_dir: str = os.path.abspath(os.path.dirname(__file__))


@pytest.mark.parametrize(
    "fpath",
    [
        os.path.join(_script_dir, "bin/Testx64.exe"),
        os.path.join(_script_dir, "bin/Testx86.exe"),
        os.path.join(_script_dir, "bin/Test.dll"),
    ],
)
def test_compute_impfuzzy_from_file(fpath: str) -> None:
    actual: Optional[str] = compute_impfuzzy_from_file(fpath)
    expected: str = pyimpfuzzy.get_impfuzzy(fpath)
    assert actual == expected
