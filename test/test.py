from PiNeR import get
import numpy as np

ini_file = 'file.ini'

opt = get(ini_file, 'section1', 'numb', as_type=np.ndarray)
if opt is not None:
    print(opt)

opt = get(ini_file, 'section1', 'char', list)
if opt:
    print(opt[1])

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