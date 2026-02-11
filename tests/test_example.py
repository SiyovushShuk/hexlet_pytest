from hexlet_pytest.example import reverse
import pytest


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""

@pytest.fixture
def arr():
    return [1, 2, 3, 4]


def test_example(arr):
    assert [1, 2, 3, 4] == arr
    print('Hello')