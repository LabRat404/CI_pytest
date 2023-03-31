from myApp import check_type
from myApp import check_name
from myApp import check_name_len
from myApp import check_sid_len
def test_check_type():
    assert check_type() == False
    assert check_type('test') == True
    try:
        check_type(123)
    except TypeError:
        assert True
    else:
        assert False

    myname = "john"
    myId = 123456789
    assert check_type(myname, myId) == True


    myId2 = "123456789"
    assert check_type(myname, myId2) == True

    myId3 = "123456789a"
    assert check_type(myname, myId3) == False

    myId4 = "a_john"
    assert check_type(myname, myId4) == False


def test_check_name():
    assert check_name("abc") == True
    assert check_name("ab ") == False
    assert check_name("\xaa\xaa") == True
    assert check_name("\xaa \xaa") == True
    assert check_name("\xaa \xaa") == True
    assert check_name("\xaa \xfa ") == False
    assert check_name("中文_is_printable") == True

def test_check_name_len():
    assert check_name_len("abc") == True
    assert check_name_len("abc abc") == True
    assert check_name_len("\xaa\xaa") == True
    assert check_name_len("\xaa \xaa") == True
    assert check_name_len("abc abc abc abc abc a") == False
    assert check_name_len("\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa") == True
    assert check_name_len("\xaa\xaa\xaa\xaa\xaa \xaa\xaa\xaa\xaa\xaa") == False


def test_check_sid_len():
    assert check_sid_len("1155") == False
    assert check_sid_len("1155111111") == True
    assert check_sid_len("115511111 ") == False
    assert check_sid_len(115511111) == False
    assert check_sid_len(1155111111) == True
    assert check_sid_len("1155 11111") == False



