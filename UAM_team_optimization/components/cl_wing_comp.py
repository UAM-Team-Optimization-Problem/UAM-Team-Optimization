from openmdao.api import ExplicitComponent


class CLWingComp(ExplicitComponent):
# cl for section of the wing that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('wing_alpha')
        self.add_input('wing_CLa')
        self.add_input('wing_CL0')
        self.add_input('axial_int_fac')
        self.add_input('wing_blown_percent')
       
        self.add_output('wing_CL')

        self.declare_partials('wing_CL','wing_alpha')
        self.declare_partials('wing_CL','wing_CLa')
        self.declare_partials('wing_CL','wing_CL0')
        self.declare_partials('wing_CL','axial_int_fac')
        self.declare_partials('wing_CL','wing_blown_percent')


    def compute(self, inputs, outputs):
        wing_alpha = inputs['wing_alpha']
        wing_CLa = inputs['wing_CLa']
        wing_CL0 = inputs['wing_CL0']
        axial_int_fac = inputs['axial_int_fac']
        wing_blown_percent = inputs['wing_blown_percent']

        outputs['wing_CL'] = (wing_CLa * wing_alpha + wing_CL0) + (wing_CLa * wing_alpha + wing_CL0)*wing_blown_percent*((1+axial_int_fac)**2 - 1)

    def compute_partials(self, inputs, partials):
        wing_alpha = inputs['wing_alpha']
        wing_CLa = inputs['wing_CLa']
        wing_CL0 = inputs['wing_CL0']
        axial_int_fac = inputs['axial_int_fac']
        wing_blown_percent = inputs['wing_blown_percent']

        partials['wing_CL', 'wing_alpha'] = wing_CLa + wing_CLa*wing_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['wing_CL', 'wing_CLa'] = wing_alpha + wing_alpha*wing_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['wing_CL', 'wing_CL0'] = 1 + wing_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['wing_CL', 'axial_int_fac'] = 2*(wing_CLa * wing_alpha + wing_CL0)*wing_blown_percent*(1+axial_int_fac)
        partials['wing_CL', 'wing_blown_percent'] = (wing_CLa * wing_alpha + wing_CL0)*((1+axial_int_fac)**2 - 1)

 
