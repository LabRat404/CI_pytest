from myApp import check_type

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
