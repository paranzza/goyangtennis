gitfrom selenium import webdriver

import pyautogui

import time

driver = webdriver.Chrome()

url = "https://goyangtennis.or.kr/bbs/board.php?bo_table=tennis_reservation"
driver.get(url)

time.sleep(1.5)

pyautogui.moveTo(891,278)
pyautogui.click()

time.sleep(1)

xpath="//input[@name='mb_id']"
driver.find_element_by_xpath(xpath).send_keys('terin1')

xpath="//input[@name='mb_password']"
driver.find_element_by_xpath(xpath).send_keys('1111aa@@')

xpath="//button[@class='btn-e btn-e-red']"
driver.find_element_by_xpath(xpath).click()

#1번째
xpath="//a[@title='토당시립코트 예약하기']"
driver.find_element_by_xpath(xpath).click()

#코트번호4번=31, 5번=32
xpath="//a[@data-rm-ix='31']"
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

xpath="//i[@class='fa fa-chevron-right']"
driver.find_element_by_xpath(xpath).click()

xpath="//a[@data-date='2022-04-09']"
driver.find_element_by_xpath(xpath).click()

time.sleep(1)

xpath="//a[@data-time='16:00']"
driver.find_element_by_xpath(xpath).click()

xpath="//button[@class='btn btn-success']"
driver.find_element_by_xpath(xpath).click()

xpath="//input[@id='bk_payment_card']"
driver.find_element_by_xpath(xpath).click()

xpath="//input[@id='agree1']"
driver.find_element_by_xpath(xpath).click()

xpath="//input[@id='agree2']"
driver.find_element_by_xpath(xpath).click()

xpath="//button[@class='btn btn-success']"
driver.find_element_by_xpath(xpath).click()

time.sleep(1.5)

#전체약관동의
pyautogui.moveTo(418,380)
pyautogui.click()

#삼성카드선택
pyautogui.moveTo(460,440)
pyautogui.click()

#카드선택완료
pyautogui.moveTo(548,821)
pyautogui.click()

time.sleep(1)

#앱카드결제선택
pyautogui.moveTo(633,571)
pyautogui.click()

time.sleep(10)

#결제내용확인
pyautogui.moveTo(430,600)
pyautogui.click()

#결제완료
pyautogui.moveTo(465,801)
pyautogui.click()

xpath="//button[@class='btn btn-lg btn-success']"
driver.find_element_by_xpath(xpath).click()
