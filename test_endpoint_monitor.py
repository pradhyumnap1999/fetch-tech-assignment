import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from endpoint_monitor import monitor_endpoints, calculate_availability
from endpoint_monitor import check_health

class TestEndpointMonitor(unittest.TestCase):
    def setUp(self):
        # Mock requests.request to simulate a successful response
        self.requests_patcher = patch('requests.request')
        self.mock_request = self.requests_patcher.start()

    def tearDown(self):
        self.requests_patcher.stop()

    def test_check_health_success(self):
        # Simulate a successful response
        self.mock_request.return_value = MagicMock(status_code=200, elapsed=MagicMock(total_seconds=lambda: 0.2))

        endpoint = {'url': 'https://fetch.com/'}
        result = check_health(endpoint)

        self.assertTrue(result)

    def test_check_health_failure_status_code(self):
        # Simulate a failure due to non-2xx status code
        self.mock_request.return_value = MagicMock(status_code=404, elapsed=MagicMock(total_seconds=lambda: 0.2))

        endpoint = {'url': 'https://fetch.com/'}
        result = check_health(endpoint)

        self.assertFalse(result)

    def test_check_health_failure_latency(self):
        # Simulate a failure due to response latency exceeding 500 ms
        self.mock_request.return_value = MagicMock(status_code=200, elapsed=MagicMock(total_seconds=lambda: 0.6))

        endpoint = {'url': 'https://fetch.com/'}
        result = check_health(endpoint)

        self.assertFalse(result)

    def test_monitor_endpoints_keyboard_interrupt(self):
        # Simulate KeyboardInterrupt to stop monitoring
        with patch('builtins.input', side_effect=KeyboardInterrupt()):
            with patch('builtins.print') as mock_print:
                monitor_endpoints([{'url': 'https://fetch.com/'}])

                # Verify that the program prints the correct message
                mock_print.assert_called_with("Monitoring stopped by user.")

    def test_calculate_availability(self):
        # Test availability calculation
        stats = {'up': 3, 'total': 5}
        result = calculate_availability(stats)

        self.assertEqual(result, 60.0)

    def test_calculate_availability_no_tests(self):
        # Test availability calculation when no tests have been performed yet
        stats = {'up': 0, 'total': 0}
        result = calculate_availability(stats)

        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()

    