from testproject.profile import Profile
from testproject.orderHistory import OrderHistory
# both the profile login details and the order history classes are required in this function

def test_order_history_valid(): # in this test, order history is to be recorded
    if verify_login(username, password)== True: # checks if the user is logged in, it is True
        assert OrderHistory.record(details)== True # record order history

def test_order_history_invalid(): # in this test, order history is not to be recorded
    if verify_login(username, password)== False: # checks if the user is logged in, it is False
        assert OrderHistory.record(details)== False # does not record order history
