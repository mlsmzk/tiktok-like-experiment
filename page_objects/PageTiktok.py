from seleniumbase import Driver
#from selenium import webdriver
from selenium.webdriver.common.by import By # contains operators for the type of search we want to do
import time
from seleniumbase import BaseCase
from random import randint
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

"""
1 batch = the number of posts available on page before scrolling down and loading more.
"""

class PageTiktok(BaseCase): #inherit BaseCase
    predefined_hashtag_list = ["viral","foryou"]
    chromebrowser = Driver(uc=True)
    actions = ActionChains(chromebrowser)
    current_batch = []
    len_all_posts = None
    all_videos_on_page = []

    def info_videos(self,videoList):
        '''
        when given a list of video divs, return a summary of each video
        [{web_element: video, index:1, hashtag:[], num_comment = {}}, ...]
        '''
        summary = []
        for index, video in enumerate(videoList):
            summary.append({"index":index, "video":video, "hashtag":self.get_hashtag(video)})

        return summary

    def get_hashtag(self,video):
        hashtag_list = video.find_elements(By.XPATH, './/*[@class="ejg0rhn6 css-g8ml1x-StyledLink-StyledCommonLink er1vbsz0"]')
        if hashtag_list:
            return [hashtag.get_attribute('href').split('/')[-1] for hashtag in hashtag_list]
        else:
            return []
        

    def fetch_tiktok(self):
        """
        open tiktok, provide time for manual log in, fill in the current_batch with the posts preloaded on screen
        """
        self.chromebrowser.uc_open_with_reconnect('https://www.tiktok.com/en/',reconnect_time=5) #link to login page
        time.sleep(20)

        #initialize values
        try:
            self.current_batch = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-14bp9b0-DivItemContainer etvrc4k0"]')
            self.all_videos_on_page = self.current_batch
            self.len_all_posts = len(self.all_videos_on_page)
        except StaleElementReferenceException:
            self.fetch_tiktok()
        
    def login(self):
        """
        not used. Manually log in instead, have to close the 2 popups on the bottom right
        """
        # click "use phone/number/email" on login page
        use_email = self.chromebrowser.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]")
        use_email.click()
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
 
    def like_video(self,video):
        '''
        likes a video passed in parameter
        '''
        try:
            like_button = video.find_elements(By.XPATH, ".//*[@class='css-1ok4pbl-ButtonActionItem e1hk3hf90']")[0]
            like_button.click()
            print(f"clicked button {like_button.get_attribute('aria-label')}")
            time.sleep(1)
        except ElementClickInterceptedException:
            print(f"elementclickexception")
            pass
    
    def like_videos_with_hashtag(self,current_batch,predefined_hashtag_list):
        """
        in each video in current_batch, like it iff it contains a hashtag in the predefined hashtag list
        """
        current_batch_info = self.info_videos(current_batch)
        for video_info in current_batch_info:
            if video_info["hashtag"]:
                if set(video_info["hashtag"]) & set(predefined_hashtag_list):
                    self.like_video(video_info["video"])
    
    def update_batch(self):
        """
        updates batch by scrolling to the bottom 
        """
        current_batch_exists = False

        self.actions.move_to_element(self.all_videos_on_page[-1]).perform()
        time.sleep(5)
        old_batch = self.current_batch
        old_all_videos = self.all_videos_on_page
        print(f"***old batch:{self.info_videos(old_batch)}\n")
        print(f"\n***length of old batch: {len(old_batch)}\n")

        #print(f"\n***old all videos on page: {self.info_videos(old_all_videos)}")
        print(f"\n***length of old all videos on page:{len(old_all_videos)}")

        self.current_batch = set(old_all_videos) ^ set(self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-14bp9b0-DivItemContainer etvrc4k0"]'))
        print(f"Is there no overlap between old batch and new batch?:{self.validate_no_overlapping_post(old_batch, self.current_batch)}")
        
        self.all_videos_on_page = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-14bp9b0-DivItemContainer etvrc4k0"]')
        #print(f"\n***new all videos on page: {self.info_videos(self.all_videos_on_page)}")
        print(f"\n***length of new all videos on page:{len(self.all_videos_on_page)}")

        if self.current_batch: #if new videos were loaded
            print(f"\n***new batch: {self.info_videos(self.current_batch)}")
            print(f"\n***length of new batch: {len(self.current_batch)}\n")
            current_batch_exists = True
        else:
            print("\n!!!!no new posts were added!!!!\n")
        
        return current_batch_exists


    def validate_no_overlapping_post(self, oldbatch, newbatch):
        ''''
        validates that the the oldbatch and the new batch (videolists) does not overlap
        '''
        return (not (set(oldbatch) & set(newbatch)))
    

    def iterate_through_batches(self):
        """
        like posts in current batch after updating, then move on to the next batch
        """
        num_batches = 5
        while self.update_batch() and num_batches > 0: #if new batch appeared on foryou page
            print(f"\n****ENTERING BATCH{6-num_batches}\n")
            num_batches -= 1
            self.like_videos_with_hashtag(self.current_batch,self.predefined_hashtag_list)
            time.sleep(10)
        
    

  
    




        
