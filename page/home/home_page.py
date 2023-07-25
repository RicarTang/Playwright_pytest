"""首页页面模型"""
from playwright.sync_api import Page
import allure


class HomePage:
    """首页页面模型"""

    def __init__(self, page: Page) -> None:
        # 钱包首页(由于多个页面元素都可以在一个页面定位到，先定位首页然后定位其中元素)
        self.__wallet_home_page = page.locator("//w-home-page")
        # 活动弹窗关闭按钮
        self.recharge_invite_dialog_close_button = page.locator(
            "//mb-recharge-invite-dialog//span[@class='--icon']"
        )
        # 转账按钮
        self.transfer_button = self.__wallet_home_page.locator(
            "//button//div[text()='转账']"
        )
        # 锻造按钮
        self.mint_button = self.__wallet_home_page.locator("//button//div[text()='锻造']")
        # 收款按钮
        self.receive_button = self.__wallet_home_page.locator(
            "//button//div[text()='收款']"
        )
        # 钱包菜单按钮
        self.wallet_menu_button = self.__wallet_home_page.locator("//nav/button")
        # 钱包面板
        self.__wallet_bottom_panel = page.locator("//common-page[@headertitle='钱包']")
        # 钱包面板标题
        self.wallet_bottom_panel_title = self.__wallet_bottom_panel.get_by_role(
            "heading", name="钱包"
        )
        # 钱包列表面板关闭按钮
        self.wallet_bottom_panel_close_button = self.__wallet_bottom_panel.locator(
            "//common-page[@headertitle='钱包']//button[@mode='icon']"
        )
        # 钱包列表面板管理按钮
        self.wallet_bottom_panel_manage_button = self.__wallet_bottom_panel.get_by_role(
            "button", name="管理"
        )
        # 钱包列表面板PMC钱包li
        self.pmc_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("PMC")
        # 钱包列表面板BFMT钱包li
        self.bfmt_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("BFMTEST")
        # 钱包列表面板BFT钱包li
        self.bft_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("BFT")
        # 钱包列表面板BSC钱包li
        self.bsc_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("BSC")
        # 钱包列表面板CCC钱包li
        self.ccc_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("CCC")
        # 钱包列表面板ETH钱包li
        self.eth_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("ETH")
        # 钱包列表面板TRX钱包li
        self.trx_wallet_li = self.__wallet_bottom_panel.locator(
            "//w-home-wallet-list/div//li"
        ).get_by_text("TRX")

    @allure.step("点击活动弹窗关闭按钮")
    def click_recharge_invite_dialog_close_button(self):
        """点击活动弹窗关闭按钮"""
        self.recharge_invite_dialog_close_button.click()

    @allure.step("点击转账按钮")
    def click_transfer_button(self):
        """点击转账按钮"""
        self.transfer_button.click()

    @allure.step("点击锻造按钮")
    def click_mint_button(self):
        """点击锻造按钮"""
        self.mint_button.click()

    @allure.step("点击收款按钮")
    def click_receive_button(self):
        """点击收款按钮"""
        self.receive_button.click()

    @allure.step("点击钱包菜单按钮")
    def click_wallet_menu_button(self):
        """点击钱包菜单按钮"""
        self.wallet_menu_button.click()

    @allure.step("点击钱包列表面板关闭按钮")
    def click_wallet_bottom_panel_close_button(self):
        """点击钱包列表面板关闭按钮"""
        self.wallet_bottom_panel_close_button.click()

    @allure.step("点击钱包列表面板管理按钮")
    def click_wallet_bottom_panel_manage_button(self):
        """点击钱包列表面板管理按钮"""
        self.wallet_bottom_panel_manage_button.click()

    @allure.step("点击钱包列表PMC钱包")
    def click_pmc_wallet_li(self):
        """点击钱包列表PMC钱包"""
        self.pmc_wallet_li.click()

    @allure.step("点击钱包列表BFMT钱包")
    def click_bfmt_wallet_li(self):
        """点击钱包列表BFMT钱包"""
        self.bfmt_wallet_li.click()

    @allure.step("点击钱包列表BFT钱包")
    def click_bft_wallet_li(self):
        """点击钱包列表BFT钱包"""
        self.bft_wallet_li.click()

    @allure.step("点击钱包列表BSC钱包")
    def click_bsc_wallet_li(self):
        """点击钱包列表BSC钱包"""
        self.bsc_wallet_li.click()

    @allure.step("点击钱包列表CCC钱包")
    def click_ccc_wallet_li(self):
        """点击钱包列表CCC钱包"""
        self.ccc_wallet_li.click()

    @allure.step("点击钱包列表ETH钱包")
    def click_eth_wallet_li(self):
        """点击钱包列表ETH钱包"""
        self.eth_wallet_li.click()

    @allure.step("点击钱包列表TRX钱包")
    def click_trx_wallet_li(self):
        """点击钱包列表TRX钱包"""
        self.trx_wallet_li.click()
