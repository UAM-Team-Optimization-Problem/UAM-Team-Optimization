import numpy as np
from openmdao.api import ExplicitComponent


class BatteryCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('total_avail_energy_kWh')
        self.add_input('kwhcost')
        self.add_input('quantity')
        self.add_output('BatteryCost')

        self.declare_partials('BatteryCost', 'quantity')


        
    def compute(self, inputs, outputs):
        
        total_avail_energy_kWh = inputs['total_avail_energy_kWh']
        kwhcost = inputs['kwhcost']
        quantity = inputs['quantity']

        outputs['BatteryCost'] = total_avail_energy_kWh * kwhcost * quantity

    def compute_partials(self, inputs, partials):
       
        total_avail_energy_kWh = inputs['total_avail_energy_kWh']
        kwhcost = inputs['kwhcost']
        quantity = inputs['quantity']

        partials['BatteryCost', 'quantity'] = total_avail_energy_kWh * kwhcost
        partials['BatteryCost', 'total_avail_energy_kWh'] = quantity * kwhcost
        partials['BatteryCost', 'kwhcost'] = total_avail_energy_kWh * quantity