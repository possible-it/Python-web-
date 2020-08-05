from selenium import webdriver
from time import sleep
import os
import pyautogui as pg
import shutil

driver = webdriver.  # 创建一个driver对象
driver.maximize_window()    # 最大化浏览器窗口
url = 'https://www.toutiao.com/'  # 要访问的网址
driver.get(url)   # 连接要访问的网址
driver.find_elements_by_xpath('//*[@id="rightModule"]/div[2]/div/div/ul/li[1]')[0].click()  # 利用xpath语法定位并点击QQ小图标
sleep(3)  # 等待三秒钟
driver.switch_to.frame("ptlogin_iframe")  # 跳转到iframe框架
sleep(3)
# 登录方式1.未登录QQ时（容易出验证码）
driver.find_elements_by_xpath('//*[@id="switcher_plogin"]')[0].click()   # 点击账号密码登录
driver.find_elements_by_xpath('//*[@id="u"]')[0].send_keys('账号')   # 输入QQ账号
driver.find_elements_by_xpath('//*[@id="p"]')[0].send_keys('密码')   # 输入密码
driver.find_elements_by_xpath('//*[@id="login_button"]')[0].click()     # 点击登录
# 登录方式2.登录QQ后快速登录
driver.find_elements_by_xpath('//*[@id="qlogin_list"]/a[1]')[0].click()

driver.switch_to.window(driver.window_handles[0])
sleep(3)
# url = "https://sso.toutiao.com/"
# driver.get(url)
# driver.find_elements_by_xpath('//*[@id="user-mobile"]')[0].send_keys('15890507275')
# driver.find_elements_by_xpath('//*[@id="mobile-code-get"]')[0].click()
# sleep(40)
# driver.find_elements_by_xpath('//*[@id="login-button"]')[0].click()
# sleep(5)
driver.find_elements_by_xpath('//li[@class="new-article"]/a')[0].click()
driver.switch_to.window(driver.window_handles[1])
sleep(5)
driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[1]/div[2]/div[1]/div/div[3]')[0].click()
sleep(5)
driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[2]/div/div[1]/div[2]/div')[0].click()
sleep(3)
path = 'E:/cosplay/'
img_dir = os.listdir(path)
for imgs in img_dir:
    paths = path+imgs
    img_list = os.listdir(path+imgs)
    print(paths)
    try:
        path1 = paths + '/' + img_list[0]
    except:
        shutil.rmtree(paths)
        continue
    driver.find_elements_by_xpath('//div[@class="btn-upload-handle upload-handler"]/input')[0].send_keys(path1)
    for img in img_list[1:]:
        image = paths + '/'+img
        sleep(2)
        driver.find_elements_by_xpath('//ul[@class="image-list min-scroll has-images"]//input[@type="file"]')[0].send_keys(image)
        sleep(3)
    driver.find_elements_by_xpath('//div[@class="footer"]/div[@class="confirm-btns"]/button[2]')[0].click()
    sleep(2)
    driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[2]/div/div[1]/div[1]/div/div/textarea')[0].send_keys(imgs)
    sleep(2)
    # pg.moveTo(1360, 255)
    # pg.dragTo(1360, 695)
    # pg.click(455, 623)
    # sleep(3)
    driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[2]/div/div[3]/div/button[3]')[0].click()
    sleep(3)
    driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/ul/li[1]/ul/li[2]/a')[0].click()
    sleep(5)
    driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[1]/div[2]/div[1]/div/div[3]')[0].click()
    sleep(5)
    driver.find_elements_by_xpath('//*[@id="graphic"]/div/div[2]/div/div[1]/div[2]/div')[0].click()
    sleep(3)
    shutil.move(paths, 'E:/cosplay1/')

