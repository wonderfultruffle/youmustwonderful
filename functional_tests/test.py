import time
from selenium import webdriver

from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    test_time = time.time()

    def setUp(self) -> None:

        # remote node 가 GUI 를 지원하지 않는 환경이므로(ubuntu 22.04_server) '--headless' option을 사용한다.
        # ff_opt = webdriver.FirefoxOptions()
        # ff_opt.add_argument("--headless")
        # self.browser = webdriver.Firefox(options=ff_opt)

        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument(f"--headless")
        self.browser = webdriver.Chrome(options=chrm_opt)
        
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()

        self.test_time = round(time.time() - self.test_time, 2)
        print(f"Spent time : {self.test_time}")
        return super().tearDown()

    def test_board_top_level_view(self):
        # 게시판 app의 top level page 에 접속한다.
        self.browser.get(f"{self.live_server_url}/board/")

        # 게시판 app의 top level page 가 잘 동작하는 지 확인한다.
        self.assertIn("게시판 top", self.browser.find_element("tag name", "body").text)


    # def test_visit_todolist(self):
