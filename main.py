import selenium.webdriver
import selenium.webdriver.common.keys as keys
from bs4 import BeautifulSoup
import time


def find_timetable_by_day(day, lines) -> list:
	timetable = []
	for row in lines:
		cellNumber = 0
		cells = row.findChildren('td')
		for cell in cells:
			value = cell.text
			if (cellNumber == day):
				timetable.append(value)
			cellNumber += 1
	return timetable


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
	#  print(len(table))
	try:
		myTable = table[len(table)-1]
		rows = myTable.findChildren(['th', 'tr'])

		#  enter day you want to look at
		timetable = find_timetable_by_day(2, rows)

		times = ['    ', '8:30-10:00', '10:10-11:40', '11:50-13:20', '14:00-15:30', '15:40-17:10', '17:50-19:20']
		for i in range(7):
			print(times[i], ' ', timetable[i])
	except IndexError:
		print("Something wrong with tables on the html page, please try again")
