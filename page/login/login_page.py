"""登录页面模型"""
from playwright.sync_api import Page
import allure

class LoginPage:
    """登录页面模型"""
    def __init__(self,page:Page):
        # 创建钱包按钮
        self.create_wallet_button = page.locator("//button[text()='创建钱包']")
        # 恢复钱包按钮
        self.restore_wallet_button = page.locator("//button[text()='恢复钱包']")

    @allure.step("点击创建钱包按钮")
    def click_create_wallet_button(self):
        """点击创建钱包按钮"""
        self.create_wallet_button.click()

    @allure.step("点击恢复钱包按钮")
    def click_restore_wallet_button(self):
        """点击恢复钱包按钮"""
        self.restore_wallet_button.click()