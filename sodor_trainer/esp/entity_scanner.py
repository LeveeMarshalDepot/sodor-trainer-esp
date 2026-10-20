from dataclasses import dataclass

from sodor_trainer.core import offsets
from sodor_trainer.core.injector import Injector


@dataclass
class SodorEntity:
    address: int
    name: str
    x: float
    y: float
    z: float
    health: float


class EntityScanner:
    def __init__(self, injector: Injector) -> None:
        self.inj = injector

    def scan(self) -> list[SodorEntity]:
        out: list[SodorEntity] = []
        count = int(self.inj.read_float(offsets.ENTITY_COUNT))
        for i in range(min(count, 64)):
            addr = offsets.ENTITY_LIST + i * offsets.ENTITY_STRIDE
            x = self.inj.read_float(addr + offsets.ENTITY_POS)
            y = self.inj.read_float(addr + offsets.ENTITY_POS + 4)
            z = self.inj.read_float(addr + offsets.ENTITY_POS + 8)
            hp = self.inj.read_float(addr + offsets.ENTITY_HEALTH)
            if -1e6 < x < 1e6:
                out.append(SodorEntity(addr, f"entity_{i}", x, y, z, hp))
        return out