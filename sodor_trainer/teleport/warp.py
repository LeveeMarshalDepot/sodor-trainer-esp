from sodor_trainer.core import offsets
from sodor_trainer.core.injector import Injector
from sodor_trainer.teleport.waypoints import SODOR_WAYPOINTS, Waypoint


class Warp:
    def __init__(self, inj: Injector) -> None:
        self.inj = inj

    def to_waypoint(self, key: str) -> bool:
        wp = SODOR_WAYPOINTS.get(key)
        if wp is None:
            return False
        self._apply(wp)
        return True

    def to_coords(self, x: float, y: float, z: float) -> None:
        self._apply(Waypoint("custom", x, y, z))

    def _apply(self, wp: Waypoint) -> None:
        self.inj.write_float(offsets.POS_X, wp.x)
        self.inj.write_float(offsets.POS_Y, wp.y)
        self.inj.write_float(offsets.POS_Z, wp.z)
        self.inj.write_float(offsets.SPEED, 0.0)