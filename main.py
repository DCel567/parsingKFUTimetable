import selenium.webdriver
import selenium.webdriver.common.keys as keys
from bs4 import BeautifulSoup
import time


if __name__ == "__main__":
	driver = selenium.webdriver.Firefox()
	driver.get("https://kpfu.ru/studentu/ucheba/raspisanie")
	input_field = driver.find_element_by_id("p_group_name")
	input_field.send_keys("09-821")
	input_field.send_keys(keys.Keys.ENTER)

	#  got into timetable
	time.sleep(2)

	HTMLPage = driver.page_source
	#  print(HTMLPage)

	soup = BeautifulSoup(HTMLPage, 'html5lib')
	table = soup.findChildren('table')
	myTable = table[0]

	rows = myTable.findChildren(['th', 'tr'])
	for row in rows:
		cells = row.findChildren('td')
		for cell in cells:
			value = cell.text
			print(value)
			print()


