"""公共元素页面"""
from pydantic import validate_arguments,StrictInt,StrictStr
from playwright.sync_api import Page
import allure


class GoBackMixin:
    """全局返回按钮Mixin"""

    def __init__(self, page: Page) -> None:
        # 返回按钮
        self.go_back_button = page.locator("//button[@mode='icon']").last

    @allure.step("点击返回按钮")
    def click_go_back(self):
        """点击返回按钮"""
        self.go_back_button.click()


class TransferInfoMixin:
    """签名面板/密码面板组件元素Mixin"""

    def __init__(self, page: Page) -> None:
        # 转账信息面板确认按钮
        self.transfer_info_confirm_button = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/footer/button[text()='下一步']"
        )
        # 关闭面板图标按钮
        self.close_transfer_info_button = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/section//mb-icon[@name='fail']"
        )
        # 返回上一级按钮
        self.back_button = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/section//mb-icon[@name='back']"
        )
        # 转账密码input
        self.transfer_info_pwd_input = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/section//input[@formcontrolname='password']"
        )
        # 重置密码链接
        self.reset_pwd_link = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/footer//span[text()='忘记密码，去重置']"
        )
        # 确认密码提交按钮
        self.confirm_pwd_submit_button = page.locator(
            "//mat-bottom-sheet-container//common-page[@class='loose-footer']/footer//button[@type='submit' and text()='确定']"
        )

    @allure.step("点击交易信息面板下一步按钮")
    def click_transfer_info_confirm_button(self):
        """点击交易信息面板下一步按钮"""
        self.transfer_info_confirm_button.click()

    @allure.step("密码面板输入钱包密码")
    @validate_arguments
    def input_transfer_wallet_pwd(self, pwd: StrictStr):
        """密码面板输入钱包密码

        Args:
            pwd (StrictStr): _description_
        """
        self.transfer_info_pwd_input.fill(pwd)

    @allure.step("点击密码面板确定按钮")
    def click_confirm_pwd_submit_button(self):
        """点击密码面板确定按钮"""
        self.confirm_pwd_submit_button.click()
