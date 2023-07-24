"""确认助记词页页面模型"""
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin

class ConfirmMnemonicPage(GoBackMixin):
    """确认助记词页页面模型

    Args:
        GoBackMixin (_type_): 返回元素Mixin
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 确认自动补全助记词button（测试环境）
        self.confirm_auto_complete_mnemonic_button = page.locator("//button[text()=' 确定 ']")
        # 取消自动补全助记词button（测试环境）
        self.cancel_auto_complete_mnemonic_button = page.locator("//button[text()=' 取消 ']")
        # 确认完成button
        self.confirm_finish_button = page.locator("//button/bn-loading-wrapper/div[contains(text(),'完成')]")

    @allure.step("点击确认自动补全助记词按钮")
    def click_confirm_auto_complete_mnemonic_button(self):
        """点击自动补全助记词按钮"""
        self.confirm_auto_complete_mnemonic_button.click()

    @allure.step("点击取消自动补全助记词按钮")
    def click_cancel_auto_complete_mnemonic_button(self):
        """点击取消自动补全助记词按钮"""
        self.cancel_auto_complete_mnemonic_button.click()

    @allure.step("点击确认助记词完成按钮")
    def click_confirm_mnemonic_finish_button(self):
        """点击确认助记词完成按钮"""
        self.confirm_finish_button.click()