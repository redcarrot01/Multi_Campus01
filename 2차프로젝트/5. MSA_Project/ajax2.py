import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.samsung.com/sec/support/downloadcenter/#")

time.sleep(1)
step1 = driver.find_element_by_xpath('//*[@id="moreLow"]/a')
step1.click()
time.sleep(1)
step2 = driver.find_element_by_xpath('//*[@id="1Step"]/div[2]/div[2]/ul/li[4]/ul/li[2]/a')
step2.click()
time.sleep(1)
step3 = driver.find_element_by_xpath('//*[@id="2Step"]/div/div[2]/ul/li[1]/a/div')
step3.click()
time.sleep(1)
for i in range(10):
    step4 = driver.find_element_by_xpath('//*[@id="btnMore"]')
    step4. click()
    time.sleep(2)

step5 = driver.find_element_by_xpath('//*[@id="3Step"]/div[1]/div[2]').find_elements_by_tag_name('span')
time.sleep(2)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
res = soup.find_all(class_='lr-code')
for n in res:
    print(n.get_text())


second1 = driver.find_element_by_xpath('//*[@id="2Step"]/div/div[2]/ul/li[2]/a/div')
second1.click()
time.sleep(1)

for i in range(18):
    second2 = driver.find_element_by_xpath('//*[@id="btnMore"]')
    second2.click()
    time.sleep(1)

second3 = driver.find_element_by_xpath('//*[@id="3Step"]/div[1]/div[2]').find_elements_by_tag_name('span')
time.sleep(1)

html2 = driver.page_source
soup2 = BeautifulSoup(html2, "html.parser")
res2 = soup2.find_all(class_='lr-code')
for n in res2:
    print(n.get_text())


Third1 = driver.find_element_by_xpath('//*[@id="2Step"]/div/div[2]/ul/li[3]/a/div')
Third1.click()
time.sleep(2)

for i in range(31):
    Third2 = driver.find_element_by_xpath('//*[@id="btnMore"]')
    Third2.click()
    time.sleep(1)

Third3 = driver.find_element_by_xpath('//*[@id="3Step"]/div[1]/div[2]').find_elements_by_tag_name('span')
time.sleep(2)

html3 = driver.page_source
soup3 = BeautifulSoup(html3, "html.parser")
res3 = soup3.find_all(class_='lr-code')
for n in res3:
    print(n.get_text())


Fourth1 = driver.find_element_by_xpath('//*[@id="2Step"]/div/div[2]/ul/li[4]/a/div')
Fourth1.click()
time.sleep(1)

for i in range(26):
    Fourth2 = driver.find_element_by_xpath('//*[@id="btnMore"]')
    Fourth2.click()
    time.sleep(1)

Fourth3 = driver.find_element_by_xpath('//*[@id="3Step"]/div[1]/div[2]').find_elements_by_tag_name('span')
time.sleep(2)

html4 = driver.page_source
soup4 = BeautifulSoup(html4, "html.parser")
res4 = soup4.find_all(class_='lr-code')
for n in res4:
    print(n.get_text())

f= open('product_code.txt', 'r')
line_num = 1
line = f.readline()
line = line.replace("- ","")
while line:

    print('%d' ' %s' %(line_num, line))
    line = f.readline()
    line = line.replace("- ", "")
    line_num += 1
f.close()