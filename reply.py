# -*- encoding: utf-8 -*-
'''
@File : reply2.py
@Date : 2023-07-11
@Time : 14:59:25
@Author : lizeyujack@sjtu.edu.cn 
'''
from selenium import webdriver
import time, sys

# replies = ['交汇处', '总建筑面积约为22万平方米', '由3栋高层住宅和1栋洋房组成', '共有900余套房源', '物业类型为智能住宅。建筑设计：该项目由国际著名建筑设计公司HOK担任总体设计师', '设计风格融合了现代简约和中式元素', '外观采用了玻璃幕墙和石材饰面', '营造出高贵典 \
# 雅的氛围。', '房源类型：金地半山风华提供了多种户型选择', '包括约100平方米至300平方 \
# 米不等的2至4房户型和约400平方米至500平方米不等的洋房', '满足不同客户的需求。', '项 \
# 目配套：该项目提供了多项高端配套', '包括超大型会所、恒温泳池、健身房、亲子活动室、私家影院等', '为业主提供了高品质的生活享受。', '交通便利：金地半山风华位于广州市中心 \
# 区域', '周边交通便利', '靠近地铁5号线和6号线', '距离广州火车站和广州南站均不远', '方 \
# 便业主出行。', '价格情况：具体价格因户型和楼层不同而有所差异', '目前该项目的参考均 \
# 价在6万至8万元/平方米左右。','金地半山风华位于广州市天河区龙口中路和龙珠路交汇处，周边商业设施和学校比较丰富，主 \
# 要包括以下几个方面：', '商业设施：周边有多家商场和购物中心，如天河城、正佳广场、太古 \
# 汇等，提供了丰富的购物、餐饮、娱乐等服务。此外，还有多家超市、便利店、药店等生活服务 \
# 设施，满足了居民的日常需求。', '学校：金地半山风华周边有多所优质学校，包括：', '广州 \
# 市天河区龙洞小学', '广州市天河区龙洞第二小学', '广州市第五中学天河分校', '华南理工大 \
# 学附属中学', '广东省实验中学', '这些学校的教学质量和师资力量较为优秀，为业主的子女提 \
# 供了良好的教育资源。', '医疗设施：周边有多家大型医院和诊所，如广州市第一人民医院、广 \
# 东省妇幼保健院、广东省中医院等，为居民提供了全方位的医疗保障。', '总体来说，金地半山 \
# 风华周边的商业设施和学校比较齐全，生活和教育资源丰富，为业主提供了便利和舒适的生活环 \
# 境']
# replies = [
#     "全民健身可以增强身体素质,提高身体免疫力。",
#     "全民健身有助于促进身体循环,保持身体健康。",
#     "全民健身可以促进身体代谢,帮助减少体重。",
#     "全民健身有助于缓解压力,提高身体和心理健康。",
#     "全民健身可以改善睡眠质量,帮助睡眠更加深沉。",
#     "全民健身可以增强心肺功能,提高身体耐力。",
#     "全民健身有助于改善身体姿势,预防脊椎问题。",
#     "全民健身可以增强肌肉力量,提高身体爆发力。",
#     "全民健身有助于改善身体柔韧性,增强身体灵活性。",
#     "全民健身可以增强身体平衡感,预防跌倒和受伤。"
# ]
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
url = 'https://www.douyin.com/video/7252498862038928696'

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

# comment_boxes = driver.find_element_by_css_selector(".richtext-container > .DraftEditor-root")
comment_boxes = driver.find_element_by_css_selector('.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')


# for ele in comment_boxes:
#     print(ele.get_attribute('outerHTML'))

# 遍历所有的评论框,并进行回复
comment_boxes.click()
time.sleep(4)
# idx_ = idx % len(replies)
reply_content = f"{replies[0]},互动，互动，争取早日财务自由"
# 输入回复内容
comment_boxes_ = driver.find_element_by_css_selector('.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
comment_boxes_.send_keys(reply_content)
time.sleep(2)

# 点击回复按钮
# reply_button = driver.find_element_by_css_selector('.comment-item .comment-reply')
reply_button = driver.find_element_by_css_selector(".XAze1wis :nth-child(3)")# 发送点击
reply_button.click()
time.sleep(5)

exists_comment_boxes = driver.find_elements_by_css_selector('.rJFDwdFI :nth-child(3)')# 评论点击
print(len(exists_comment_boxes))
from selenium.webdriver.common.action_chains import ActionChains
action_chains = ActionChains(driver)
# action_chains.drag_and_drop_by_offset(exists_comment_boxes[-1], 0, 1000).perform()
time.sleep(10)
exists_comment_boxes = driver.find_elements_by_css_selector('.rJFDwdFI :nth-child(1) :nth-child(3)')# 评论点击
# exists_likes_boxes = driver.find_elements_by_css_selector('.rJFDwdFI :nth-child(1) :nth-child(1) :nth-child(1)') # 点赞数量
print("本次评论有：",len(exists_comment_boxes))
# print("本次点赞有：",len(exists_likes_boxes))
from tqdm import tqdm
length_diff = len(exists_comment_boxes)
counter, counter_temp = 0, 0
while True:
    # for idx, comment_box in enumerate(exists_comment_boxes):
    for idx in tqdm(range(counter, len(exists_comment_boxes))):
        # 点击评论输入框
        try:
            # try:
            #     like_box = exists_likes_boxes[idx]
            #     like_box.click()
            #     time.sleep(3)
            # except:
                # print('无赞或点赞失败')
            try:
                comment_box = exists_comment_boxes[idx]
                comment_box.click()
                time.sleep(3)
            except:
                print('评论失败')
            idx_ = idx % len(replies)
            reply_content = f"{replies[idx_]},和我互动吧"
            # 输入回复内容
            comment_boxes_ = driver.find_elements_by_css_selector('.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
            comment_boxes_[1].click()# 点击开始评论
            comment_boxes_[1].send_keys(reply_content)
            time.sleep(4.8)
            
            # 点击回复按钮
            reply_button = driver.find_elements_by_css_selector(".XAze1wis :nth-child(3)")
            for i in range(len(reply_button)):
                try:
                    reply_button[i].click()
                    break
                except:
                    pass
            time.sleep(8.5)
        except:
            pass
        counter_temp += 1
    counter = counter_temp
    action_chains.drag_and_drop_by_offset(exists_comment_boxes[-1], 0, 1000).perform()
    time.sleep(10)
    exists_comment_boxes = driver.find_elements_by_css_selector('.rJFDwdFI :nth-child(1) :nth-child(3)')# 评论点击
    # exists_likes_boxes = driver.find_elements_by_css_selector('.rJFDwdFI :nth-child(1) :nth-child(1) :nth-child(1)')# 点击红心
    print("本次新增评论有：",len(exists_comment_boxes)-counter)
    if counter >len(replies)+1:
        break
# 关闭浏览器
driver.quit()
