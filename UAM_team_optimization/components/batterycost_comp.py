import numpy as np
from openmdao.api import ExplicitComponent


class BatteryCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('kwh')
        self.add_input('kwhcost')
        self.add_input('q')
        self.add_output('BatteryCost')

        self.declare_partials('BatteryCost', 'q')


        
    def compute(self, inputs, outputs):
        
        kwh = inputs['kwh']
        kwhcost = inputs['kwhcost']
        q = inputs['q']

        outputs['BatteryCost'] = kwh * kwhcost * q

    def compute_partials(self, inputs, partials):
       
        kwh = inputs['kwh']
        kwhcost = inputs['kwhcost']
        q = inputs['q']

        partials['BatteryCost', 'q'] = kwh * kwhcost