"""Entity filters for ESP (engines vs coaches vs scenery)."""
from sodor_trainer.esp.entity_scanner import SodorEntity


def only_engines(ents: list[SodorEntity]) -> list[SodorEntity]:
    return [e for e in ents if e.health > 0 and e.name.startswith("entity_")]


def within(ents: list[SodorEntity], origin: tuple[float, float, float],
           radius: float) -> list[SodorEntity]:
    ox, oy, oz = origin
    out = []
    for e in ents:
        d2 = (e.x - ox) ** 2 + (e.y - oy) ** 2 + (e.z - oz) ** 2
        if d2 <= radius * radius:
            out.append(e)
    return out