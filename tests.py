import calculator
import pytest

calc = calculator.Calculator()


def test_01():
    """Emtpy string test"""
    assert calc.add("") == 0


def test_02():
    """White space string test"""
    assert calc.add(" ") == 0


def test_03():
    """One number in string test"""
    assert calc.add("1") == 1


def test_04():
    """Two numbers string test"""
    assert calc.add("1,2") == 3


def test_05():
    """More than two numbers in string test"""
    assert calc.add("1,2,3,4,5,6,7") == 28


def test_06():
    """String with letters test"""
    with pytest.raises(ValueError):
        calc.add("1,2,Lersre,2,D")


def test_07():
    """New line as delimeter"""
    assert calc.add("1\n2,3") == 6


def test_08():
    """Custom delimeter"""
    assert calc.determine_delimiter("//[;]\n1;2")[0] == ';'


def test_09():
    """Custom delimeter add"""
    assert calc.add("//[;]\n1;2") == 3


def test_10():
    """Two delimeters in row (test empty string input)"""
    assert calc.add("1, ,2") == 3


def test_11():
    """ValueError test"""
    with pytest.raises(ValueError) as info:
        calc.add("1,-2,-3")
    assert str(info.value) == 'negatives not allowed -2, -3'


def test_12():
    """Number bigger than 1000"""
    assert calc.add("1001,1,3") == 4


def test_13():
    """Number equal 1000"""
    assert calc.add("1000,2,5") == 1007


def test_14():
    """Multiple character delimiter"""
    assert calc.add("//[***]\n1***2***3") == 6