from unittest import expectedFailure

from Tools.scripts.make_ctype import values
from selenium import webdriver
from time import sleep
d = webdriver.Chrome()
d.get("https://google.com")
d.get("file:///C:/Users/USER/Downloads/tip_calc%20(1)/tip_calc/index.html")
d.find_element(by="id", value="billment").send_keys("100")
d.find_element(by="xpatch", value='//*[@id="serviceQual"]/option[3]').click()
d.find_element(by="id", value="peopleamt").send_keys("2")
actual = d.find_element(by="id", value="calculate").click() = d.find_element(by="id", value="tip").text
expected = "6.00"
assert actual == expected
assert is_visible