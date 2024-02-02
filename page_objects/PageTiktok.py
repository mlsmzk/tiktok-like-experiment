from seleniumbase import Driver
#from selenium import webdriver
from selenium.webdriver.common.by import By # contains operators for the type of search we want to do
import time
from seleniumbase import BaseCase
from random import randint
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

class PageTiktok(BaseCase): #inherit BaseCase
    chromebrowser = Driver(uc=True)
    
    def fetch_tiktok(self):
        self.chromebrowser.uc_open_with_reconnect('https://www.tiktok.com/en/',reconnect_time=5) #link to login page
        time.sleep(25)
        
    def login(self):
        time.sleep(1)

        # click "use phone/number/email" on login page
        use_email = self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]")
        use_email.click()

        time.sleep(4)

        # click "login with email or username"
        self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div[2]/form/div[1]/a").click()

        time.sleep(1)

        input_username = self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div[2]/form/div[1]/input")
        input_password = self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div[2]/form/div[2]/div/input")

        input_username.send_keys(self.email)
        input_password.send_keys(self.password)

        time.sleep(3)

        login = self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div[2]/form/button")
        login.click()
    
    def like_posts(self, trial):
        print(f"ENTERING TRIAL {trial}")
        retry = 0
        while retry <= 2:
            retry += 1
            self.helper_like(retry)
    
    def helper_like(self,retry):
            print(f"#{retry} retry")
            self.chromebrowser.uc_open_with_reconnect('https://www.tiktok.com/en/',reconnect_time=5)
            try:
                button_list = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-1ok4pbl-ButtonActionItem e1hk3hf90"]')
                print(f"{retry}:# like buttons",len(button_list)//4)
                print("was able to get attribute of these like buttons:\n")
                for i, post_button in enumerate(button_list):
                    if i % 4 == 0: #if like button
                        print(post_button.get_attribute("aria-label"))
                        time.sleep(0.5)

                for i, post_button in enumerate(button_list):
                    if i % 4 == 0:
                        try:
                            post_button.click()
                            print(f"clicked button #{i//4}")
                            time.sleep(0.5)
                        except ElementClickInterceptedException:
                            print(f"elementclickexception at like #{i//4}")
                            pass
                time.sleep(6)

            except StaleElementReferenceException:
                print("stale element:reload") 




        
