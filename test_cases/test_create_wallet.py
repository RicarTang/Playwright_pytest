import os
import pytest
import allure
from playwright.sync_api import Page,expect
import config
from page.login_page import LoginPage
from page.create_wallet_page import CreateWalletPage
from utils.load_file import LoadFile

@allure.epic("登录钱包")
@allure.feature("创建钱包集")
class TestCreateWallet:
    """创建钱包测试用例集"""
    # def setup_class(self,page:Page):
    #     """类前置"""
    #     self.page = page

    @pytest.mark.create_wallet
    @pytest.mark.parametrize(
        "data",
        LoadFile(
            os.path.join(config.TESTCASE_DATA_PATH, "create_wallet_data.yaml")
        ),
    )
    def test_create_wallet_case(self, data: dict,page:Page):
        """创建钱包测试用例"""
        allure.dynamic.title(data["title"])
        page.goto("http://127.0.0.1:6939")
        login_page = LoginPage(page)
        login_page.click_create_wallet_button()
        create_wallet_page = CreateWalletPage(page)
        create_wallet_page.input_wallet_name(data["data"]["wallet_name"])
        create_wallet_page.input_wallet_pwd(data["data"]["wallet_pwd"])
        create_wallet_page.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
        create_wallet_page.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
        create_wallet_page.click_user_agreement_checkbox
        # 断言提交按钮is_disabled
        expect(create_wallet_page.create_wallet_submit_button).to_be_disabled()
        # assert (

        #     self.locator(self.create_wallet_submit).is_enabled()
        #     is data["expect"]["is_enabled"]
        # )
        # self.click_create_wallet_submit_button()
        # if data["expect"]["is_enabled"] is True:
        #     if data["title"] == "成功创建钱包,跳过备份":
        #         # 跳过备份流程
        #         self.click_skip_backup_mnemonic_button()
        #         self.click_backup_abort_button()
        #         assert True  # 断言主页元素
        #     else:
        #         # 备份流程
        #         self.click_backup_mnemonic_button()
        #         self.click_confirm_backedup_button()
        #         self.click_confirm_auto_complete_mnemonic_button()
        #         self.click_confirm_mnemonic_finish_button()
        #         assert True  # 断言主页元素