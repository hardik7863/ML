"""
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
WebScraping often involves making numereous network requests to
fetch web pages. These tasks are I/o-bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly 
improve the performance by allowing multiple web pages to be fetch concurrently


"""
"""
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

"""

import threading
import requests
from bs4 import BeautifulSoup

urls=[
"https://python.langchain.com/v0.2/docs/introduction/",

"https://python.langchain.com/v0.2/docs/concepts/"

,"https://python.langchain.com/v0.2/docs/tutorials/"
]