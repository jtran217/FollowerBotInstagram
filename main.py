# IMPORT LIST
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep


# CONSTANT VARIABLES
USER = "USER"
PASS = "PASS"
ACCOUNT_FOLLOW = "FOLLOWER TO FOLLOW"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.instagram_followers = []

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        user_name_field = self.driver.find_element_by_name("username")
        user_name_field.send_keys(USER)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(PASS)
        sleep(1)
        password_field.send_keys(Keys.ENTER)
        sleep(2)
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        sleep(3)
        not_now_notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_notification.click()
    def find_followers(self):
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(ACCOUNT_FOLLOW)
        sleep(2)
        first_in_list = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        first_in_list.click()
        sleep(2)
        follower_click = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_click.click()
        sleep(2)
        scroll_body = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        #SCROLL THROUGH FOLLOWERS OF INSTAGRAM PAGE
        more_scroll = True
        while more_scroll:
            len_list = len(self.driver.find_elements_by_css_selector(".PZuss li"))
            previous_len = len_list
            print(f"The len list is {len_list}")
            sleep(3)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_body)
            sleep(3)
            len_list = len(self.driver.find_elements_by_css_selector(".PZuss li"))
            print(f"The new list len is {len_list}")

            if len_list != previous_len:
                continue
            else:
                more_scroll = False
        self.instagram_followers =(self.driver.find_elements_by_css_selector(".PZuss li button"))


    def follow(self):
        for followers in self.instagram_followers:
            try:
                sleep(5)
                followers.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



instbot = InstaFollower()
instbot.login()
instbot.find_followers()
instbot.follow()
