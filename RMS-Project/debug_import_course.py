import importlib, traceback
try:
    m = importlib.import_module('Course')
    print('Loaded Course from', m.__file__)
    print(sorted([n for n in dir(m) if not n.startswith('_')]))
except Exception:
    traceback.print_exc()
