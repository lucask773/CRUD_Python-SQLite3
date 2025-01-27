
float = 0.0

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'float', falsy(float))