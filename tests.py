import calculator

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
    assert calc.add("1,2,Lersre,2,D") == 5


def test_07():
    """New line as delimeter"""
    assert calc.add("1\n2,3") == 6


def test_08():
    """Custon delimeter"""
    assert calc.determine_delimeter("//[;]\n1;2")[0] == ';'

def test_09():
    """Custon delimeter add"""
    assert calc.add("//[;]\n1;2") == 3