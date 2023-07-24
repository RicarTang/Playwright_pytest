"""首页页面模型"""
from playwright.sync_api import Page
import allure

class HomePage:
    """首页页面模型"""
    def __init__(self,page:Page) -> None:
        # 活动弹窗关闭按钮
        self.recharge_invite_dialog_close_button = page.locator("//mb-recharge-invite-dialog//span[@class='--icon']")
        # 转账按钮
        self.transfer_button = page.locator("//button//div[text()='转账']")
        # 锻造按钮
        self.mint_button = page.locator("//button//div[text()='锻造']")
        # 收款按钮
        self.receive_button = page.locator("//button//div[text()='收款']")

    @allure.step("点击活动弹窗关闭按钮")
    def click_recharge_invite_dialog_close_button(self):
        """点击活动弹窗关闭按钮"""
        self.recharge_invite_dialog_close_button.click()

    @allure.step("点击转账按钮")
    def click_transfer_button(self):
        """点击转账按钮"""
        self.transfer_button.click()

    @allure.step("点击锻造按钮")
    def click_mint_button(self):
        """点击锻造按钮"""
        self.mint_button.click()

    @allure.step("点击收款按钮")
    def click_receive_button(self):
        """点击收款按钮"""
        self.receive_button.click()