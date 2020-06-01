import numpy as np
from openmdao.api import ExplicitComponent


class MfgCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('quantity')
        self.add_output('MfgCost')

        self.declare_partials('MfgCost', 'EmptyWeight')
        self.declare_partials('MfgCost', 'v_inf')
        self.declare_partials('MfgCost', 'quantity')
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6
        quantity = inputs['quantity']

        outputs['MfgCost'] = 1.1236 * 31.2 * EmptyWeight**.921 * v_inf**.621 * quantity**.799

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6
        quantity = inputs['quantity']

        partials['MfgCost', 'EmptyWeight'] = 1.1236 * 28.7352 * EmptyWeight**-.079 * v_inf**.621 * quantity**.799
        partials['MfgCost', 'v_inf'] = 1.1236 * 19.3752 * EmptyWeight**.921 * v_inf**-.379 * quantity**.799
        partials['MfgCost', 'quantity'] = 1.1236 * 24.9288 * EmptyWeight**.921 * v_inf**.621 * quantity**-.201