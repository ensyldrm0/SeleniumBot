from instagramBotInfo import email,password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self,email,password):
      self.browser = webdriver.Chrome()
      self.email = email
      self.password = password
    
    def singIn(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(3)
        emailInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
    def getFollowers(self):
        self.browser.get("https://www.instagram.com/?hl=tr/{self.username}")
        
        followersLink = self.browser.find_element(By.XPATH , "//*[@id='mount_0_0_Ye']/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a/div")
        followersLink.click()





instagram = Instagram("ensyldrm0","wanrltw123")
instagram.singIn()    
instagram.getFollowers()    


