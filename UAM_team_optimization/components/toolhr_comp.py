import numpy as np
from openmdao.api import ExplicitComponent


class ToolHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_input('q')
        self.add_output('ToolHr')

        self.declare_partials('ToolHr', 'EmptyWeight')
        self.declare_partials('ToolHr', 'v_inf')
        self.declare_partials('ToolHr', 'q')
        
    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        outputs['ToolHr'] = 7.22 * EmptyWeight**.777 * v_inf**.696 * q**.263

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']
        v_inf = inputs['v_inf']
        q = inputs['q']

        partials['ToolHr', 'EmptyWeight'] = 5.60994 * EmptyWeight**-.223 * v_inf**.696 * q**.263
        partials['ToolHr', 'v_inf'] = 5.02512 * EmptyWeight**.777 * v_inf**-.304 * q**.263
        partials['ToolHr', 'q'] =  1.89886 * EmptyWeight**.777 * v_inf**.696 * q**-.737