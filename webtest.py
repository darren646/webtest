import requests
import selenium
session=requests.session()
getinfo=session.get("https://www.baidu.com")
print(getinfo.content)
print(getinfo.text)
print(getinfo.status_code)
#postinfo=requests.post()
pass

#-- coding:UTF-8 -*-
#导入 webdriver
from lxml import etree
from selenium import webdriver
from bs4 import BeautifulSoup
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
#无界面浏览器相关设置
# 创建chrome参数对象
# opt = webdriver.ChromeOptions()
# #把chrome设置成为无界面模式
# opt.set_headless()
# #创建chrome无界面对象
# driver = webdriver.Chrome(
#         options=opt, executable_path='/Users/wxl/Desktop/chromedriver')

#创建chrome有界面对象
driver = webdriver.Chrome()#调用Chrome浏览器创建浏览器对像(指定一下位置)
#driver.implicitly_wait(1000)
time.sleep(2)
#打开浏览器，模拟浏览器请求页面
driver.get('http://www.baidu.com/')
#获取页面的源码信息
html = driver.page_source
print(html)
#soup = BeautifulSoup(html,“html.parser”)
soup = etree.HTML(html)
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
#打印数据内容
print(data)

#打印标题数据
print(driver.title)

#向百度的搜索框输入搜索关键字
driver.find_element_by_id('kw').send_keys('美女')
#百度搜索按钮，click() 是模拟点击
driver.find_element_by_id('su').click()

#获取当前页面的cookies()
cookies = driver.get_cookies()

cookie = ''

for item in cookies:

    cookie += item['name']+item['value']+' ;'

    print(cookie[:-1])

#全选输入框中的内容ctrl+a
print(driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a'))

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

#清空输入框内容
driver.find_element_by_id('kw').clear()
#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('风景')
#模拟回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
#获取当前的url
currentUrl = driver.current_url
print(currentUrl)

#截取网页页面（生成当前的页面快照并保存）
driver.save_screenshot('baidu.png')

#睡眠7秒
time.sleep(7)
# 关闭浏览器
driver.quit()

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()#-- coding:UTF-8 -*-
#导入 webdriver
from lxml import etree
from selenium import webdriver
from bs4 import BeautifulSoup
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
#无界面浏览器相关设置
# 创建chrome参数对象
# opt = webdriver.ChromeOptions()
# #把chrome设置成为无界面模式
#
# opt.headless
# #创建chrome无界面对象
# driver = webdriver.Chrome(
#         options=opt, executable_path='/Users/wxl/Desktop/chromedriver')

#创建chrome有界面对象
driver = webdriver.Chrome()
#driver.implicitly_wait(1000)
time.sleep(2)
#打开浏览器，模拟浏览器请求页面
driver.get('http://www.baidu.com/')
#获取页面的源码信息
html = driver.page_source
print(html)
#soup = BeautifulSoup(html,“html.parser”)
soup = etree.HTML(html)
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
#打印数据内容
print(data)

#打印标题数据
print(driver.title)

#向百度的搜索框输入搜索关键字
driver.find_element_by_id('kw').send_keys('美女')
#百度搜索按钮，click() 是模拟点击
driver.find_element_by_id('su').click()

#获取当前页面的cookies()
cookies = driver.get_cookies()

cookie = ''

for item in cookies:

    cookie += item['name']+item['value']+' ;'

    print(cookie[:-1])

#全选输入框中的内容ctrl+a
print(driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a'))

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

#清空输入框内容
driver.find_element_by_id('kw').clear()
#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('风景')
#模拟回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
#获取当前的url
currentUrl = driver.current_url
print(currentUrl)

#截取网页页面（生成当前的页面快照并保存）
driver.save_screenshot('baidu.png')

#睡眠7秒
time.sleep(7)
# 关闭浏览器
driver.quit()

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()