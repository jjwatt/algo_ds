import unittest

from unittest.mock import patch

import backoff
from backoff import retry_with_backoff

class TestRetryDecorator(unittest.TestCase):

    def setUp(self):
        if hasattr(self, 'flaky_function_decorated'):
            delattr(self, 'flaky_function_decorated')

    def test_function_succeeds_on_retry(self):
        @retry_with_backoff(max_retries=3, initial_delay=0, random_range=0)
        def flaky_function():
            if not hasattr(flaky_function, 'counter'):
                flaky_function.counter = 0
            flaky_function.counter += 1
            if flaky_function.counter < 3:
                raise ValueError('Simulated failure')
            return 'Success'
        result = flaky_function()
        self.assertEqual(result, 'Success')
        self.assertEqual(flaky_function.counter, 3)


    def test_function_fails_after_max_retries(self):
        @retry_with_backoff(max_retries=2, initial_delay=0, random_range=0)
        def failing_function():
            if not hasattr(failing_function, 'counter'):
                failing_function.counter = 0
            failing_function.counter += 1
            raise ValueError('Always fails')
        with self.assertRaises(ValueError):
            failing_function()
        self.assertEqual(failing_function.counter, 2)

    @patch('time.sleep')
    def test_delays_between_retries(self, mock_sleep):
        @retry_with_backoff(max_retries=3, initial_delay=0.1, random_range=0)
        def flaky_function():
            if not hasattr(flaky_function, 'counter'):
                flaky_function.counter = 0
            flaky_function.counter += 1
            if flaky_function.counter < 3:
                raise ValueError("Simulated failure")
            return "Success"
        flaky_function()
        self.assertEqual(mock_sleep.call_count, 2)
        expected_calls = [unittest.mock.call(0.1), unittest.mock.call(0.2)]
        mock_sleep.assert_has_calls(expected_calls, any_order=False)

            
if __name__ == "__main__":
    unittest.main()
