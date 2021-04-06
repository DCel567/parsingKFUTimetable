import selenium.webdriver
import selenium.webdriver.common.keys as keys
import bs4
import time


if __name__ == "__main__":
	driver = selenium.webdriver.Firefox()
	driver.get("https://kpfu.ru/studentu/ucheba/raspisanie")
	input_field = driver.find_element_by_id("p_group_name")
	input_field.send_keys("09-821")
	input_field.send_keys(keys.Keys.ENTER)

	#  got into timetable

