import unittest

from core.number.BigFloat import BigFloat

from position.Position import Position


class PositionTestCase(unittest.TestCase):

    def test_should_set_position_instrument_and_quantity(self):
        position = Position(instrument='GBP', quantity=BigFloat('1000.01'))
        self.assertEqual(position.instrument, 'GBP')
        self.assertEqual(position.quantity, BigFloat('1000.01'))


if __name__ == '__main__':
    unittest.main()
