# yamlarg
 Easy YAML arguments for python scripts.

## Usage

```bash
python3.8 -m pip install yamlarg
```

```python
import yamlarg
args = yamlarg.parse('argument_file.yaml')
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
