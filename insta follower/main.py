from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = "buzzfeedtasty"  # Change this to an account of your choice
USERNAME = "jayprints"  # Replace with your Instagram username
PASSWORD = "YOUR_PASSWORD"  # Replace with your Instagram password

class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out if necessary
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking the element or button
            cookie_warning[0].click()

        # Enter username and password
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        try:
            save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            save_login_prompt.click()
        except NoSuchElementException:
            pass

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        try:
            notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
            notifications_prompt.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(5)
        # Navigate to the followers page of the similar account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(8.2)

        try:
            # Wait for the modal (followers list) to appear
            modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )

            for i in range(5):
                # Scroll the modal to load more followers
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)
        except Exception as e:
            print(f"Error finding followers: {e}")

    def follow(self):
        # Try to click the follow button for each follower
        try:
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1.1)
                except ElementClickInterceptedException:
                    # Handle if the dialog appears (Unfollow/Cancel)
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
        except Exception as e:
            print(f"Error during follow operation: {e}")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
