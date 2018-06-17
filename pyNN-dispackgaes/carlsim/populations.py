import numpy
from pyNN import common
from pyNN.standardmodels import StandardCellType
from pyNN.parameters import ParameterSpace, simplify
from . import simulator
from .recording import Recorder
from carlsim import *

class Assembly(common.Assembly):
    __doc__ = common.Assembly.__doc__
    _simulator = simulator

class Population(common.Population):
    __doc__ = common.Population.__doc__
    _simulator = simulator
    _recorder_class = Recorder
    _assembly_class = Assembly

    def _create_cells(self):
        id_range = numpy.arange(simulator.state.id_counter,
                                simulator.state.id_counter + self.size)
        self.all_cells = numpy.array([simulator.ID(id) for id in id_range],
                                     dtype=simulator.ID)
        self._mask_local = numpy.ones((self.size,), bool)
        self.carlsim_group = simulator.state.network.createGroup("output", 9, EXCITATORY_NEURON)

    def _set_initial_value_array(self, variable, initial_value):
        """
        Empty method to suppress setting initial value
        Carlsim does not need initial value setting (handled internally)
        :param variable:
        :param initial_value:
        :return:
        """

    def _get_view(self, selector, label=None):
        """
        Empty method to suppress getting the view
            shall be implemented later by the developer
            """


        pass