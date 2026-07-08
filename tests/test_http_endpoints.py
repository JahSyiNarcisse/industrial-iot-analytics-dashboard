import unittest
from pathlib import Path

from src.app.main import root
from src.app.routes import (
    health, cpu, memory, disk, environment, system, network, machines, sensors
)


class RouteFunctionTests(unittest.TestCase):
    def test_root_payload(self):
        data = root()
        self.assertIn('message', data)
        self.assertIn('endpoints', data)

    def test_route_functions(self):
        self.assertEqual(health()['status'], 'ok')
        self.assertIsInstance(cpu()['percent'], (int, float))
        self.assertIn('total', memory())
        self.assertIn('total', disk())
        self.assertIn('python_version', environment())
        self.assertIn('platform', system())
        self.assertIn('bytes_sent', network())
        self.assertIsInstance(machines(), list)
        self.assertIsInstance(sensors(), list)

    def test_dashboard_template_exists(self):
        tpl = Path(__file__).resolve().parents[1] / 'src' / 'app' / 'templates' / 'dashboard.html'
        self.assertTrue(tpl.exists())


if __name__ == '__main__':
    unittest.main()
