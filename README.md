# yamlarg
 Easy YAML arguments for python scripts.

## Usage

```bash
python3.8 -m pip install yamlarg
```

```python
import yamlarg
args = yamlarg.parse('argument_file.yaml', description="This is an example description.\nPlace an overview here.")
```

Example YAML arguments file.
```yaml
---
string:
  help: Example string parameter.
  type: str
  default: 'default string'
bool_false:
  help: Example boolean with a default of false.
  default: False
  action: 'store_true'
bool_true:
  help: Example boolean with a default of true
  default: True
  action: 'store_false'
list:
  help: List of n number of unnamed arguments.
  default: ''
  nargs: '*'
```

Running a python script would then look like this.
```bash
python3.8 ./script.py --string "this is a test string" --bool_false --bool_true --list a b c
```
```python
{'string': 'this is a test string', 'bool_false': True, 'bool_true': False, 'list': ['a', 'b', 'c']}
```

```bash
python3.9 ./script.py --help
usage: script.py [-h] [--string STRING] [--bool_false] [--bool_true] [--list [LIST ...]]

This is an example description.
Place an overview here.

optional arguments:
  -h, --help         show this help message and exit
  --string STRING    Example string parameter.
  --bool_false       Example boolean with a default of false.
  --bool_true        Example boolean with a default of true
  --list [LIST ...]  List of n number of unnamed arguments.
```

## Changelog

### 0.0.8

- Added "description" as an optional argument for the parse function.
- Changed the description formatting to raw to allow for newlines in the description.
- Added a bit more information to the readme.