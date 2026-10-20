from sodor_trainer.teleport.waypoints import SODOR_WAYPOINTS


def test_waypoints_have_expected_keys():
    for key in ("tidmouth_sheds", "knapford_station", "gordon_hill"):
        assert key in SODOR_WAYPOINTS


def test_waypoint_coords_are_floats():
    for wp in SODOR_WAYPOINTS.values():
        assert isinstance(wp.x, float)
        assert isinstance(wp.y, float)
        assert isinstance(wp.z, float)