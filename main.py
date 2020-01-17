from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput import keyboard
import requests
import time
from selenium.webdriver.chrome.options import Options


class facebook:
    def __init__(self):
        pass

    def post(self, user, pa, groupList, chromePath, post):
        url = 'https://www.facebook.com/'
        grouplist =  groupList
        r = requests.get(url)
        r.cookies
        username = user
        password = pa
        chromePath = chromePath
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        wd = webdriver.Chrome(chromePath, chrome_options=chrome_options)
        wd.get("https://www.facebook.com/login")
        grouppost = post
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("login").click()
        with open(grouplist) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                linkName = line.strip()
                wd.get('https://www.facebook.com/' + linkName)
                try:
                    wd.find_element_by_xpath("(//a[@class='_4-h7 _5qtn fbReactComposerAttachmentSelector_STATUS'])").click()
                    wd.find_element_by_name('xhpc_message_text').send_keys(grouppost)
                    wd.find_element_by_xpath("(//button[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft'])").click()
                except:
                    pass
                time.sleep(1)
                line = fp.readline()
                cnt += 1

if __name__ == '__main__':
    username = "" #include your id in quotation marks
    password = "" #include the passwords in quotation marks
    grouppost = "" #here, type what you want to say.
    chromePath = "" #download chromeDriver and indicate its path here
    groupList = "" #where is the group text file?
    facebook.post(username, password, groupList, chromePath, grouppost)