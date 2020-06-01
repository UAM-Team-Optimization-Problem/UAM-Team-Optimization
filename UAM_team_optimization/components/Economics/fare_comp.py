import numpy as np
from openmdao.api import ExplicitComponent


class FareComp(ExplicitComponent):

    def setup(self):
        self.add_input('Price_km')
        self.add_input('distance')
        self.add_input('v_drive')
        self.add_input('v_inf')
        self.add_input('t_tol')
        self.add_input('savings')
        self.add_output('Fare')

        self.declare_partials('Fare', 'Price_km')
        self.declare_partials('Fare', 'v_inf')
        self.declare_partials('Fare', 'v_drive')
        self.declare_partials('Fare', 'distance')
        self.declare_partials('Fare', 't_tol')
        self.declare_partials('Fare', 'savings')
    def compute(self, inputs, outputs):
        
        Price_km = inputs['Price_km']
        v_inf = inputs['v_inf']*3.6
        distance = inputs['distance']/1000
        v_drive = inputs['v_drive']
        t_tol = inputs['t_tol']
        savings = inputs['savings']
        

        outputs['Fare'] = Price_km * distance + (((distance/v_drive)-((distance/v_inf) + t_tol)) * savings)

    def compute_partials(self, inputs, partials):
       
        Price_km = inputs['Price_km']
        v_inf = inputs['v_inf']*3.6
        distance = inputs['distance']/1000
        v_drive = inputs['v_drive']
        t_tol = inputs['t_tol']
        savings = inputs['savings']


        partials['Fare', 'v_inf'] = distance*savings/v_inf**2
        partials['Fare', 'v_drive'] = -distance * savings / v_drive**2
        partials['Fare', 'distance'] = savings*((1/v_drive)-(1/v_inf))+ Price_km
        partials['Fare', 't_tol'] = -savings
        partials['Fare', 'savings'] = (distance/v_drive)-(distance/v_inf)-t_tol
        partials['Fare', 'Price_km'] = distance 