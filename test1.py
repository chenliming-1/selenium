#导入驱动文件
from selenium import webdriver
import time
#1、打开浏览器
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="chromedriver.exe")
#2、访问网址
driver.get('https://sso.test.klxuexi.net/login')

# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/form/section[4]/div").click()
#3、操作元素（输入内容、点击按钮）
e= driver.find_element_by_id("username").send_keys("clming_1")
e= driver.find_element_by_id("password").send_keys("clming@123")
e= driver.find_element_by_id("validateCode").send_keys("1278")
#4、判断出现页面按钮是否存在 （页面title、url、页面上元素）
#固定等待时间
# time.sleep(3)
# assert  driver.title == "快乐学习 天天向上"
# print("搜索成功")
#隐式等待--网页在10s内加载完成，节约测试时间
# driver.implicitly_wait(10)
# e=driver.find_element_by_xpath("/html/body/footer/span[2]")
# assert  e.text=="Histudy.com All Rights Reserved"
# assert  driver.title == "快乐学习 天天向上"
# print("搜索成功")

#显示等待
e=("xpath","/html/body/footer/span[2]")   #e是一个元组，（定位方式，定位方式的值）
a =WebDriverWait(driver,10).until(lambda s:s.find_element(*e)) #找到就返回元素的对象，找不到就报错
assert  a.text=="Histudy.com All Rights Reserved"
print("搜索成功")