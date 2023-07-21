from typing import Generator
import pytest
from playwright.sync_api import Page
from page.login.login_page import LoginPage
from page.create_wallet import (
    CreateWalletPage,
    BackupOrNotWalletPage,
    BackupMnemonicPage,
    ConfirmMnemonicPage,
)
from page.restore_wallet.restore_wallet_page import RestoreWalletPage
from page.home.home_page import HomePage

@pytest.fixture
def login_page(page:Page) -> Generator[LoginPage, None, None]:
    """登录页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[LoginPage]: _description_
    """
    login_page = LoginPage(page)
    yield login_page

@pytest.fixture
def create_wallet_page(page:Page) -> Generator[CreateWalletPage, None, None]:
    """创建钱包页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[CreateWalletPage]: _description_
    """
    create_wallet_page = CreateWalletPage(page)
    yield create_wallet_page
    
@pytest.fixture
def restore_wallet_page(page:Page)->Generator[RestoreWalletPage, None, None]:
    """恢复钱包页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[RestoreWalletPage]: _description_
    """
    restore_wallet_page = RestoreWalletPage(page)
    yield restore_wallet_page

@pytest.fixture
def backup_or_not_wallet_page(page:Page) -> Generator[BackupOrNotWalletPage, None, None]:
    """是否备份页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[BackupOrNotWalletPage]: _description_
    """
    backup_or_not_wallet_page = BackupOrNotWalletPage(page)
    yield backup_or_not_wallet_page

@pytest.fixture
def backup_mnemonic_page(page:Page) -> Generator[BackupMnemonicPage, None, None]:
    """备份助记词页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[BackupMnemonicPage]: _description_
    """
    backup_mnemonic_page = BackupMnemonicPage(page)
    yield backup_mnemonic_page

@pytest.fixture
def confirm_mnemonic_page(page:Page) -> Generator[ConfirmMnemonicPage, None, None]:
    """确认助记词页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[ConfirmMnemonicPage]: _description_
    """
    confirm_mnemonic_page = ConfirmMnemonicPage(page)
    yield confirm_mnemonic_page

@pytest.fixture
def home_page(page:Page) -> Generator[HomePage, None, None]:
    """首页模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[HomePage]: _description_
    """
    home_page = HomePage(page)
    yield home_page



@pytest.fixture
def restore_wallet(page: Page):
    """恢复钱包"""
    pass


@pytest.fixture
def create_wallet(page:Page):
    """创建钱包"""
    pass
