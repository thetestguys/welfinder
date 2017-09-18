from selenium import webdriver
import sys

# Arguments: welfinder.py <chromeDriverPath <url> <onlyDisplayed>
# chromeDriverPath = path to Chrome driver executable
# url = URL to be checked
# onlyDisplayed = either TRUE/FALSE/ALL

chromeDriverPath = sys.argv[1]
url = sys.argv[2]
onlyDisplayed = sys.argv[3].upper()
driver = webdriver.Chrome(chromeDriverPath)
driver.get(url)
elements = driver.find_elements_by_xpath('//*')
for element in elements:
    if (element.tag_name is None) or (element.get_attribute("id") is None) or (element.get_attribute("class") is None):
        continue
    else:
        attributes = "Tag:" + element.tag_name + " ID:" + \
            element.get_attribute("id") + " Class:" + \
            element.get_attribute("class")
    if onlyDisplayed == 'TRUE':
        if element.is_displayed():
            print("Element displayed on screen " + attributes)
    elif onlyDisplayed == 'FALSE':
        if not element.is_displayed():
            print("Element not displayed on screen " + attributes)
    else:
        print("Element " + attributes)
driver.quit()
