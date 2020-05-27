from openmdao.api import Group, IndepVarComp

# from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp

from lsdo_aircraft.api import Preprocess, Atmosphere, Powertrain, PowertrainGroup, AtmosphereGroup
from lsdo_aircraft.api import SimpleRotor, SimpleMotor
from openmdao.api import ExplicitComponent

import numpy as np

n = 1
shape = (n, n)

powertrain = Powertrain()

preprocess_name = 'preprocess'
atmosphere_name = 'atmosphere'
simple_motor_name = 'motor'
simple_rotor_name = 'rotor'


powertrain.add_module(Preprocess(
    name=preprocess_name,
))
powertrain.add_module(Atmosphere(
    name=atmosphere_name,
))
powertrain.add_module(SimpleMotor(
    name=simple_motor_name,
))
powertrain.add_module(SimpleRotor(
    name=simple_rotor_name,
))

powertrain.add_link(
    preprocess_name, 'altitude',
    atmosphere_name, 'altitude',
)
powertrain.add_link(
    preprocess_name, 'speed',
    atmosphere_name, 'speed',
)
powertrain.add_link(
    preprocess_name, 'speed',
    simple_rotor_name, 'speed',
)
powertrain.add_link(
    atmosphere_name, ['density', 'sonic_speed'],
    simple_rotor_name, ['density', 'sonic_speed'],
)
powertrain.add_link(
    simple_motor_name, ['angular_speed', 'shaft_power'],
    simple_rotor_name, ['angular_speed', 'shaft_power'],
)

class PropulsionGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 

        wing_left_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_left_outer_prop_group', wing_left_outer_prop_group, promotes=['*'])

        wing_left_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_left_inner_prop_group', wing_left_inner_prop_group)

        tail_left_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('tail_left_prop_group', tail_left_prop_group)

        wing_right_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_right_outer_prop_group', wing_right_outer_prop_group)

        wing_right_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_right_inner_prop_group', wing_right_inner_prop_group)

        tail_right_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('tail_right_prop_group', tail_right_prop_group)


        # comp = GeometryComp()
        # self.add_subsystem('geometry_comp', comp, promotes = ['*'])