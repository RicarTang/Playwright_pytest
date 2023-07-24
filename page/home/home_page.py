"""首页页面模型"""
from playwright.sync_api import Page
import allure

class HomePage:
    """首页页面模型"""
    def __init__(self,page:Page) -> None:
        # 活动弹窗关闭按钮
        self.recharge_invite_dialog_close_button = page.locator("//mb-recharge-invite-dialog//span[@class='--icon']")