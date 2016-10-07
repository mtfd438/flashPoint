# Python Selenium Examples


## Tests included
- Verify Docker site search will return 0 search results if search querey is not found
- Verify Docker site search will return search results if search querey is found
- Verify an user can successfully login into Docker with active account credentials
- Verify user cannot login to Docker with bad credentials and login error alert is displayed
- Verify a new user can successfully signup for new Docker account

## How to run tests
- Edit Conf.ini file to add credentials for running login tests and signup tests
- From command line python script.py
- Testing script names test_login.py test_search.py test_singup.py

##TODOs
- Add test for a new user attempting to signing up with an exitisting ID
- Add robust error logging







