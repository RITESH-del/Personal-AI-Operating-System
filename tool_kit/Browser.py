# from playwright.sync_api import sync_playwright
# from .tools import Tool
# import time

# class BrowserTool:
#     def __init__(self):
#         self.playwright = None
#         self.browser = None
#         self.page = None

#     def _ensure_browser(self):
#         if not self.playwright:
#             self.playwright = sync_playwright().start()
#             self.browser = self.playwright.chromium.launch(headless=False)
#             self.page = self.browser.new_page()

#     def open_url(self, url):
#         self._ensure_browser()
#         self.page.goto(url)
#         return "Opened " + url

#     def search_google(self, query):
#         self._ensure_browser()
#         self.page.goto("https://www.google.com")
#         self.page.fill("textarea[name='q']", query)
#         self.page.press("textarea[name='q']", "Enter")
#         return f"Searched {query}"

#     def get_text(self):
#         self._ensure_browser()
#         return self.page.inner_text("body")

#     def close(self):
#         if self.browser:
#             self.browser.close()
#             self.browser = None
#         if self.playwright:
#             self.playwright.stop()
#             self.playwright = None
#         return "Browser closed"

# browser_tool = BrowserTool()

# Tool(
#     name="open_url",
#     description="Opens a URL in the browser.",
#     args={"url": "string"},
#     func=browser_tool.open_url)

# Tool(
#     name="search_google",
#     description="Searches a query on Google.",
#     args={"query": "string"},
#     func=browser_tool.search_google)

# Tool(
#     name="get_text",    
#     description="Gets the text content of the current page.",
#     args={},
#     func=browser_tool.get_text
# )

# Tool(
#     name="close_browser",
#     description="Closes the browser instance.",
#     args={},
#     func=browser_tool.close
# )