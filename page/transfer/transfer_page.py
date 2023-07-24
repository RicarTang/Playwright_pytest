"""转账页面模型"""
from playwright.sync_api import Page
import allure
from page.common_page import GoBackMixin,TransferInfoMixin


class TransferPage(TransferInfoMixin,GoBackMixin):
    """转账页面模型

    Args:
        GoBackMixin (_type_): _description_
    """

    def __init__(self, page: Page) -> None:
        TransferInfoMixin.__init__(self,page)
        GoBackMixin.__init__(self,page)
        # 收款地址input
        self.receive_address_input = page.locator(
            "//input[@placeholder='请输入 Pay Meta Chain地址']"
        )
        # 选择资产button
        self.select_asset_button = page.locator("//button[@mode='text']")
        # 转账金额input
        # self.transfer_amount_input = page.locator("//input[@placeholder='输入数量']")
        self.transfer_amount_input = page.get_by_role("group", name="转账金额").get_by_placeholder("输入数量")  # 同样出现两个元素
        # 全部button
        self.all_button = page.locator("//button[@mode='text' and text()='全部']")
        # 附言input
        self.memo_input = page.locator("//input[@placeholder='附言（选填）']")
        # 选择矿工费button
        self.select_miner_fee_button = page.locator(
            "//fieldset[@class='ng-star-inserted']/button"
        )
        # 修改旷工费input
        self.modify_miner_fee_input = page.locator(
            "//common-card[@headertitle='矿工费']//input"
        )
        # 确定修改矿工费button
        self.miner_fee_confirm_button = page.locator(
            "//common-card[@headertitle='矿工费']//button[text()=' 确定 ']"
        )
        # 取消修改矿工费button
        self.miner_fee_cancel_button = page.locator(
            "//common-card[@headertitle='矿工费']//button[text()=' 取消 ']"
        )
        # 提交转账button
        self.submit_transfer_button = page.locator(
            "//form//button[@type='submit']"
        ).first  # 莫名其妙定位出两个submit按钮，好像还是同一个，使用first解决严格模式检查

    @allure.step("输入收款地址")
    def input_receive_address(self, address: str):
        """输入收款地址

        Args:
            address (str): _description_
        """
        self.receive_address_input.fill(address)

    @allure.step("点击选择资产按钮")
    def click_select_asset_button(self):
        """点击选择资产按钮"""
        self.select_asset_button.click()

    @allure.step("输入转账金额")
    def input_transfer_amount(self, amount: str | int):
        """输入收款地址

        Args:
            address (str): _description_
        """
        self.transfer_amount_input.fill(str(amount))

    @allure.step("输入转账附言")
    def input_transfer_memo(self, memo: str):
        """输入收款地址

        Args:
            address (str): _description_
        """
        self.memo_input.fill(memo)

    @allure.step("点击选择修改矿工费")
    def click_select_miner_fee_button(self):
        """点击选择修改矿工费"""
        self.select_miner_fee_button.click()

    @allure.step("输入修改的矿工费")
    def input_modify_miner_fee(self, fee: str | int):
        """输入修改的矿工费

        Args:
            fee (str | int): _description_
        """
        self.modify_miner_fee_input.clear()
        self.modify_miner_fee_input.fill(str(fee))

    @allure.step("点击确定修改矿工费按钮")
    def click_miner_fee_confirm_button(self):
        """点击确定修改矿工费按钮"""
        self.miner_fee_confirm_button.click()

    @allure.step("点击取消修改矿工费按钮")
    def click_miner_fee_cancel_button(self):
        """点击确定修改矿工费按钮"""
        self.miner_fee_cancel_button.click()

    @allure.step("点击提交转账按钮")
    def click_submit_transfer_button(self):
        """点击提交转账按钮"""
        self.submit_transfer_button.click()
