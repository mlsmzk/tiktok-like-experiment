from page_objects.PageTiktok import PageTiktok
import time

def test_like_hashtag():
    # login with your active tiktok account
    scenario_num_1 = 1 #change this number here for different scenarios!
    username_1 = "Sec02Gr2Sc1Activ_JL" #replace JL with your initial
    page1 = PageTiktok(scenario_num_1,username_1)
    page1.fetch_tiktok()
    time.sleep(60)
    page1.iterate_through_batches_like_by_hashtag()
    #page1.chromebrowser.delete_all_cookies()
    time.sleep(10)


