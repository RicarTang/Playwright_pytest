import os
import pytest
import allure
from playwright.sync_api import Page, expect
import config
from utils.load_file import LoadFile


@allure.epic("登录钱包")
@allure.feature("创建钱包集")
class TestCreateWallet:
    """创建钱包测试用例集"""

    @pytest.mark.create_wallet
    @pytest.mark.parametrize(
        "data",
        LoadFile(os.path.join(config.TESTCASE_DATA_PATH, "create_wallet_data.yaml")),
    )
    def test_create_wallet_case(
        self,
        data: dict,
        page: Page,
        login_page,
        create_wallet_page,
        backup_or_not_wallet_page,
        backup_mnemonic_page,
        confirm_mnemonic_page,
        home_page,
    ):
        """创建钱包测试用例"""
        allure.dynamic.title(data["title"])
        page.goto("http://127.0.0.1:6939")
        login_page.click_create_wallet_button()
        create_wallet_page.input_wallet_name(data["data"]["wallet_name"])
        create_wallet_page.input_wallet_pwd(data["data"]["wallet_pwd"])
        create_wallet_page.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
        create_wallet_page.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
        create_wallet_page.click_user_agreement_checkbox()
        # 断言提交按钮is_disabled
        if data["expect"]["is_enabled"] is True:
            expect(create_wallet_page.create_wallet_submit_button).to_be_enabled()
            create_wallet_page.click_create_wallet_submit_button()
            if data["title"] == "成功创建钱包,跳过备份":
                # 跳过备份流程
                backup_or_not_wallet_page.click_skip_backup_mnemonic_button()
                backup_or_not_wallet_page.click_backup_abort_button()
                # 断言首页元素可见
                expect(home_page.recharge_invite_dialog_close_button).to_be_visible()
            else:
                # 备份流程
                backup_or_not_wallet_page.click_backup_mnemonic_button()
                backup_mnemonic_page.click_confirm_backedup_button()
                confirm_mnemonic_page.click_confirm_auto_complete_mnemonic_button()
                confirm_mnemonic_page.click_confirm_mnemonic_finish_button()
                # 断言首页元素可见
                expect(home_page.recharge_invite_dialog_close_button).to_be_visible()
        else:
            expect(create_wallet_page.create_wallet_submit_button).to_be_disabled()
