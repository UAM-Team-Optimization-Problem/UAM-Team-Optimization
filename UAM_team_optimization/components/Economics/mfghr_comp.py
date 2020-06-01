import numpy as np
from openmdao.api import ExplicitComponent


class MfgHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('quantity')
        self.add_output('MfgHr')

        self.declare_partials('MfgHr', 'EmptyWeight')
        self.declare_partials('MfgHr', 'v_inf')
        self.declare_partials('MfgHr', 'quantity')
        
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6
        quantity = inputs['quantity']

        outputs['MfgHr'] = 10.5 * EmptyWeight**.82 * v_inf**.484 * quantity**.641 

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6
        quantity = inputs['quantity']

        partials['MfgHr', 'EmptyWeight'] =  8.61 * EmptyWeight**-.18 * v_inf**.484 * quantity**.641 
        partials['MfgHr', 'v_inf'] = 5.082 * EmptyWeight**.82 * v_inf**-.516 * quantity**.641 
        partials['MfgHr', 'quantity'] =  6.7305 * EmptyWeight**.82 * v_inf**.484 * quantity**-.359 