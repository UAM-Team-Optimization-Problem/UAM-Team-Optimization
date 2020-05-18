from openmdao.api import ExplicitComponent

import numpy as np

class CDiWingComp(ExplicitComponent):


    def setup(self):
        self.add_input('wing_CL')
        self.add_input('wing_AR')
        self.add_input('wing_e')
       
        self.add_output('wing_CDi')

        self.declare_partials('wing_CDi','wing_CL')
        self.declare_partials('wing_CDi','wing_AR')
        self.declare_partials('wing_CDi','wing_e')

    def compute(self, inputs, outputs):
        
        wing_CL = inputs['wing_CL']
        wing_AR = inputs['wing_AR']
        wing_e = inputs['wing_e']
        
        outputs['wing_CDi'] = wing_CL ** 2. /np.pi /wing_e /wing_AR

    def compute_partials(self, inputs, partials):
        
        wing_CL = inputs['wing_CL']
        wing_AR = inputs['wing_AR']
        wing_e = inputs['wing_e']


        partials['wing_CDi', 'wing_CL'] =  2 * wing_CL / np.pi / wing_e / wing_AR
        partials['wing_CDi', 'wing_AR'] = -wing_CL**2/np.pi/wing_e/wing_AR**2
        partials['wing_CDi', 'wing_e'] = -wing_CL**2/np.pi/wing_AR/wing_e**2

        

 
