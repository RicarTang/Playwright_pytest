import os
import pytest
import allure
from playwright.sync_api import expect, Page
from config import config
from utils.load_file import LoadFile
from page.home.home_page import HomePage

# @allure.epic("锻造")
# @allure.feature("锻造")
# class TestMint:
#     """锻造测试"""
#     @pytest.mark.transfer_mint
#     @pytest.mark.transfer_mint_trx
#     @pytest.mark.parametrize(
#         "data",
#         LoadFile(
#             os.path.join(config.TESTCASE_DATA_PATH, "mint", "mint_trx_data.yaml")
#         ),
#     )
#     def test_transfer_bfmt_case(
#         self,
#         data: dict,
#         restore_wallet,
#         home_page: HomePage,
#     ):
#         """_summary_

#         Args:
#             data (dict): _description_
#             restore_wallet (_type_): _description_
#             home_page (HomePage): _description_
#         """
#         pass