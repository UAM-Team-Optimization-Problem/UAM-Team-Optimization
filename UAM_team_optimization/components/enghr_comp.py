import numpy as np
from openmdao.api import ExplicitComponent


class EngHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('q')
        self.add_output('EngHr')

        self.declare_partials('EngHr', 'EmptyWeight')
        self.declare_partials('EngHr', 'v_inf')
        self.declare_partials('EngHr', 'q')
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        outputs['EngHr'] = 5.18 * EmptyWeight**.777 * v_inf**.894 * q**.163 

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        partials['EngHr', 'EmptyWeight'] = 4.02486 * EmptyWeight**-.223 * v_inf**.894 * q**.163
        partials['EngHr', 'v_inf'] = 4.63092 * EmptyWeight**.777 * v_inf**-.106 * q**.163
        partials['EngHr', 'q'] = .84434 * EmptyWeight**.777 * v_inf**.894 * q**-.837