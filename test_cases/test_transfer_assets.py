import os
import pytest
import allure
from playwright.sync_api import expect, Page
from config import config
from utils.load_file import LoadFile
from page.home.home_page import HomePage
from page.transfer.transfer_page import TransferPage
from page.asset_detail.asset_detail_list_page import AssetDetailListPage
from page.transfer.select_asset_page import SelectAssetPage


@allure.epic("转账")
@allure.feature("转账PMC")
class TestTransferPMC:
    """转账PMC测试"""

    @pytest.mark.transfer_pmc
    @pytest.mark.transfer_assets
    @pytest.mark.parametrize(
        "data",
        LoadFile(
            os.path.join(config.TESTCASE_DATA_PATH, "pmc", "transfer_pmc_data.yaml")
        ),
    )
    def test_transfer_pmc_case(
        self,
        data: dict,
        restore_wallet,
        home_page: HomePage,
        transfer_page: TransferPage,
        asset_detail_list_page: AssetDetailListPage,
    ):
        """成功转账pmc测试

        Args:
            data (dict): 参数化dict数据
            restore_wallet (_type_): 恢复钱包前置
            home_page (HomePage): _description_
            transfer_page (TransferPage): _description_
            asset_detail_list_page (AssetDetailListPage): _description_
        """
        allure.dynamic.title(data["title"])
        home_page.click_recharge_invite_dialog_close_button()
        home_page.click_transfer_button()
        transfer_page.input_receive_address(data["data"]["receive_address"])
        transfer_page.input_transfer_amount(data["data"]["amount"])
        transfer_page.input_transfer_memo(data["data"]["memo"])
        expect(transfer_page.submit_transfer_button).to_be_enabled()
        transfer_page.click_submit_transfer_button()
        transfer_page.click_transfer_info_confirm_button()
        transfer_page.input_transfer_wallet_pwd(data["data"]["transfer_wallet_pwd"])
        transfer_page.click_confirm_pwd_submit_button()
        expect(asset_detail_list_page.page_h1_title).to_be_visible()

    @pytest.mark.transfer_usdm
    @pytest.mark.transfer_assets
    @pytest.mark.parametrize(
        "data",
        LoadFile(
            os.path.join(config.TESTCASE_DATA_PATH, "pmc", "transfer_usdm_data.yaml")
        ),
    )
    def test_transfer_usdm_case(
        self,
        data: dict,
        restore_wallet,
        home_page: HomePage,
        transfer_page: TransferPage,
        select_asset_page: SelectAssetPage,
        asset_detail_list_page: AssetDetailListPage,
    ):
        """成功转账usdm测试

        Args:
            data (dict): _description_
            restore_wallet (_type_): _description_
            home_page (HomePage): _description_
            transfer_page (TransferPage): _description_
            asset_detail_list_page (AssetDetailListPage): _description_
        """
        allure.dynamic.title(data["title"])
        home_page.click_recharge_invite_dialog_close_button()
        home_page.click_transfer_button()
        # 选择USDM资产
        transfer_page.click_select_asset_button()
        expect(select_asset_page.page_h1_title).to_be_visible()
        select_asset_page.click_asset_button("usdm")
        transfer_page.input_receive_address(data["data"]["receive_address"])
        transfer_page.input_transfer_amount(data["data"]["amount"])
        transfer_page.input_transfer_memo(data["data"]["memo"])
        expect(transfer_page.submit_transfer_button).to_be_enabled()
        transfer_page.click_submit_transfer_button()
        transfer_page.click_transfer_info_confirm_button()
        transfer_page.input_transfer_wallet_pwd(data["data"]["transfer_wallet_pwd"])
        transfer_page.click_confirm_pwd_submit_button()
        expect(asset_detail_list_page.page_h1_title).to_be_visible()

