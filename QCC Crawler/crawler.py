from selenium import webdriver  # 从selenium导入浏览器驱动
from selenium.webdriver.common.by import By  # 导入网页元素定位模块
from bs4 import BeautifulSoup  # 导入网页解析库
import time  # 导入时间库,利用time.sleep()防止爬虫访问过于频繁被禁止访问
from tqdm import tqdm  # 导入进度条模块,可视化爬取进程
import re  # 导入正则表达式,过滤出符合要求的网页链接
import openpyxl  # 导入Excel表格处理库
import os  # 导入路径库,设置Excel存储路径


def login():
    """登录,以获取最新的cookies"""
    driver = explorer()
    driver.get('https://www.qcc.com')  # 浏览器打开网站
    print('企查查官网已打开，请登录！')
    time.sleep(20)  # 暂停20秒，请务必登录，以获得cookies
    login_cookies = driver.get_cookies()
    print('登录成功,cookies获取成功!')
    print('-' * 28)
    driver.quit()  # 关闭浏览器
    return login_cookies


# 下面使用循环对公司列表中的每个公司进行爬取，并存储到文件
def spider(company_list, login_cookies, file_path):
    """爬取企业股权信息"""

    for company in tqdm(company_list):
        shareholders = []  # 储存股东名称
        shareholding = []  # 储存持股比例
        subscribed_capital = []  # 储存认缴出资额

        driver = explorer()
        driver.maximize_window()  # 最大化浏览器窗口

        driver.get("https://www.qcc.com")
        time.sleep(1)
        '''设置cookies'''
        cookies = login_cookies
        for cookie in cookies:
            driver.add_cookie(cookie)  # 将cookies添加到浏览器
        driver.refresh()  # 自动刷新页面,将登录账号
        try:
            print('开始匹配' + company)
            driver.find_element(By.ID, "searchKey").send_keys(company)  # 寻找输入框，输入要查询的企业名称
            time.sleep(4)
            driver.find_element(By.TAG_NAME, "button").click()  # 模仿浏览器点击搜索按钮
            time.sleep(1)
            driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div[2]/div/table/tr[1]/td[3]/div/span/span[1]/a") \
                .click()  # 进入对应公司网页
            time.sleep(2)
            company_page = BeautifulSoup(driver.page_source, 'html.parser')  # 将加载好的网页用BeautifulSoup解析成文本
            urls = re.findall(
                r'<span class="text-primary" data-v-5be7f8e2=""><a data-v-5be7f8e2="" href="(.*?)" target="_blank">',
                str(company_page))
            driver.get(urls[0])  # 进入公司股权结构网页
            time.sleep(1)
            '''设置cookies'''
            cookies = login_cookies
            for cookie in cookies:
                driver.add_cookie(cookie)  # 将cookies添加到浏览器
            driver.refresh()  # 自动刷新页面,将登录账号
            time.sleep(3)
            result_page = BeautifulSoup(driver.page_source, 'html.parser')
            stock_right_information = result_page.find(class_='app-tree-table').find(class_='ntable').find_all('tr')
            for info in stock_right_information[1:]:
                td_list = info.find_all('td')
                name = td_list[1].find(class_='name').text.strip()  # 爬取股东名称
                ratio = td_list[2].text.strip('\n').strip()  # 爬取持股比例
                capital = td_list[3].find('div').text.strip()  # 爬取认缴出资额

                shareholders.append(name)
                shareholding.append(ratio)
                subscribed_capital.append(capital)

            dataframe = []

            title_info = stock_right_information[0]
            th_list = title_info.find_all('th')[1:4]
            title_list = []
            for i in range(len(th_list)):
                if i == 1:
                    title_list.append(th_list[i].text[0:4])
                elif i == 2:
                    title_list.append(th_list[i].text[0:10].strip('\n'))
                else:
                    title_list.append(th_list[i].text.strip('\n').strip())

            dataframe.append(title_list)
            print(company + '匹配成功\n', '企业股东为:\n', shareholders, '\n', '各股东持股比例为:\n', shareholding,
                  '\n', '认缴出资额为:\n', subscribed_capital)

            for i in range(len(shareholders)):
                dataframe.append([shareholders[i], shareholding[i], subscribed_capital[i]])
            save_data(file_path, company, dataframe)  # 将信息录入Excel中
            print(company + '股权信息储存成功')
        except Exception as error:
            print('匹配失败。可能原因为:该公司无股东,或网页布局更改。\n%s' % error)


def save_data(file_path, company_name, dataframe):
    os.chdir(file_path)  # 工作路径（Excel文件储存路径）
    create = not os.path.exists('text.xlsx')
    if create:
        workbook = openpyxl.Workbook()
        sheet = workbook.active  # 获取活动表
        sheet.append([company_name])  # 输入表格标题
        for row in dataframe:
            sheet.append(row)
        workbook.save('text.xlsx')
    else:
        write_data('text.xlsx', company_name, dataframe)


def write_data(file_name, company_name, dataframe):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active  # 获取活动表
    sheet.append([''])
    sheet.append([company_name])
    for row in dataframe:
        sheet.append(row)
    workbook.save('text.xlsx')


def explorer():
    options = webdriver.EdgeOptions()
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 '
        'Safari/537.36 Edg/109.0.1518.70')
    options.add_argument("disable-blink-features=AutomationControlled")  # 去除webdriver痕迹
    driver = webdriver.Edge(options=options)
    return driver


if __name__ == '__main__':
    path = r'./'
    new_cookies = login()
    while True:
        company_input = input('请输入需要查询的企业名称，若是多家企业则需用|隔开。如：企查查科技有限公司|腾讯科技（深圳）有限公司:')
        companies = company_input.split('|')
        if len(company_input) == 0:
            companies = company_input
            if companies == '':
                quit_input = input('是否退出程序？[Y/n]')
                if quit_input == 'Y':
                    exit()
            else:
                spider(companies, new_cookies, path)
        else:
            spider(companies, new_cookies, path)
