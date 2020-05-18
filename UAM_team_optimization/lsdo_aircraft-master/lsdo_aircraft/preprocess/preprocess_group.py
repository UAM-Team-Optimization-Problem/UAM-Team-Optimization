from __future__ import print_function

from openmdao.api import Group, IndepVarComp

from lsdo_utils.api import PowerCombinationComp


class PreprocessGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)
        self.options.declare('options_dictionary')

        self.promotes = None

    def setup(self):
        shape = self.options['shape']

        comp = IndepVarComp()
        comp.add_output('altitude', val = 1500, shape=shape)
        comp.add_output('speed', val = 67, shape=shape)
        comp.add_output('wing_area', val = 25, shape=shape)
        self.add_subsystem('inputs_comp', comp, promotes=['*'])