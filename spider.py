import re
import os
import requests
import random
import socket
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree


driver = webdriver.Firefox()

# 网站入口
url = 'http://www.57mh.com/118/'

# 定制请求头（模拟浏览器访问）

user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                   "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                   "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
                   ]

UA = random.choice(user_agent_list)
headers = {'User-Agent': UA}

# 这里对整个socket层设置超时时间
# timeout = 30
# socket.setdefaulttimeout(timeout)
# sleep_download_time = 30
# time.sleep(sleep_download_time)


response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    # 单个网页集合
    href_list = soup.find('div', class_='chapter-list cf mt10').find_all('a')
    for href in href_list:
        # 单独网页集合
        jihe_href = href['href']
        jihe_name = href['title']
        # print(jihe_href)

        dir_name = str(jihe_name).strip()
        os.makedirs(os.path.join("G:\Cartoon", dir_name))  # 创建一个存放套图的文件夹
        os.chdir("G:\Cartoon\\" + dir_name)  # 切换到上面创建的文件夹


        single_url = 'http://www.57mh.com/' + jihe_href
        # print(single_url)

        # 此处加一个循环（页数的循环）
        # 获取单独网页链接的内容


        # 这里对整个socket层设置超时时间
        # timeout = 10
        # sleep_download_time = 10
        # socket.setdefaulttimeout(timeout)
        # time.sleep(sleep_download_time)

        single_response = requests.get(single_url, headers=headers)
        single_response.encoding = 'utf-8'
        if single_response.status_code == 200:
            # 解析单独网页链接的内容
            single_soup = BeautifulSoup(single_response.text, 'lxml')

            all_option = single_soup.find('div', class_='w996 tc').find_all('option')[-1].get_text()
            # print(all_a)

            pattern = re.compile(r'第(.*?)页')
            items = re.findall(pattern, all_option)
            for item in items:
                # print(item)
                for page in range(1, int(item) + 1):
                    page_url = single_url + '?p=' + str(page)
                    # print(page_url)  # 这个page_url就是每张图片的页面地址啦！但还不是实际地址！


                    # img_response = requests.get(page_url, headers=headers)
                    # img_response.encoding = 'utf-8'
                    # if img_response.status_code == 200:

                    # 最初的方法（BeautifulSoup）
                    # img_soup = BeautifulSoup(img_response.text, 'lxml')
                    # img_url = img_soup.find('tr').find('img')['src']
                    # print(img_url)


                    # 第一种方法（XPATH）
                    # img_path = etree.HTML(img_response.text)
                    # img_url = img_path.xpath('//*[(@id = "manga")]//@src')
                    # print(img_url)


                    # 第二种方法(CSS选择器)
                    # img_url = img_soup.select('#manga')
                    # print(img_url)

                    # 第三种方法（正则表达式）
                    # img_pattern = re.compile('<img id.*?src="(.*?)".*?/>', re.S)
                    # img_pattern = re.compile(r'<img id.*?src="(.*?)".*?/>')
                    # img_url = re.findall(img_pattern, img_response.text)
                    # print(img_url)


                    # 以上方法都不行，原因是图片采用的是JS动态加载技术，需要另觅他法


                    # 利用selenium技术提取网页代码
                    driver.get(page_url)
                    img_soup = BeautifulSoup(driver.page_source, 'lxml')
                    img_url = img_soup.find('tr').find('img')['src']
                    print(img_url)

                    # file_name = img_url[-5:-4]
                    # file_name = random.uniform(1, 1000)

                    # 这里对整个socket层设置超时时间
                    timeout = 10
                    sleep_download_time = 10
                    socket.setdefaulttimeout(timeout)
                    time.sleep(sleep_download_time)


                    file_name = str(page)
                    img = requests.get(img_url, headers=headers)
                    with open(str(file_name) + '.jpg', 'ab') as f:
                        f.write(img.content)

