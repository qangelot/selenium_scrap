from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = MY CHROME DRIVER PATH
TARGET_ACCOUNT = "nvidiaai"
USERNAME = MY INSTAGRAM
PASSWORD = MY PASSWORD


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        # scroll inside the popup div : find the new iframe which contains the name of followers, 
        # then make a for loop for it until it reaches to the end of page
        for i in range(20):
            # 20 here is arbitrary, possible to use the total of followers / nb of followers displayed on screen
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # if the account is already followed it will display an unfollow pop up,
                # click on the Cancel button to dismiss the popup and continue to add followers
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
