#!/usr/bin/env python

"""
setup.py file 
"""

from distutils.core import setup, Extension


carlsim_module = Extension('_carlsim',
                           sources=['carlsim_wrap.cxx', '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/interface/src/carlsim.cpp',
                            'interface/src/callback_core.cpp', 
                            '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/interface/src/linear_algebra.cpp', 
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/interface/src/poisson_rate.cpp', 
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/interface/src/user_errors.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/kernel/src/print_snn_info.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/kernel/src/snn_cpu_module.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/kernel/src/snn_manager.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/kernel/src/spike_buffer.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/connection_monitor.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/connection_monitor_core.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/group_monitor.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/group_monitor_core.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/spike_monitor.cpp',
                           '/home/anup/swig-3.0.12/Examples/python/CARLsim4/carlsim/monitor/spike_monitor_core.cpp',
                            '/home/anup/swig-3.0.12/Examples/python/CARLsim4/tools/spike_generators/spikegen_from_vector.cpp'


                           ]
                           )

setup (name = 'carlsim',
       version = '0.2',
       author      = "Prathyusha Adiraju",
       description = """CARLsim simulator as Python library""",
       ext_modules = [carlsim_module],
       py_modules = ["carlsim"],
       )