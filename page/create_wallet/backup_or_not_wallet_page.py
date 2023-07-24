"""是否备份钱包页页面模型"""
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin

class BackupOrNotWalletPage(GoBackMixin):
    """是否备份钱包页页面模型

    Args:
        GoBackMixin (_type_): 返回元素Mixin
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 立即备份助记词button
        self.backup_mnemonic_button = page.locator("//button[text()='立即备份助记词']")
        # 跳过备份div
        self.skip_backup_mnemonic_div = page.locator("//div[text()='跳过备份']")
        # 是否备份弹窗放弃备份button
        self.backup_abort_button = page.locator("//common-card//button[text()=' 放弃备份 ']")
        # 是否备份弹窗取消button
        self.cancel_button = page.locator("//common-card//button[text()=' 取消 ']")

    @allure.step("点击立即备份助记词")
    def click_backup_mnemonic_button(self):
        """点击立即备份助记词"""
        self.backup_mnemonic_button.click()

    @allure.step("点击跳过备份")
    def click_skip_backup_mnemonic_button(self):
        """点击跳过备份"""
        self.skip_backup_mnemonic_div.click()

    @allure.step("点击跳过备份弹窗放弃备份按钮")
    def click_backup_abort_button(self):
        """点击跳过备份弹窗放弃备份按钮"""
        self.backup_abort_button.click()

    @allure.step("点击跳过备份弹窗取消按钮")
    def click_backup_abort_cancel_button(self):
        """点击跳过备份弹窗取消按钮"""
        self.cancel_button.click()