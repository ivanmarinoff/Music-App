from django.test import TestCase
from playwright.sync_api import Playwright, sync_playwright, expect

class MusicAppTestCase(TestCase):
    def test_create_album(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://music-app-n6cm.onrender.com/")
            page.get_by_role("link", name="Home").click()
            expect(page.get_by_role("link", name="Home")).to_be_visible()
            expect(page.get_by_role("link", name="Create Album")).to_be_visible()
            expect(page.get_by_role("link", name="Profile")).to_be_visible()

            page.get_by_role("link", name="Create Album").click()
            page.goto("https://music-app-n6cm.onrender.com/album/add")
            
            page.get_by_text("Add Album")
            page.get_by_label("Album name:")
            page.get_by_label("Genre:")
            page.get_by_label("Artist:")
            page.get_by_label("Description:")
            page.get_by_label("Image URL:")
            page.get_by_label("Price:")
            page.get_by_role("button", name="Add New Album")
            expect(page.get_by_role("button", name="Add New Album")).to_be_visible()

            page.get_by_role("link", name="Profile").click()
            page.goto("https://music-app-n6cm.onrender.com/profile/details/")
            expect(page.get_by_role("link", name="Delete")).to_be_visible()

            page.get_by_role("link", name="Delete").click()
            page.goto("https://music-app-n6cm.onrender.com/profile/delete/")
            page.get_by_role("button", name="Delete")

            # ---------------------
            context.close()
            browser.close()