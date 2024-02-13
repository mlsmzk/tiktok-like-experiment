from page_objects.PageTiktok import PageTiktok
import time

def test_like_control():
    # login with your control tiktok account
    scenario_num = -1
    username = "Sec02Gr2Sc5Cntrl_JL" #replace JL with your initial
    page = PageTiktok(scenario_num,username)
    page.fetch_tiktok()
    page.iterate_through_batches_like_control()
    time.sleep(10)
    