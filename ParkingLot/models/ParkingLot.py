import uuid
from typing import List

from LLD.ParkingLot.models.Floor import Floor


class ParkingLot:
    def __init__(self):
        self._id = uuid.uuid4()
        self._floors: List[Floor] = []

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def floors(self):
        return self._floors

