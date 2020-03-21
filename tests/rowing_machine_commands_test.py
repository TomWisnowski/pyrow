from src import rowing_machine_commands
import unittest


class TestRowingCommands(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(len(rowing_machine_commands.RowingMachineComamands), 25)

if __name__ == '__main__':
    unittest.main()
