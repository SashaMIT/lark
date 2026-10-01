from lark.utils import TextSlice

import pytest


def test_textslice_rejects_an_end_past_the_text():
    with pytest.raises(AssertionError):
        TextSlice("hello", 0, 100)
    with pytest.raises(AssertionError):
        TextSlice("hello", 0, -100)
    with pytest.raises(AssertionError):
        TextSlice("hello", 10, 12)

    view = TextSlice("hello", 1, -1)
    assert (view.start, view.end, len(view)) == (1, 4, 3)
