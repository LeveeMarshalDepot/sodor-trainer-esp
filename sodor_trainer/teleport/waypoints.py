from dataclasses import dataclass


@dataclass
class Waypoint:
    name: str
    x: float
    y: float
    z: float


SODOR_WAYPOINTS: dict[str, Waypoint] = {
    "tidmouth_sheds": Waypoint("Tidmouth Sheds", 1024.0, 12.5, -880.0),
    "knapford_station": Waypoint("Knapford Station", 640.0, 14.0, 220.0),
    "gordon_hill": Waypoint("Gordon's Hill", -1100.0, 88.0, 430.0),
    "blue_mountain_quarry": Waypoint("Blue Mountain Quarry", 2100.0, 45.0, 1500.0),
    "brendam_docks": Waypoint("Brendam Docks", -2200.0, 3.0, -1800.0),
    "victorstown": Waypoint("Vicarstown", 3200.0, 22.0, -400.0),
}