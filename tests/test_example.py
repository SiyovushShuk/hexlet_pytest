from hexlet_pytest.example import reverse
import pytest
from pathlib import Path


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return open(get_test_data_path(filename)).read()

@pytest.fixture
def inputfile():
    return read_file('input.txt')

@pytest.fixture
def expected_data():
    return read_file('result.txt')


def test_base(inputfile, expected_data):
    reversed_str = reverse(inputfile)
    assert reversed_str == expected_data