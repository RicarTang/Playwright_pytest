"""选择币种页面模型"""
from pydantic import validate_arguments,StrictStr
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin

class SelectAssetPage(GoBackMixin):
    """选择币种页面模型

    Args:
        GoBackMixin (_type_): _description_
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        # 页面h1标题
        self.page_h1_title = page.locator("//h1[text()=' 选择币种 ']")
        
    @allure.step("点击币种")
    @validate_arguments
    def click_asset_button(self,asset_name:StrictStr):
        """点击币种,因为button太多使用填充参数达到定位

        Args:
            asset_name (StrictStr): 币种名称
        """
        locator = self.page.get_by_text(" "+asset_name.upper()+" ")
        locator.click()