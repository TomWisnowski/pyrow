from src import pyrow
import unittest
import mock


class TestMyClass(unittest.TestCase):

    def test_that_we_call_pyrow_monitor(self):
        myOrchestrator = new Orchestrator()

        mockPyrow = mock(Pyrow.class)
        mockQueueService = mock(QueueService.class)

        expectedMonitorResult = {}
        when(mockPyrow.get_monitor()).thenReturn(expectedMonitorResult)

        myOrchestrator.orchestrate(mockPyrow, mockQueueService)
        
        self.assertCalledTimes(mockPyrow.get_monitor(),1)
        self.assertCalledTimes(mockQueueService.send(expectedMonitorResult),1)

if __name__ == '__main__':
    unittest.main()