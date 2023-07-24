"""playwright封装工具包"""

import allure
from playwright.sync_api import Page


class PlayWright(Page):
    """对playwright实现二次封装

    Args:
        Page (_type_): _description_
    """
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self,url:str,**kwargs):
        """封装重写跳转页面

        Args:
            url (str): 目标地址
        """
        # 添加allure step
        with allure.step(f"goto：{url}"):
            goto = self.page.goto(url,**kwargs)
        return goto