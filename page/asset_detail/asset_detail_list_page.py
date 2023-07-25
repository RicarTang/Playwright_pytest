"""资产列表详情页页面模型"""
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin

class AssetDetailListPage(GoBackMixin):
    """资产列表详情页页面模型

    Args:
        GoBackMixin (_type_): _description_
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 页面h1标题
        self.page_h1_title = page.locator("//h1[contains(text(),' 详情 ')]")
        # 转账按钮
        self.transfer_button = page.locator("//div[@footer]//button[text()='转账']")
        # 收款按钮
        self.receive_button = page.locator("//div[@footer]//button[text()='收款']")

    @allure.step("点击转账按钮")
    def click_transfer_button(self):
        """点击转账按钮"""
        self.transfer_button.click()

    @allure.step("点击收款按钮")
    def click_receive_button(self):
        """点击收款按钮"""
        self.receive_button.click()
        