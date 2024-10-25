
import pytest
from StringUtils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize('string, result', [("katya", "Katya"), ("345", "345"),
        ("Здраствуйте!", "Здраствуйте!"),
        ("н ", "Н ")
                ])
def test_capitilize_positive(string, result):
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [("", ""), ("  ", "  "),
                                    ])
def test_capitilize_negative(string, result):
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [(" Katya", "Katya"), ("   ЛЕТО", "ЛЕТО"),
                                           ("Здраствуйте 1", "Здраствуйте 1")
                                           ])
def test_trim_positive(string, result):
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("", ""), ("   ", ""),
                                           ("Здраст вуйте", "Здраст вуйте")
                                           ])
def test_trim_negative(string, result):
    res = string_utils.trim(string)
    assert res == result

def test_to_list_positive():
    res= string_utils.to_list("1,2,3,4")
    assert res == ["1", "2", "3", "4"]

    res= string_utils.to_list("1:2:3:4", ":")
    assert res == ["1", "2", "3", "4"]

def test_to_list_negative():
    res= string_utils.to_list("")
    assert res == []

    res = string_utils.to_list(" : : ")
    assert res == [' : : ']

def test_contains_positive():
    res= string_utils.contains("Компания", "м")
    assert res == True

    res = string_utils.contains("Компания 345", "5")
    assert res == True

def test_contains_positive():
    res= string_utils.contains("Компания", "G")
    assert res == False

    res= string_utils.contains("Компания", "344")
    assert res == False

def test_delete_symbol_positive():
    res= string_utils.delete_symbol("Svetlana", "S")
    assert res == "vetlana"

    res = string_utils.delete_symbol("Я купила кофе", "к")
    assert res == "Я упила офе"

def test_delete_symbol_negative():
    res= string_utils.delete_symbol("", "S")
    assert res == ""

    res = string_utils.delete_symbol("   ", "")
    assert res == "   "

def test_starts_with_positive():
    res= string_utils.starts_with("Svetlana 3455", "S")
    assert res == True

    res = string_utils.starts_with("#$%^&& 3455", "#")
    assert res == True

def test_starts_with_negative():
    res= string_utils.starts_with("Svetlana 3455", "%")
    assert res == False

    res = string_utils.starts_with("", "%")
    assert res == False

def test_end_with_positive():
    res= string_utils.end_with("Svetlana 3455", "5")
    assert res == True

    res = string_utils.end_with("arguments", "s")
    assert res == True

def test_end_with_positive():
    res= string_utils.end_with("Svetlana 3455", "G")
    assert res == False

    res = string_utils.end_with("Svetlana 3455", "Gghj")
    assert res == False

def test_is_empty_positive():
    res= string_utils.is_empty("")
    assert res == True

    res = string_utils.is_empty("   ")
    assert res == True

def test_is_empty_negative():
    res= string_utils.is_empty("#$%%%")
    assert res == False

    res = string_utils.is_empty("Я купила кофе")
    assert res == False

def test_list_to_string_positive():
    res= string_utils.list_to_string(["DF","GH","HJ","jk"])
    assert res == "DF, GH, HJ, jk"

    res = string_utils.list_to_string(["DF", "GH", "HJ", "jk"], "-")
    assert res == "DF-GH-HJ-jk"

def test_list_to_string_negative():
    res= string_utils.list_to_string([])
    assert res == ""

    res = string_utils.list_to_string([   ])
    assert res == ""