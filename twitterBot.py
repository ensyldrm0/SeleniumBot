from lib2to3.pgen2 import driver
from twitterBotInfo import username , password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self , username, password):
        """ self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs" , {"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver",chrome_options=self.browserProfile)
        self.browser.maximize_window()
        self.browser.implicitly_wait(20) """
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(40)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
        
        frame_id = self.browser.find_element(by = By.ID, value = "searchModalIframe")
        self.browser.switch_to.frame(frame_id)  
        
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input").send_keys(self.username)
      
        btnSubmit1 = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        btnSubmit1.click() 

        """  btnSubmit = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[8]/span[2]/span/span")
        btnSubmit.click() """
        

       

        
        

twitter=Twitter("aa","bb")
twitter.signIn()