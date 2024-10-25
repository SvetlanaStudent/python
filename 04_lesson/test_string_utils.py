
import pytest
from StringUtils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize('string, result', [("katya","Katya"),("345", "345"),
        ("Здраствуйте!", "Здраствуйте!"),
        ("н ", "Н ")
                ])
def test_capitilize_positive(string, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [("", ""), ("  ", "  "),
                                    ])
def test_capitilize_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [(" Katya", "Katya"), ("   ЛЕТО", "ЛЕТО"),
                                           ("Здраствуйте 1", "Здраствуйте 1")
                                           ])
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("", ""), ("   ", ""),
                                           ("Здраст вуйте", "Здраст вуйте")
                                           ])
def test_trim_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [(" Katya", "Katya"), ("   ЛЕТО", "ЛЕТО"),
                                           ("Здраствуйте 1", "Здраствуйте 1")
                                           ])
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("", ""), ("   ", ""),
                                           ("Здраст вуйте", "Здраст вуйте")
                                           ])
def test_trim_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

def test_to_list():
    res= string_utils.to_list("1,2,3,4")
    assert res == ["1", "2", "3", "4"]

    res= string_utils.to_list("1:2:3:4", ":")
    assert res == ["1", "2", "3", "4"]