from wordwrap import wrap


def test_wrap():
    assert wrap("the quick brown fox", 9) == ["the quick", "brown fox"]
