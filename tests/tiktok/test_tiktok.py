from page_objects.PageTiktok import PageTiktok
import time

def test_like_hashtag():
    scenario_num = 1 #change this number here for different scenarios!
    page = PageTiktok(scenario_num)
    page.fetch_tiktok()
    page.iterate_through_batches_like_by_hashtag()
    time.sleep(10)

'''
def test_like_control():
    scenario_num = -1
    page = PageTiktok(scenario_num)
    page.fetch_tiktok()
    self.iterate_through_batches_like_control()
    time.sleep(10)

def test_like_random(self):
    scenario_num = 1 #change this for different scenarios
    page = PageTiktok(scenario_num)
    page.fetch_tiktok()
    self.iterate_through_batches_like_random()
    time.sleep(10)
    self.chromebrowser.close()
 '''
    


