from  selenium.webdriver.support.ui import WebDriverWait
def find_element(driver,locator,timeout=10):
    """
    方法名：查找元素
    driver：浏览器的句柄/把柄
    locator：元素定位方式，格式("id",""username)
    timeout：超时间，默认10s
    :return
        -找到元素：返回元素
        -没有找到元素：直接报错
        return WebDriverWait(driver,timeout).until(lambda s:s.find_element(locator))
    """
    return WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator))

def assert_element_exist(driver,locator,timeout=10):
    """
        方法名：查找元素是否存在
        driver：浏览器的句柄/把柄
        locator：元素定位方式，格式("id",""username)
        timeout：超时间，默认10s
        :return
            -找到元素：true
            -没有找到元素：false
            return WebDriverWait(driver,timeout).until(lambda s:s.find_element(locator))
        """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))