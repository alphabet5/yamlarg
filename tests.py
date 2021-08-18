import yamlarg

if __name__ == '__main__':
    args = yamlarg.parse('arguments.yaml', description="This is an example description.\nPlace an overview here.")
    print(args)
    assert args == {'string': 'default string',
                    'bool_false': False,
                    'bool_true': True,
                    'list': ''}
