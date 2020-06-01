import numpy as np
from openmdao.api import ExplicitComponent


class EngHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('quantity')
        self.add_output('EngHr')

        self.declare_partials('EngHr', 'EmptyWeight')
        self.declare_partials('EngHr', 'v_inf')
        self.declare_partials('EngHr', 'quantity')
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6
        quantity = inputs['quantity']

        outputs['EngHr'] = 5.18 * EmptyWeight**.777 * v_inf**.894 * quantity**.163 

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3/6
        quantity = inputs['quantity']

        partials['EngHr', 'EmptyWeight'] = 4.02486 * EmptyWeight**-.223 * v_inf**.894 * quantity**.163
        partials['EngHr', 'v_inf'] = 4.63092 * EmptyWeight**.777 * v_inf**-.106 * quantity**.163
        partials['EngHr', 'quantity'] = .84434 * EmptyWeight**.777 * v_inf**.894 * quantity**-.837