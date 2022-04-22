from position.Position import Position
from position.provider.supplier.PositionSupplier import PositionSupplier


class PositionProvider:

    def __init__(self, position_supplier: PositionSupplier):
        self.position_supplier = position_supplier

    def obtain_position(self) -> Position:
        return self.position_supplier.fetch_position()
