import numpy as np
from openmdao.api import ExplicitComponent


class MotorCostComp(ExplicitComponent):

    def setup(self):

        self.add_input('num_motor')
        self.add_input('q')
        self.add_output('MotorCost')

        self.declare_partials('MotorCost', 'q')


        
    def compute(self, inputs, outputs):
        
        num_motor = inputs['num_motor']
        q = inputs['q']

        outputs['MotorCost'] = 10000 * num_motor * q

    def compute_partials(self, inputs, partials):
       
        num_motor = inputs['num_motor']
        q = inputs['q']

        partials['MotorCost', 'q'] = 10000 * num_motor