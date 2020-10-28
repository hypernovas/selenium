import time
 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://developer.amazon.com/alexa/console/ask/test/amzn1.ask.skill.8f6514b4-b42b-424f-89e4-6caca46508ca/development/en_US') # You have to replace the url with your own skills' testing page url

browser.find_element_by_id("ap_email").send_keys("YOUR ACCOUNT NAME")
browser.find_element_by_id("ap_password").send_keys("YOUR PASSWORD")
browser.find_element_by_id("signInSubmit").click()

# Wait for 5 seconds
time.sleep(5)
browser.find_element_by_css_selector('input.askt-utterance__input').send_keys("Alexa, enable lab rule")
time.sleep(1)
browser.find_element_by_css_selector("input.askt-utterance__input").send_keys(Keys.RETURN)
time.sleep(15)

for xx in browser.find_elements_by_css_selector("p.askt-dialog__message"):
	print(xx.text)

