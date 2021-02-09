Required python packages:
- Logging
- time
- os
- unittest
- pytest
- inspect
- selenium

Technology/Framework Used:
- Python, Selenium
- Page Object Model

How to use:
- There is one test case regarding user logging story in tests/homepage/login_test.py 
module. The second regarding registration story is placed in tests/homepage/register_test.py
- There is screenshot functionality implemented as well with separate package in the project for them 
to be stored. As of the state the framework is right now, there should not be a trigger for screenshot
  in case of test_validLogin function as the credentials put as the arguments are those required to conduct
  chosen test scenario. If you'd like to check if screenshot function works correctly for this test case,
  please feel free to change credentials put into the login function.
- Second test case for registering story is set to create an account based on existing user credentials
and as I checked the scenario in regular browser there was no problem to observe an expected error message 
  to appear after clicking the 'Create Account' button, however Dribbble is protected by captcha in every 
  registering scenario so running this test case will surely lead to its failing and triggering of
  screenshot function. As I actually had very little time to prepare the framework because of preparation
  for my thesis defence, I had to leave it like it is, so I apologize. 
- It is possible to choose the browser to run the tests in pytest, I was mainly testing on firefox and thus
it is set as the default browser to run them. To use different browser(before running tests please
  make sure you have a PATH variable set) try running e.g.
py.test -s -v tests/homepage --browser chrome
- For logs from script run, please refer to automation.log file
- I use teststatus module to allow test cases do more assertions than one. Not useful in this particular case
but could be handy with more complex text cases