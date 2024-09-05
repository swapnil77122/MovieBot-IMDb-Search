from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# Open the IMDB signin page
driver.get("https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS9jaGFydC90b3AvP3JlZl89bG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")

# Wait for the email input field to be present with a timeout of 30 seconds
wait = WebDriverWait(driver, 30)
email_input = wait.until(EC.presence_of_element_located((By.ID, 'ap_email')))
password_input = wait.until(EC.presence_of_element_located((By.ID, 'ap_password')))

# Enter the login credentials
email_input.send_keys("enter your email")
password_input.send_keys("password")

# Click the sign in button
driver.find_element_by_id('signInSubmit').click()

# Wait for the login to complete
time.sleep(5)

# Open the IMDB homepage
driver.get("https://www.imdb.com/")

# Wait for the search input field to be present with a timeout of 30 seconds
search_input = wait.until(EC.presence_of_element_located((By.ID, 'suggestion-search')))

# Enter the movie title
search_input.send_keys("The Dark Knight")
search_input.submit()

time.sleep(5)
# Go back to the previous page
driver.execute_script("window.history.go(-1)")

time.sleep(10)
# Enter the next movie title
search_input = wait.until(EC.presence_of_element_located((By.ID, 'suggestion-search')))
search_input.send_keys("The Godfather")
search_input.submit()
time.sleep(5)

# Close the browser
driver.quit()