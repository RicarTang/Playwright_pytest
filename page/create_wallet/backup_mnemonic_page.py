"""备份助记词页页面模型"""
from playwright.sync_api import Page
import allure
from page.common_page import CommonPageMixin

class BackupMnemonicPage(CommonPageMixin):
    """备份助记词页面模型

    Args:
        CommonPageMixin (_type_): 公共元素类
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 复制助记词button
        self.copy_mnemonic_button = page.locator("//button[text()='复制助记词']")
        # 确认已备份button
        self.confirm_backedup_button = page.locator("//button[text()='确认已备份']")

    @allure.step("点击复制助记词")
    def click_copy_mnemonic_button(self):
        """点击复制助记词"""
        self.copy_mnemonic_button.click()

    @allure.step("点击确认已备份按钮")
    def click_confirm_backedup_button(self):
        """点击确认已备份按钮"""
        self.confirm_backedup_button.click()