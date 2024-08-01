from PiNeR import get

ini_file = 'file.ini'

opt = get(ini_file, 'section1', 'numb', float)
if opt:
    print(opt)

opt = get(ini_file, 'section1', 'char', str)
if opt:
    print(opt)

opt = get(ini_file, 'section1', 'bool', bool)
if opt:
    print(opt)

opt = get(ini_file, 'sezione2', 'numero', float)
if opt:
    print(opt)

opt = get(ini_file, 'sezione2', 'carattere', str)
if opt:
    print(opt)

opt = get(ini_file, 'sezione2', 'logico', bool)
if opt:
    print(opt)