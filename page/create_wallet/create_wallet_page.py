"""创建钱包页页面模型"""
from pydantic import validate_arguments,StrictStr
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin

class CreateWalletPage(GoBackMixin):
    """创建钱包页页面模型

    Args:
        GoBackMixin (_type_): 返回元素Mixin
    """
    def __init__(self,page: Page):
        super().__init__(page)
        # 钱包名称input
        self.wallet_name_input = page.locator("//input[@placeholder='输入1~12个字符']")
        # 钱包密码input
        self.wallet_pwd_input = page.locator("//input[@placeholder='密码至少8个字符']")
        # 确认密码input
        self.wallet_confirm_pwd_input = page.locator("//input[@placeholder='确认密码']")
        # 密码提示input
        self.wallet_pwd_hint_input = page.locator("//input[@placeholder='输入密码提示信息']")
        # 选择助记词语言button
        self.choose_mnemonic_language_button = page.locator("//button/div[contains((text()),'English')]")
        # 选择助记词数量button
        self.choose_mnemonic_number_button = page.locator("//button/div[contains((text()),'12 个字')]")
        # 用户协议checkbox
        self.user_agreement_checkbox = page.locator("//input[@type='checkbox'and@id='agree']")
        # 用户协议
        self.user_agreement_span = page.locator("//span[text()='用户协议']")
        # 创建钱包submit button
        self.create_wallet_submit_button = page.locator("//button[@type='submit']")

    @allure.step("输入钱包名称")
    @validate_arguments
    def input_wallet_name(self,wallet_name:StrictStr):
        """输入钱包名称

        Args:
            wallet_name (StrictStr): _description_
        """
        self.wallet_name_input.fill(wallet_name)

    @allure.step("输入钱包密码")
    @validate_arguments
    def input_wallet_pwd(self,wallet_pwd:StrictStr):
        """输入钱包密码

        Args:
            wallet_pwd (StrictStr): _description_
        """
        self.wallet_pwd_input.fill(wallet_pwd)

    @allure.step("输入钱包确认密码")
    @validate_arguments
    def input_wallet_confirm_pwd(self,wallet_pwd:StrictStr):
        """输入确认钱包密码

        Args:
            wallet_pwd (StrictStr): _description_
        """
        self.wallet_confirm_pwd_input.fill(wallet_pwd)

    @allure.step("输入钱包密码提示")
    @validate_arguments
    def input_wallet_pwd_hint(self,wallet_pwd_hint:StrictStr):
        """输入钱包密码提示

        Args:
            wallet_pwd_hint (StrictStr): _description_
        """
        self.wallet_pwd_hint_input.fill(wallet_pwd_hint)

    @allure.step("点击选择助记词语言")
    def click_choose_mnemonic_language(self):
        """点击选择助记词语言"""
        self.choose_mnemonic_language_button.click()

    @allure.step("点击选择助记词数量")
    def click_choose_mnemonic_number(self):
        """点击选择助记词数量"""
        self.choose_mnemonic_number_button.click()

    @allure.step("点击勾选用户协议")
    def click_user_agreement_checkbox(self):
        """点击勾选用户协议"""
        self.user_agreement_checkbox.click()

    @allure.step("点击查看用户协议")
    def click_view_user_agreement(self):
        """点击查看用户协议"""
        self.user_agreement_span.click()
    
    @allure.step("点击创建钱包按钮")
    def click_create_wallet_submit_button(self):
        """点击创建钱包按钮"""
        self.create_wallet_submit_button.click()

    