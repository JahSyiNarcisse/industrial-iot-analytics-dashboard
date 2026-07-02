import unittest

from src.app.routes import cpu, disk, health, memory, network, system


class RouteTests(unittest.TestCase):
    def test_health_endpoint(self):
        payload = health()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["version"], "0.1.0")
        self.assertIn("timestamp", payload)

    def test_cpu_endpoint(self):
        payload = cpu()
        self.assertIn("percent", payload)
        self.assertIsInstance(payload["percent"], (int, float))

    def test_memory_endpoint(self):
        payload = memory()
        self.assertIn("total", payload)
        self.assertIn("available", payload)
        self.assertIn("used", payload)
        self.assertIn("percent", payload)

    def test_disk_endpoint(self):
        payload = disk()
        self.assertIn("total", payload)
        self.assertIn("free", payload)
        self.assertIn("used", payload)
        self.assertIn("percent", payload)

    def test_system_endpoint(self):
        payload = system()
        self.assertIn("platform", payload)
        self.assertIn("boot_time", payload)
        self.assertIn("hostname", payload)

    def test_network_endpoint(self):
        payload = network()
        self.assertIn("bytes_sent", payload)
        self.assertIn("bytes_received", payload)
        self.assertIn("packets_sent", payload)
        self.assertIn("packets_received", payload)


if __name__ == "__main__":
    unittest.main()
