from djfly.core import DeckState


def test_tick_is_bounded():
    frame = DeckState().tick(0.5)
    assert 0.0 <= frame["energy"] <= 1.0
    assert 0.0 <= frame["groove"] <= 1.0
    assert 0.0 <= frame["pulse"] <= 1.0


def test_default_bpm():
    assert DeckState().bpm == 128.0
