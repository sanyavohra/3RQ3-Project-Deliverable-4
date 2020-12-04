from testproject.orderScheduling import OrderScheduling

def test_scheduled_time_available(): # in this test, the order will be successfully scheduled
    availableTimes = [ # sets the available times for this test
        "1PM",
    ]

    orderscheduling = OrderScheduling()
    for time in availableTimes:
        assert orderscheduling.accept_time(time) == True, "The time for pickup is scheduled"
        # the time selected matches the available times so the order is scheduled successfully

def test_profile_login_invalid(): # in this test, the order will not be scheduled
    availableTimes = [ # sets the available times for this test
        "1PM",
    ]

    orderscheduling = OrderScheduling()
    if time not in availableTimes:
        assert profile.verify_login(username) == False, "That is not a valid time for pickup"
        # the time selected is not a valid time, the order is not scheduled