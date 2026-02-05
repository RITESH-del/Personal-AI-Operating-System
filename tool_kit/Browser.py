from playwright.sync_api import sync_playwright
from .tools import Tool

class BrowserTool:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open_url(self, url):
        self.page.goto(url)
        return "Opened " + url

    def search_google(self, query):
        self.page.goto("https://www.google.com")
        self.page.fill("textarea[name='q']", query)
        self.page.press("textarea[name='q']", "Enter")
        return f"Searched {query}"

    def get_text(self):
        return self.page.inner_text("body")

    def close(self):
        self.browser.close()
        self.playwright.stop()

BrowserTool = BrowserTool() 

Tool(
    name="open_url",
    description="Opens a URL in the browser.",
    args={"url": "string"},
    func=BrowserTool.open_url)

Tool(
    name="search_google",
    description="Searches a query on Google.",
    args={"query": "string"},
    func=BrowserTool.search_google)

Tool(
    name="get_text",    
    description="Gets the text content of the current page.",
    args={},
    func=BrowserTool.get_text
)

Tool(
    name="close_browser",
    description="Closes the browser instance.",
    args={},
    func=BrowserTool.close
)