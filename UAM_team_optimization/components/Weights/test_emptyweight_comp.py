import unittest

# from emptyweight_comp import EmptyWeightComp
from UAM_team_optimization.components.weightsandstability.emptyweight_comp import EmptyWeightComp
from openmdao.api import Problem
from openmdao.utils.assert_utils import assert_check_partials


class TestEmptyWeightComp(unittest.TestCase):
    def test_component_and_derivatives(self):
        prob = Problem()
        prob.model = EmptyWeightComp(rho=1.2)
        prob.setup()
        prob.run_model()

        data = prob.check_partials(out_stream=None)
        assert_check_partials(data, atol=1.e-3, rtol=1.e-3)

if __name__ == '__main__':
    unittest.main()
