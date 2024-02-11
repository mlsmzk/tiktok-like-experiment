from page_objects.PageTiktok import PageTiktok
import time

def test_like_hashtag():
    # login with your active tiktok account
    scenario_num = 1 #change this number here for different scenarios!
    username = "Sec02Gr2Sc1Activ_JL" #replace JL with your initial
    page = PageTiktok(scenario_num,username)
    page.fetch_tiktok()
    time.sleep(60)
    page.iterate_through_batches_like_by_hashtag()
    #page.chromebrowser.delete_all_cookies()
    time.sleep(10)


