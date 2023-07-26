"""锻造页面模型"""
from pydantic import validate_arguments,StrictStr
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin


class MintPage(GoBackMixin):
    """锻造页面模型

    Args:
        GoBackMixin (_type_): _description_
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 锻造页面
        self.mint_page = page.locator("//mb-deposit-page")
        # 发送地址
        # self.send_address_