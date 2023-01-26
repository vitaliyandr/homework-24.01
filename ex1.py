try:
    print(eval(input()))
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')