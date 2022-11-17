import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Prerequisite settings for the Web Driver
options = Options()
options.add_experimental_option("detach", True)

# Initializes the Web Driver to use Chrome with the set options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Opens the webpage and maximizes the window
driver.get("https://neuralnine.com/")
driver.maximize_window()

# Stores all elements that have an anchor tag with a link in links
links = driver.find_elements("xpath", "//a[@href]")

# Goes through the links on the page and clicks on the link with the span named "Books"
for link in links:
  if "Books" in link.get_attribute("innerHTML"):
    link.click()
    break

# Looks for the links on the "Books" page and stores in bookLinks
bookLinks = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

# Executes Javascript for scrolling to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Clicks on the matching link once found on screen
bookLinks[0].click()

# Switches to the 2nd tab
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)