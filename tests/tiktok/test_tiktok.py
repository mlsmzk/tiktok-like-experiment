from page_objects.PageTiktok import PageTiktok

class TiktokAudit(PageTiktok):
    def test_like(self):
        self.fetch_tiktok()
        self.update_batch()

    



