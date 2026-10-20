from sodor_trainer.core import offsets


def test_player_offsets_are_ordered():
    assert offsets.HEALTH < offsets.COAL < offsets.POS_X < offsets.SPEED


def test_entity_stride_multiple_of_4():
    assert offsets.ENTITY_STRIDE % 4 == 0