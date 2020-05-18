from openmdao.api import ExplicitComponent

import numpy as np

class CDiTailComp(ExplicitComponent):


    def setup(self):
        self.add_input('tail_CL')
        self.add_input('tail_AR')
        self.add_input('tail_e')
       
        self.add_output('tail_CDi')

        self.declare_partials('tail_CDi','tail_CL')
        self.declare_partials('tail_CDi','tail_AR')
        self.declare_partials('tail_CDi','tail_e')

    def compute(self, inputs, outputs):
        
        tail_CL = inputs['tail_CL']
        tail_AR = inputs['tail_AR']
        tail_e = inputs['tail_e']
        
        outputs['tail_CDi'] = tail_CL ** 2. /np.pi /tail_e /tail_AR

    def compute_partials(self, inputs, partials):
        
        tail_CL = inputs['tail_CL']
        tail_AR = inputs['tail_AR']
        tail_e = inputs['tail_e']


        partials['tail_CDi', 'tail_CL'] =  2 * tail_CL / np.pi / tail_e / tail_AR
        partials['tail_CDi', 'tail_AR'] = -tail_CL**2/np.pi/tail_e/tail_AR**2
        partials['tail_CDi', 'tail_e'] = -tail_CL**2/np.pi/tail_e**2/tail_AR

        

 
