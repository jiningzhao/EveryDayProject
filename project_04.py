'''
开发人员：赵吉宁
脚本功能：selenium自动化登陆
时间：2019-08-07
'''
from selenium import webdriver
from selenium.webdriver.common.by import By                       # 用于制定指定HTML文件中DOM标签元素
from selenium.webdriver.support.ui import WebDriverWait           # 用于等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC  # 用于指定网页加载结束的条件
from selenium.webdriver.common.action_chains import ActionChains
import time
from tqdm import tqdm
import re

driver=webdriver.Chrome()
# driver.implicitly_wait(30)
web=driver.get("https://service-wbs2461.newtamp.cn")

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"login-wrappers")))
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/input").clear()
driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys("18888888888")
driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys("a111111")
driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/div[3]/button").click()

time.sleep(5)
WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME,"_gio_c_modal__close")))
zero_click=driver.find_element_by_xpath("//div[@class='_gio_c_modal__close']")
ActionChains(driver).click(zero_click).perform()


# time.sleep(5)
WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME,"navigation-icon")))
first_click=driver.find_element_by_xpath("//span[@slot='title'][1]")
ActionChains(driver).click(first_click).perform()

# time.sleep(5)
WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME,"el-menu-item")))
second_click=driver.find_element_by_xpath("//li[contains(text(),'员工管理')]")
ActionChains(driver).click(second_click).perform()
#
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"nb-scroll-content")))
time.sleep(5)
add_element=driver.find_element_by_xpath('//*[@id="nb-scroll-content"]/section/div[1]/div[1]/div/div[1]/section/div[1]')
ActionChains(driver).click(add_element).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="pane-0"]/section[1]/form/div[1]/div/div/div[2]/div/input').send_keys("自动化生成员工")
time.sleep(3)
driver.find_element_by_xpath('//div[@class="click-input"]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[contains(text(),"总裁办")]').click()
time.sleep(5)
driver.find_element_by_xpath("//button[@type='button']").click()

