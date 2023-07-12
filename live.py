# -*- encoding: utf-8 -*-
'''
@File : reply2.py
@Date : 2023-07-11
@Time : 14:59:25
@Author : lizeyujack@sjtu.edu.cn 
'''
from selenium import webdriver
import time, sys

replies = [
    '看完这个视频,我更加珍惜现在的健康,也更加爱护自己的孩子。',
    '真是太感人了,希望所有的孩子都能健康成长。',
    '我也是一个妈妈,看到孩子生病真的是比什么都难受。',
    '孩子生病真的是太痛苦了,希望孩子们都能健康成长。',
    '祝福所有的孩子都能健康成长,不再生病。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远快乐健康。',
    '生病的孩子真的让人心疼,希望他们早日康复。',
    '看到这个视频,我更加明白了健康的重要性。',
    '孩子的健康是最重要的,希望所有的孩子都能健康成长。',
    '这个视频真的让人感动,希望孩子们都能健康快乐。',
    '孩子们都是天使,希望他们健康成长。',
    '看到孩子们的笑容,真的是太幸福了。',
    '希望所有的孩子都能健康成长,不再受病痛的折磨。',
    '孩子生病真的是太让人心疼了,希望所有的孩子都能健康快乐。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远健康快乐。',
    '健康是最重要的,希望所有的孩子都能健康成长。',
    '生病的孩子真的太让人心疼了,希望他们早日康复。',
    '希望所有的孩子都能永远健康快乐,不再生病。',
    '孩子们都是天使,希望他们健康成长。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远快乐健康。',
    '生病的孩子真的太难受了,希望他们早日康复。',
    '希望所有的孩子都能健康成长,不再被病痛困扰。',
    '孩子们的健康是最重要的,希望他们都能健康成长。',
    '看到孩子们的笑容,真的是太幸福了,希望他们永远快乐健康。',
    '生病的孩子真的让人心疼,希望他们早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的折磨。',
    '孩子们都是天使,希望他们健康快乐。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远健康快乐。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '健康是最重要的,希望所有的孩子都能健康成长,不再生病。',
    '孩子们的笑容真的是太可爱了,希望他们永远健康快乐。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的困扰。',
    '孩子们的健康是最重要的,希望他们都能健康成长。',
    '看到孩子们的笑容,真的是太幸福了,希望他们永远快乐健康。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的折磨。',
    '孩子们都是天使,希望他们健康快乐。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远健康快乐。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的折磨。',
    '孩子们的健康是最重要的,希望他们都能健康成长。',
    '看到孩子们的笑容,真的是太幸福了,希望他们永远快乐健康。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的困扰。',
    '孩子们的健康是最重要的,希望他们都能健康成长。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远健康快乐。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的折磨。',
    '孩子们都是天使,希望他们健康快乐。',
    '看到孩子们的笑容,真的是太幸福了,希望他们永远快乐健康。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。',
    '希望所有的孩子都能健康成长,不再受病痛的困扰。',
    '孩子们的健康是最重要的,希望他们都能健康成长。',
    '看到孩子们的笑容,真的是太感动了,希望他们永远健康快乐。',
    '生病的孩子真的太让人心疼了,希望他们能早日康复。']

# 设置抖音视频的网址
# url = 'https://www.douyin.com/video/xxxxxxxxxxxxx'
# url = 'https://www.douyin.com/video/7251242947981692163'
# url = 'https://www.douyin.com/video/7249344150926118176'
url = 'https://live.douyin.com/293133237723'

# 设置Chrome浏览器的驱动程序路径
# driver_path = 'chromedriver.exe'
# driver_path = "D:\\下载\\chromedriver_win32\\chromedriver.exe"
driver_path = "E:\\Download\\chromedriver_win32\\chromedriver.exe"# 要对应下载

driver_service = webdriver.chrome.service.Service(executable_path=driver_path)
# option = webdriver.ChromeOptions()
# option.add_argument("--user-data-dir=" + f"C:\\Users\\lizeyu\\AppData\\Local\\Google\\Chrome\\User Data\\")
# driver = webdriver.Chrome(chrome_options=option)
print('driver_service')
driver = webdriver.Chrome(executable_path=driver_path)

print('打开浏览器')
# 打开抖音网页
driver.get(url)
print('打开网页')
# 等待网页加载完成
time.sleep(25)
import random

# comment_boxes = driver.find_element_by_css_selector(".richtext-container > .DraftEditor-root")
# comment_boxes = driver.find_element_by_css_selector('.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
comment_boxes = driver.find_element_by_css_selector('.webcast-chatroom___input-container > .webcast-chatroom___textarea')


# for ele in comment_boxes:
#     print(ele.get_attribute('outerHTML'))
for i in range(50):
    random_number_1 = random.uniform(1, 3)
    random_number_2 = random.uniform(2, 5)
    random_number_3 = random.uniform(5, 15)
    # 遍历所有的评论框,并进行回复
    comment_boxes.click()
    time.sleep(random_number_1)
    # idx_ = idx % len(replies)
    reply_content = f"{replies[0]},互动，互动，争取早日财务自由"
    # 输入回复内容
    # comment_boxes_ = driver.find_element_by_css_selector('.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
    comment_boxes.send_keys(reply_content)
    time.sleep(random_number_2)

    # 点击回复按钮
    # reply_button = driver.find_element_by_css_selector('.comment-item .comment-reply')
    reply_button = driver.find_element_by_css_selector(".webcast-chatroom___input-container :nth-child(3)")# 发送点击
    reply_button.click()
    time.sleep(random_number_3)

driver.quit()