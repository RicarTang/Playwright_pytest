"""公共元素页面"""
from pydantic import validate_arguments, StrictInt, StrictStr
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
        # 转账信息面板
        self.__transfer_info_bottom_panel = page.locator(
            "//w-home-payment-details-page"
        )
        # 转账信息面板确认按钮
        self.transfer_info_confirm_button = self.__transfer_info_bottom_panel.locator(
            "//footer/button[text()='下一步']"
        )
        # 关闭面板图标按钮
        self.close_transfer_info_button = self.__transfer_info_bottom_panel.locator(
            "//section//mb-icon[@name='fail']"
        )
        # 返回上一级按钮
        self.back_button = self.__transfer_info_bottom_panel.locator(
            "//section//mb-icon[@name='back']"
        )
        # 二次密码面板
        # bft系钱包链上二次密码input输入框
        self.transfer_info_second_pwd_input = (
            self.__transfer_info_bottom_panel.get_by_role("textbox", name="输入交易密码")
        )
        # bft系钱包下一步button
        self.transfer_info_second_next_button = (
            self.__transfer_info_bottom_panel.get_by_role("button", name="下一步")
        )
        # 确认密码面板
        # 转账密码input
        self.transfer_info_pwd_input = self.__transfer_info_bottom_panel.locator(
            "//section//input[@formcontrolname='password']"
        )

        # 重置密码链接
        self.reset_pwd_link = self.__transfer_info_bottom_panel.locator(
            "//footer//span[text()='忘记密码，去重置']"
        )
        # 确认密码提交按钮
        self.confirm_pwd_submit_button = self.__transfer_info_bottom_panel.locator(
            "//footer//button[@type='submit' and text()='确定']"
        )

    @allure.step("点击交易信息面板下一步按钮")
    def click_transfer_info_confirm_button(self):
        """点击交易信息面板下一步按钮"""
        self.transfer_info_confirm_button.click()

    @allure.step("确认二次密码面板输入链上密码")
    @validate_arguments
    def input_transfer_wallet_second_pwd(self, second_pwd: StrictStr):
        """确认二次密码面板输入链上密码

        Args:
            second_pwd (StrictStr): _description_
        """
        self.transfer_info_second_pwd_input.fill(second_pwd)

    @allure.step("点击确认二次密码面板下一步按钮")
    def click_transfer_info_second_next_button(self):
        """点击确认二次密码面板下一步按钮"""
        self.transfer_info_second_next_button.click()

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

class SelectWalletPanelMixin:
    """选择钱包面板Mixin"""
    def __init__(self,page: Page) -> None:
        # 选择钱包面板
        self.__select_wallet_panel = page.locator("//mb-select-wallet-component")
        # 选择钱包面板h1标题
        self.select_wallet_panel_h1_title = self.__select_wallet_panel.get_by_role("heading",name="选择钱包")
        # 关闭选择钱包面板按钮
        self.select_wallet_panel_close_button = self.__select_wallet_panel.locator("//header//button")
        # 面板ETH身份钱包
        self.select_wallet_panel_eth = self.__select_wallet_panel.locator("//section//div/label[text()='ETH']")
        # 面板BSC身份钱包
        self.select_wallet_panel_bsc = self.__select_wallet_panel.locator("//section//div/label[text()='BSC']")
        # 面板TRX身份钱包
        self.select_wallet_panel_trx = self.__select_wallet_panel.locator("//section//div/label[text()='TRX']")

    @allure.step("点击关闭选择钱包面板按钮")
    def click_select_wallet_panel_close_button(self):
        """点击关闭选择钱包面板按钮"""
        self.select_wallet_panel_close_button.click()

    @allure.step("点击选择面板ETH身份钱包")
    def click_select_wallet_panel_eth(self):
        """点击选择面板ETH身份钱包"""
        self.select_wallet_panel_eth.click()

    @allure.step("点击选择面板BSC身份钱包")
    def click_select_wallet_panel_bsc(self):
        """点击选择面板BSC身份钱包"""
        self.select_wallet_panel_bsc.click()

    @allure.step("点击选择面板TRX身份钱包")
    def click_select_wallet_panel_trx(self):
        """点击选择面板TRX身份钱包"""
        self.select_wallet_panel_trx.click()


class SelectTokenPanelMixin:
    """选择币种面板Mixin"""
    def __init__(self,page: Page) -> None:
        # 选择币种面板
        self.__select_token_panel = page.locator("//mb-select-token-component")
        # 选择币种面板h1标题
        self.select_token_panel_h1_title = self.__select_token_panel.get_by_role("heading",name="选择币种")
        # 选择币种面板关闭按钮
        self.select_token_panel_close_button = self.__select_token_panel.locator("//header//button")
        # 

    @allure.step("点击选择钱包面板关闭按钮")
    def click_select_token_panel_close_button(self):
        """点击选择钱包面板关闭按钮"""
        self.select_token_panel_close_button.click()