"""公共元素页面"""
from playwright.sync_api import Page
import allure

class CommonPageMixin:
    """公共元素Mixin"""
    def __init__(self,page: Page) -> None:
        self.page = page
        # 返回按钮
        self.go_back_button = page.locator("//button[@mode='icon']")

    @allure.step("点击返回按钮")
    def click_go_back(self):
        """点击返回按钮"""
        self.go_back_button.click()
