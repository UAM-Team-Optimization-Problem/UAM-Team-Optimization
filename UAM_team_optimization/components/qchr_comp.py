import numpy as np
from openmdao.api import ExplicitComponent


class QcHrComp(ExplicitComponent):

    def setup(self):
        self.add_input('MfgHr')
        self.add_output('QcHr')

        self.declare_partials('QcHr', 'MfgHr')


        
    def compute(self, inputs, outputs):
        
        MfgHr = inputs['MfgHr']

        outputs['QcHr'] = .133 * MfgHr

    def compute_partials(self, inputs, partials):
       
        MfgHr = inputs['MfgHr']

        partials['QcHr', 'MfgHr'] = .133