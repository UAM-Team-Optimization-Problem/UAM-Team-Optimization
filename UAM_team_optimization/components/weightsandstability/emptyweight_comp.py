from openmdao.api import ExplicitComponent


class EmptyWeightComp(ExplicitComponent):
    def initialize(self):
        self.options.declare('rho', types=float)

    def setup(self):
        self.add_input('wing_area')
        self.add_input('wing_tc')
        self.add_input('wing_AR')
        self.add_input('tail_area')
        self.add_input('tail_tc')
        self.add_input('tail_AR')
        self.add_input('load_factor')
        self.add_input('w_design')
        self.add_input('w_else')
        self.add_input('v_inf')
        self.add_output('EmptyWeight')


        self.declare_partials('EmptyWeight', 'wing_area')
        self.declare_partials('EmptyWeight', 'wing_tc')
        self.declare_partials('EmptyWeight', 'wing_AR')
        self.declare_partials('EmptyWeight', 'tail_area')
        self.declare_partials('EmptyWeight', 'tail_tc')
        self.declare_partials('EmptyWeight', 'tail_AR')
        self.declare_partials('EmptyWeight', 'load_factor')
        self.declare_partials('EmptyWeight', 'w_design')
        self.declare_partials('EmptyWeight', 'w_else')
        self.declare_partials('EmptyWeight', 'v_inf')

    def compute(self, inputs, outputs):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        w_else = inputs['w_else']
        v_inf = inputs['v_inf']

        outputs['EmptyWeight'] = 0.036* \
                            (wing_area**0.758)* \
                            (wing_AR**0.6)* \
                            ((0.5*rho*v_inf*v_inf)**0.006)* \
                            ((100*wing_tc)**-0.3)* \
                            ((load_factor*w_design)**0.49) + \
                            0.016* \
                            ((load_factor*w_design)**0.414)* \
                            ((0.5*rho*v_inf*v_inf)**0.168)* \
                            (tail_area**0.896)* \
                            ((100*tail_tc)**-0.12)* \
                            (tail_AR**0.043) + \
                            w_else

    def compute_partials(self, inputs, partials):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        w_else = inputs['w_else']
        v_inf = inputs['v_inf']

        partials['EmptyWeight', 'wing_area'] = 0.036* \
                                               0.758*(wing_area**(1-0.758))* \
                                               (wing_AR**0.6)* \
                                               ((0.5*rho*v_inf*v_inf)**0.006)* \
                                               ((100*wing_tc)**-0.3)* \
                                               ((load_factor*w_design)**0.49)

        partials['EmptyWeight', 'wing_tc'] = 0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**0.6)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             100*(-0.3)*((100*wing_tc)**(-0.3-1))* \
                                             ((load_factor*w_design)**0.49)

        partials['EmptyWeight', 'wing_AR'] = 0.6*0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**-0.4)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             ((100*wing_tc)**-0.3)* \
                                             ((load_factor*w_design)**0.49)

        partials['EmptyWeight', 'tail_area'] = 0.016* \
                                               ((load_factor*w_design)**0.414)* \
                                               ((0.5*rho*v_inf*v_inf)**0.168)* \
                                               0.896*(tail_area**(1-0.896))* \
                                               ((100*tail_tc)**-0.12)* \
                                               (tail_AR**0.043)

        partials['EmptyWeight', 'tail_tc'] = 0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             100*(-0.12)*((100*tail_tc)**(-0.12-1))* \
                                             (tail_AR**0.043)

        partials['EmptyWeight', 'tail_AR'] = 0.043*0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             ((100*tail_tc)**-0.12)* \
                                             (tail_AR**-0.957)

        partials['EmptyWeight', 'load_factor'] = 0.036* \
                                                 (wing_area**0.758)* \
                                                 (wing_AR**0.6)* \
                                                 ((0.5*rho*v_inf*v_inf)**0.006)* \
                                                 ((100*wing_tc)**-0.3)* \
                                                 w_design*0.49*((load_factor*w_design)**(1-0.49)) + \
                                                 0.016* \
                                                 w_design*0.414*((load_factor*w_design)**(1-0.414))* \
                                                 ((0.5*rho*v_inf*v_inf)**0.168)* \
                                                 (tail_area**0.896)* \
                                                 ((100*tail_tc)**-0.12)* \
                                                 (tail_AR**0.043)

        partials['EmptyWeight', 'w_design'] = 0.036* \
                                              (wing_area**0.758)* \
                                              (wing_AR**0.6)* \
                                              ((0.5*rho*v_inf*v_inf)**0.006)* \
                                              ((100*wing_tc)**-0.3)* \
                                              load_factor*0.49*((load_factor*w_design)**(1-0.49)) + \
                                              0.016* \
                                              load_factor*0.414*((load_factor*w_design)**(1-0.414))* \
                                              ((0.5*rho*v_inf*v_inf)**0.168)* \
                                              (tail_area**0.896)* \
                                              ((100*tail_tc)**-0.12)* \
                                              (tail_AR**0.043)

        partials['EmptyWeight', 'w_else'] = 1.

        partials['EmptyWeight', 'v_inf'] = 0.036* \
                                           (wing_area**0.758)* \
                                           (wing_AR**0.6)* \
                                           ((100*wing_tc)**-0.3)* \
                                           ((load_factor*w_design)**0.49)* \
                                           ((0.5*rho)**0.006)* \
                                           (0.012)* \
                                           (v_inf**(0.012 - 1)) + 0.016* \
                                           ((load_factor*w_design)**0.414)* \
                                           (tail_area**0.896)* \
                                           ((100*tail_tc)**-0.12)* \
                                           (tail_AR**0.043)* \
                                           ((0.5*rho)**0.168)* \
                                           (2*0.168)* \
                                           (v_inf**(2*0.168 - 1))
