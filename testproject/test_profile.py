from testproject.profile import Profile

def test_profile_login_verified(): # in this test, the profile is logged into successfully
    valid_login = [ # sets the valid login details (username, password)
        "sanya","1234"
        "sean","4321"
    ]

    profile = Profile()
    for username in valid_login: # looks through the valid login details list for a username that matches
        assert profile.verify_login(username) == True, "The username is valid" # the username entered matches one in the valid login details list

    for password in valid_login: # looks through the valid login details list for a password that matches
        assert profile.verify_login(password) == True, "The password is valid" # the password entered matches one in the valid login details list

def test_profile_login_invalid(): # in this test, the profile is not logged into successfully
    valid_login = [ # sets the valid login details (username, password)
        "sanya","1234"
        "sean","4321"
    ]

    profile = Profile()
    if username not in valid_login:
        assert profile.verify_login(username) == False, "The username is invalid"
        # if the username is not in the valid login details list, the username is invalid

    if password not in valid_login:
        assert profile.verify_login(password) == False, "The password is invalid"
        # if the passsword is not in the valid login details list, the password is invalid