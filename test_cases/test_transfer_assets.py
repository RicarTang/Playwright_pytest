import os
import pytest
import allure
from playwright.sync_api import expect
from config import config
from utils.load_file import LoadFile
from page.home.home_page import HomePage
from page.transfer.transfer_page import TransferPage


@allure.epic("转账")
@allure.feature("转账PMC")
class TestTransferPMC:
    """转账PMC测试"""

    @pytest.mark.transfer_assets
    @pytest.mark.parametrize(
        "data",
        LoadFile(os.path.join(config.TESTCASE_DATA_PATH, "transfer_pmc_data.yaml")),
    )
    def test_transfer_pmc_case(
        self,
        data: dict,
        restore_wallet,
        home_page: HomePage,
        transfer_page: TransferPage,
    ):
        allure.dynamic.title(data["title"])
        home_page.click_recharge_invite_dialog_close_button()
        home_page.click_transfer_button()
        transfer_page.input_receive_address(data["data"]["receive_address"])
        transfer_page.input_transfer_amount(data["data"]["amount"])
        transfer_page.input_transfer_memo(data["data"]["memo"])
        expect(transfer_page.submit_transfer_button).to_be_enabled()
        transfer_page.click_submit_transfer_button()
