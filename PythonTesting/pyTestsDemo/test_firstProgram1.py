import pytest


def test_SalesforceLogin():
    print("Logged in successfully")
    
@pytest.mark.smoketest
def test_SalesforceLogout():
    # assert False, "Some Error Occured!"
    print("Logged out successfully")
