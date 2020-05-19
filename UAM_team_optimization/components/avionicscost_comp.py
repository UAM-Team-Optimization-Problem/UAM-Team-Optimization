import numpy as np
from openmdao.api import ExplicitComponent


class AvionicsCostComp(ExplicitComponent):

    def setup(self):

        self.add_input('q')
        self.add_output('AvionicsCost')

        self.declare_partials('AvionicsCost', 'q')


        
    def compute(self, inputs, outputs):
        
        q = inputs['q']

        outputs['AvionicsCost'] = 60000 * q

    def compute_partials(self, inputs, partials):
       
        q = inputs['q']

        partials['AvionicsCost', 'q'] = 60000 