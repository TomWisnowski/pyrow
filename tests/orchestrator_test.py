import unittest

from mock import Mock

from src.orchestrator import Orchestrator
from tests.chance import Chance

chance = Chance()


class TestMyClass(unittest.TestCase):

    def test_that_we_call_pyrow_monitor(self):
        my_orchestrator = Orchestrator()

        mock_pyrow = Mock()
        mock_queue_service = Mock()
        mock_time = Mock()

        expected_monitor_result = chance.string()
        mock_pyrow.get_monitor.return_value = expected_monitor_result

        my_orchestrator.orchestrate(mock_pyrow, mock_queue_service, mock_time)

        mock_pyrow.get_monitor.assert_called_with()
        mock_queue_service.send.assert_called_with(expected_monitor_result)
        mock_time.sleep.assert_called_with(1)


if __name__ == '__main__':
    unittest.main()
