import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    """设置浏览器大小，模拟设置"""
    return {**playwright.devices["Galaxy S9+"]}