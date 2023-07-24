import os
import allure
import pytest
from playwright.sync_api import Page, expect
from utils.load_file import LoadFile
from config import config
from page.login.login_page import LoginPage
from page.restore_wallet.restore_wallet_page import RestoreWalletPage


@allure.epic("登录钱包")
@allure.feature("恢复钱包集")
class TestRestoreWallet:
    """恢复钱包测试用例集"""

    @pytest.mark.skip
    @pytest.mark.restore_wallet
    @pytest.mark.parametrize(
        "data",
        LoadFile(os.path.join(config.TESTCASE_DATA_PATH, "restore_wallet_data.yaml")),
    )
    def test_restore_wallet_case(
        self,
        data,
        page: Page,
        login_page: LoginPage,
        restore_wallet_page: RestoreWalletPage,
    ):
        """恢复钱包测试用例"""
        allure.dynamic.title(data["title"])
        page.goto(config.TEST_URL)
        login_page.click_restore_wallet_button()
        restore_wallet_page.input_wallet_mnemonic(data["data"]["wallet_mnemonic"])
        restore_wallet_page.input_wallet_name(data["data"]["wallet_name"])
        restore_wallet_page.input_wallet_pwd(data["data"]["wallet_pwd"])
        restore_wallet_page.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
        restore_wallet_page.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
        restore_wallet_page.click_user_agreement_checkbox()
        # 断言提交按钮is_disabled
        if data["expect"]["is_enabled"] is True:
            expect(restore_wallet_page.restore_wallet_submit_button).to_be_enabled()
            restore_wallet_page.click_restore_wallet_submit_button()
            # 断言首页元素
        else:
            expect(restore_wallet_page.restore_wallet_submit_button).to_be_disabled()
