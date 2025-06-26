

#Unit test file for phone_number_location_tracker



#importing the track_location() function to test it
from signalWalker import track_location







def test_track_location():
    """function to test the track_location() function
    ----
    Note:
    This test will only pass if your API KEY is set in the environment 
    variable and the specified number is registered as valid in the API.
    In unit testing, it is generally best practice to mock API or 
    external service calls (to avoid making repeated API calls).
    If desired, you can write more advanced tests using pytest or unittest.mock .
    """


   #testing the function using a dummy phone number and username
    dummy_username: str="Dummy_User"
    dummy_phone_number: str= "+12025550123"
    assert track_location(dummy_username, dummy_phone_number) is True




