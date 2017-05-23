import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

web_driver = raw_input("Please enter the file location of your webdriver:\n")

if "chrome" in web_driver:
    os.environ["webdriver.chrome.driver"] = web_driver
elif "firefox" in web_driver:
    os.environ["webdriver.firefox.driver"] = web_driver
else:
    print "Please change the webdriver in the code from line 20"
    exit(1)

browser = webdriver.Chrome(web_driver)
browser.get("https://www.twitter.com")

# Test 1. Test to see if user can successfully login

print "\nTEST 1:"
MY_SCREEN_NAME = raw_input("\nPlease enter your username: ")
MY_PASSWORD = raw_input("\nPlease enter your password: ")

# Find the login button on the page
element = browser.find_element_by_css_selector("[class='Button StreamsLogin js-login']")

# Click the login button
element.click()

# Find the text box for the username
element = browser.find_element_by_css_selector("input.email-input")

# Input the provided username
element.send_keys(MY_SCREEN_NAME)

# Input the provided password
browser.find_element_by_css_selector(".LoginForm-password > input").send_keys(MY_PASSWORD)

# Submit the form
element.submit()

WebDriverWait(browser, 15)
if "error" in browser.current_url:
    TEST_1 = False
    print "TEST 1: FAIL"
    exit(1)
else:
    TEST_1 = True

# TEST 2. Test to see if user can enter tweet.

print "\nTEST 2:"
# Find the tweet box
element = browser.find_element_by_id('tweet-box-home-timeline')

# Enter the tweet into the box
element.send_keys(raw_input("\nPlease enter a tweet: "))

# TEST 3. Test to see if user can delete tweet.

# TODO you need to find the tweet id of the new tweet then find the class for the delete button to be able to delete

TEST_3 = False

# TEST 4.

print "\n\n\nTEST 4:"

# Initial tweet count
init_tweets = browser.find_element_by_css_selector("[class='ProfileCardStats-statValue']").text

# Click the tweet button
browser.find_element_by_css_selector("button.tweet-action").click()

# Refresh page
time.sleep(3)
browser.refresh()

# Final tweet count
tweets = browser.find_element_by_css_selector("[class='ProfileCardStats-statValue']").text

if int(init_tweets) + 1 == int(tweets):
    TEST_2 = True
    TEST_4 = True
else:
    TEST_2 = False
    TEST_4 = False
#
# print tweets.text

# TEST 5. Test to see if the user can search.

print "\nTEST 5:"

# Wait for page to reload
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='search-input']")))

# Find the search box
element = browser.find_element_by_css_selector("[class='search-input']")

# Enter the user text into the search box
element.send_keys(raw_input("\nPlease enter a search term: "))

# Send the key return command
element.send_keys(Keys.RETURN)

# Wait for the page to load
# May need to increment time to account for page load times
try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    "[class='SearchNavigation-titleText']")))
    TEST_5 = True
except TimeoutException:
    TEST_5 = False

print "Test Results: \n"
print "TEST 1: \t" + str(TEST_1)
print "\nTEST 2: \t" + str(TEST_2)
print "\nTEST 3: \t" + str(TEST_3)
print "\nTEST 4: \t" + str(TEST_4)
print "\nTEST 5: \t" + str(TEST_5)
