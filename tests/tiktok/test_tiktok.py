from page_objects.PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    def test_like_hashtag(self):
        self.fetch_tiktok()
        self.iterate_through_batches_like_by_hashtag()
        time.sleep(10)

    def test_like_random(self):
        self.fetch_tiktok()
        self.iterate_through_batches_like_random(filename="random_like_data.csv")
        time.sleep(10)


