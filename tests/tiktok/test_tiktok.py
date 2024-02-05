from page_objects.PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    def test_like(self):
        self.fetch_tiktok()
        self.iterate_through_batches()
        time.sleep(20)

    



