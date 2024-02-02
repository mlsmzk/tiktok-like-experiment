from page_objects.PageTiktok import PageTiktok

class TiktokAudit(PageTiktok):
    def test_like(self):
        self.fetch_tiktok()
        self.like_posts(1)
        self.like_posts(2)

    



