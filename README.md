# impfuzzy_lief
Yet another implementation pyimpfuzzy using [python-ssdeep](https://github.com/DinoTools/python-ssdeep) and [LIEF](https://github.com/lief-project/LIEF)

## Install

```
$ git clone https://github.com/kohnakagawa/impfuzzy_lief.git
$ cd impfuzzy_lief
$ poetry shell
$ poetry install
```

## Usage

```
>>> import impfuzzy_lief
>>> impfuzzy_lief.compute_impfuzzy_from_file("tests/bin/Testx64.exe")
'24:wz4VTMvPWvNwA3uMkE4qe/HNffGYFY/7EOVjgVM1SvmywSo07DpJm35bL9:LTeINlKNiwd4S325bL9'
>>> impfuzzy_lief.compute_impfuzzy(list(open("tests/bin/Testx64.exe", "rb").read()))
'24:wz4VTMvPWvNwA3uMkE4qe/HNffGYFY/7EOVjgVM1SvmywSo07DpJm35bL9:LTeINlKNiwd4S325bL9'
```
