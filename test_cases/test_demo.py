import pytest

from playwright.sync_api import Page




@pytest.mark.skip
def test_create_wallet(page: Page) -> None:
    page.goto("http://127.0.0.1:7665/")
    page.get_by_role("button", name="创建钱包").click()
    page.get_by_placeholder("输入1~12个字符").click()
    page.get_by_placeholder("输入1~12个字符").fill("1")
    page.get_by_placeholder("密码至少8个字符").click()
    page.get_by_placeholder("密码至少8个字符").fill("11111111")
    page.get_by_placeholder("确认密码").click()
    page.get_by_placeholder("确认密码").fill("11111111")
    page.get_by_placeholder("输入密码提示信息").click()
    page.get_by_placeholder("输入密码提示信息").fill("11111111")
    page.get_by_label("我已阅读并同意 《用户协议》").check()
    page.get_by_role("button", name="创建钱包").click()
    page.get_by_role("button", name="立即备份助记词").click()
    page.get_by_role("button", name="复制助记词").click()
    page.get_by_role("button", name="确认已备份").click()
    page.get_by_role("button", name="确定").click()
    page.get_by_role("button", name="完成").click()
    page.get_by_role("button", name="").click()

@pytest.mark.skip
def test_restore_wallet(page:Page):
    page.goto("http://127.0.0.1:7665/")
    page.get_by_role("button", name="恢复钱包").click()
    page.get_by_placeholder("输入助记词，各单词间以空格分隔").click()
    page.get_by_placeholder("输入助记词，各单词间以空格分隔").fill("front cushion afford loud hungry upset rich table delay steel margin lucky")
    page.get_by_placeholder("输入1~12个字符").click()
    page.get_by_placeholder("输入1~12个字符").fill("1")
    page.get_by_placeholder("密码至少8个字符").click()
    page.get_by_placeholder("密码至少8个字符").fill("11111111")
    page.get_by_placeholder("确认密码").click()
    page.get_by_placeholder("确认密码").fill("11111111")
    page.get_by_placeholder("输入密码提示信息").click()
    page.get_by_placeholder("输入密码提示信息").fill("11111111")
    page.get_by_label("我已阅读并同意 《用户协议》").check()
    page.get_by_role("button", name="恢复身份").click()
    page.get_by_role("button", name="").click()