from distutils.core import setup
import py2exe
import os
import matplotlib
import Graphs
import vessel_size

setup(
    windows = [ { 'script': "prealfa_v15.py", 'icon_resources': [(1, 'teste.ico')]},],
 
    data_files = matplotlib.get_py2exe_datafiles(),
    options = {
        'py2exe': {
            r'compressed': True,
            r'optimize': 2,
            r'includes': [
                r'matplotlib',
                r'matplotlib.backends.backend_tkagg',
                r'matplotlib.pyplot',
                r'scipy.sparse.csgraph._validation',
                r'scipy.special._ufuncs_cxx',
                #r'mpl_toolkits',
                r'pytz',
                r'Graphs',
                r'vessel_size'
                ],
            r'dll_excludes': [r'MSVCP90.dll'],
            r'excludes': [
                '_gtkagg',
                '_tkagg',
                '_agg2',
                '_cairo',
                '_cocoaagg',
                '_fltkagg',
                '_gtk',
                '_gtkcairo',
                'tcl'
                ]
            }
        },
    )
