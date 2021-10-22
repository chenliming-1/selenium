from  seleniumtools import find_element
from selenium import webdriver
#1、打开网址
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://sso.test.klxuexi.net/login')
#2、把元素的定位方式都收集起来再定位
username_input = ('id','username')
password_input=('id','password')
valCode_input=('id','validateCode')
find_element(driver,username_input).send_keys("clming_1")
find_element(driver,password_input).send_keys("clming@123")
find_element(driver,valCode_input).send_keys("1278")

