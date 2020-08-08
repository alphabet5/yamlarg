import yamlarg

if __name__ == '__main__':
    args = yamlarg.parse('arguments.yaml')
    print(args)
    assert args == {'string': 'default string',
                    'bool_false': False,
                    'bool_true': True,
                    'list': ''}
