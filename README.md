# IMDb Movie Search Automation

This project automates the process of logging into IMDb and searching for specific movies using Selenium WebDriver. It demonstrates how to automate a browser session for IMDb login and movie search functionality, making it easy to find information about movies without manual interaction.

## Features

- Automates login to IMDb using provided credentials.
- Searches for specific movie titles on IMDb.
- Demonstrates browser automation using Selenium WebDriver.
- Automatically navigates back to search for multiple movies.

## Prerequisites

Before running this project, you need the following:

1. **Python**: Make sure you have Python 3.6 or higher installed. You can download it from [here](https://www.python.org/downloads/).
2. **Google Chrome**: The script uses Chrome as the browser. Download Chrome if you haven't already from [here](https://www.google.com/chrome/).
3. **ChromeDriver**: Ensure that you have the correct version of ChromeDriver that matches your version of Google Chrome. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Installation

1. Clone the repository or download the code.
2. Install the required Python packages:

```bash
pip install selenium
```

3. Make sure the `chromedriver.exe` is in your project directory or update the path in the script if it's stored elsewhere.

4. Replace the placeholder login credentials with your IMDb credentials in the script:

```python
email_input.send_keys("enter your email")
password_input.send_keys("password")
```

## Usage

1. **Run the Script**: Open a terminal/command prompt and navigate to the directory where the script is located. Then run the script:

```bash
python app.py
```

2. **Login to IMDb**: The script will automatically open IMDb's sign-in page and input the provided login credentials.

3. **Search for Movies**: The script will search for "The Dark Knight," navigate back, and then search for "The Godfather." You can modify the movie titles as needed in the script.

4. **Close the Browser**: After the searches, the browser will automatically close.

## Script Breakdown

1. **Import Statements**: The script imports necessary libraries for Selenium WebDriver, time handling, and waiting for elements.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
```

2. **Driver Setup**: The ChromeDriver path is defined, and the IMDb sign-in page is opened.

```python
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.imdb.com/ap/signin?...")
```

3. **Login Automation**: The script waits for the email and password input fields to appear, inputs the provided credentials, and clicks the login button.

```python
email_input.send_keys("enter your email")
password_input.send_keys("password")
driver.find_element_by_id('signInSubmit').click()
```

4. **Movie Search**: After logging in, the script navigates to IMDb's homepage, waits for the search input field, and searches for movie titles.

```python
search_input.send_keys("The Dark Knight")
search_input.submit()
```

5. **Back Navigation**: The script navigates back to search for another movie title.

```python
driver.execute_script("window.history.go(-1)")
```

6. **Close Browser**: After all tasks, the browser is closed automatically.

```python
driver.quit()
```

## Customization

- **Change Movies**: You can modify the movie titles to search for any movies you like by replacing the titles in the `search_input.send_keys()` lines.
- **Modify Login Details**: Replace the email and password in the script with your IMDb login credentials.

## Project Structure

```
imdb-movie-search/
│
├── imdb_movie_search.py   # Main Python script for automation
├── chromedriver.exe       # ChromeDriver executable
└── README.md              # This README file
```

## Notes

- Ensure you have a valid IMDb account for the login process.
- Make sure that the ChromeDriver version matches your installed version of Google Chrome. You can check the version of your Chrome by visiting `chrome://settings/help`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to [Selenium WebDriver](https://www.selenium.dev/) for providing a powerful tool for browser automation.
