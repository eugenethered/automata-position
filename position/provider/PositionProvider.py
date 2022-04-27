from positionrepo.Position import Position
from positionrepo.PositionSlip import Status
from positionrepo.repository.PositionRepository import PositionRepository
from positionrepo.repository.PositionSlipRepository import PositionSlipRepository

from position.provider.supplier.PositionSupplier import PositionSupplier


class PositionProvider:

    def __init__(self, position_supplier: PositionSupplier, position_repository: PositionRepository, position_slip_repository: PositionSlipRepository):
        self.position_supplier = position_supplier
        self.position_repository = position_repository
        self.position_slip_repository = position_slip_repository

    def obtain_position(self) -> Position:
        position_slip = self.position_slip_repository.retrieve()
        positions = self.position_supplier.get_positions()
        position = self.choose_position_based_on_slip(positions, position_slip)
        if position is not None:
            self.use_position_slip(position_slip)
            self.position_repository.store(position)
        return position

    def use_position_slip(self, position_slip):
        position_slip.status = Status.USED
        self.position_slip_repository.store(position_slip)

    @staticmethod
    def choose_position_based_on_slip(positions, position_slip) -> Position:
        eligible_positions = [p for p in positions if p.instrument == position_slip.instrument and position_slip.status is not Status.USED]
        if len(eligible_positions) > 0:
            return eligible_positions[0]
        return None
