from selenium import webdriver

from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        
        return super().tearDown()
    
    def test_board_top_level_view(self):
        # 게시판 app 에 접속한다.
        self.browser.get(f"{self.live_server_url}/board/")
        
        # 게시판 app의 top level 인 list view 가 잘 동작하는 지 확인한다.
        self.assertIn("게시판 top", self.browser.find_element("xpath", "body").text)
    
    