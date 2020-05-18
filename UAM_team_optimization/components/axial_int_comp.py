from openmdao.api import ExplicitComponent
import numpy as np

class AxialIntComp(ExplicitComponent):
# cl for section of the tail that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('thrust_coeff')
        self.add_output('axial_int_fac')

        self.declare_partials('axial_int_fac','thrust_coeff')

    def compute(self, inputs, outputs):
        thrust_coeff = inputs['thrust_coeff']

        outputs['axial_int_fac'] = (-1 + np.sqrt(1 + thrust_coeff**2))/2

    def compute_partials(self, inputs, partials):
        thrust_coeff = inputs['thrust_coeff']
        
        partials['axial_int_fac', 'thrust_coeff'] = thrust_coeff/(2*np.sqrt(1 + thrust_coeff**2))
        
 