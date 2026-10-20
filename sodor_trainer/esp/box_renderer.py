"""Projects 3D entity coordinates into 2D ESP boxes."""
from sodor_trainer.esp.entity_scanner import SodorEntity


class BoxRenderer:
    def __init__(self, width: int = 1920, height: int = 1080, fov: float = 90.0) -> None:
        self.w = width
        self.h = height
        self.fov = fov

    def project(self, ent: SodorEntity, cam: tuple[float, float, float],
                yaw: float) -> tuple[int, int] | None:
        import math
        dx = ent.x - cam[0]
        dz = ent.z - cam[2]
        dist = math.hypot(dx, dz)
        if dist < 0.1:
            return None
        angle = math.degrees(math.atan2(dx, dz)) - yaw
        angle = (angle + 180) % 360 - 180
        if abs(angle) > self.fov / 2:
            return None
        sx = int(self.w / 2 + (angle / (self.fov / 2)) * (self.w / 2))
        sy = int(self.h / 2 - (ent.y - cam[1]) * (self.h / max(dist, 1.0)))
        return sx, sy