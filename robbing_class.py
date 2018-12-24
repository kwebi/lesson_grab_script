from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

class Worm():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='./firefox_driver/geckodriver.exe')
        self.login_url = 'https://mis.bjtu.edu.cn'
        self.rob_url = 'https://mis.bjtu.edu.cn/module/module/322/'
        with open('config.json', 'r', encoding='UTF-8') as json_f:
            load_dict = json.load(json_f)
            self.user_id = load_dict['user_id']
            self.passwd = load_dict['user_passwd']
            self.lesson_num = load_dict['lesson_num']


    def _login(self):
        self.driver.get(self.login_url)
        stu_num = self.driver.find_element_by_xpath('//input[@name="loginname"]')
        stu_num.send_keys(self.user_id)
        stu_passwd = self.driver.find_element_by_xpath('//input[@name="password"]')
        stu_passwd.send_keys(self.passwd)
        sub_btn = self.driver.find_element_by_xpath('//button[@class="btn btn-success "]')
        sub_btn.click()
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be('https://mis.bjtu.edu.cn/home/')
        )
        print('登陆成功')


    def _order(self):
        # 跳转到新教务系统
        self.driver.get(self.rob_url)
        print('跳转教务系统成功')
        lesson_btn = self.driver.find_element_by_xpath('//a[@href="/course_selection/courseselect/stuschedule/"]')
        lesson_btn.click()
        while True:
            #课余量查询
            cp_menu = self.driver.find_element_by_xpath('//a[@href="/course_selection/courseselecttask/remains/"]')
            cp_menu.click()
            input_elem = self.driver.find_element_by_xpath('//input[@class="form-control autocomplete tt-input"]')
            input_elem.send_keys(self.lesson_num)
            query_btn = self.driver.find_element_by_xpath('//input[@value=" 查询 "]')
            query_btn.click()
            #等待信息显示
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td'))
            )
            tr = self.driver.find_elements_by_xpath('//tbody/tr')
            if len(tr) < 2:
                continue
            td = tr[1].find_elements_by_xpath('.//td')

            if int(td[4].text) > 0:
                #开始抢课
                select_menu = self.driver.find_element_by_xpath('//a[@href="/course_selection/courseselecttask/selects/"]')
                select_menu.click()
                break

    def run(self):
        self._login()
        self._order()

if __name__ == '__main__':
    worm = Worm()
    worm.run()
