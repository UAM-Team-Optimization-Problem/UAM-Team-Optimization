import numpy as np
from openmdao.api import ExplicitComponent


class MfgHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('q')
        self.add_output('MfgHr')

        self.declare_partials('MfgHr', 'EmptyWeight')
        self.declare_partials('MfgHr', 'v_inf')
        self.declare_partials('MfgHr', 'q')
        
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        outputs['MfgHr'] = 10.5 * EmptyWeight**.82 * v_inf**.484 * q**.641 

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        partials['MfgHr', 'EmptyWeight'] =  8.61 * EmptyWeight**-.18 * v_inf**.484 * q**.641 
        partials['MfgHr', 'v_inf'] = 5.082 * EmptyWeight**.82 * v_inf**-.516 * q**.641 
        partials['MfgHr', 'q'] =  6.7305 * EmptyWeight**.82 * v_inf**.484 * q**-.359 