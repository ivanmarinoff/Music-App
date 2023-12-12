import re
from playwright.sync_api import Page, sync_playwright, expect

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()
def test_homepage_view(page: Page):
    page.goto("https://music-app-n6cm.onrender.com/")
    page.get_by_role("link", name="Home").click()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Create Album")).to_be_visible()
    expect(page.get_by_role("link", name="Profile")).to_be_visible()

def test_create_album(page: Page):
    page.goto("https://music-app-n6cm.onrender.com/")
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

def test_profile_details(page: Page):
    page.goto("https://music-app-n6cm.onrender.com/")
    page.get_by_role("link", name="Profile").click()
    page.goto("https://music-app-n6cm.onrender.com/profile/details/")
    expect(page.get_by_role("link", name="Delete")).to_be_visible()