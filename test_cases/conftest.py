from typing import Generator
import pytest
import allure
from playwright.sync_api import Page, expect
from config import config
from utils._playwright import PlayWright
from page.login.login_page import LoginPage
from page.create_wallet import (
    CreateWalletPage,
    BackupOrNotWalletPage,
    BackupMnemonicPage,
    ConfirmMnemonicPage,
)
from page.restore_wallet.restore_wallet_page import RestoreWalletPage
from page.home.home_page import HomePage
from page.transfer.transfer_page import TransferPage
from page.asset_detail.asset_detail_list_page import AssetDetailListPage
from page.transfer.select_asset_page import SelectAssetPage


@pytest.fixture
def restore_wallet(
    cpage: PlayWright,
    login_page: LoginPage,
    restore_wallet_page: RestoreWalletPage,
):
    """前置，恢复钱包

    Args:
        cpage (PlayWright): _description_
        login_page (LoginPage): _description_
        restore_wallet_page (RestoreWalletPage): _description_
    """
    cpage.goto(config.TEST_URL)
    login_page.click_restore_wallet_button()
    restore_wallet_page.input_wallet_mnemonic(config.TEST_MNEMONIC)
    restore_wallet_page.input_wallet_name(config.TEST_WALLET_NAME)
    restore_wallet_page.input_wallet_pwd(config.TEST_WALLET_PWD)
    restore_wallet_page.input_wallet_confirm_pwd(config.TEST_WALLET_PWD)
    restore_wallet_page.input_wallet_pwd_hint(config.TEST_WALLET_PWD)
    restore_wallet_page.click_user_agreement_checkbox()
    restore_wallet_page.click_restore_wallet_submit_button()


@pytest.fixture
def create_wallet(
    cpage: PlayWright,
    login_page: LoginPage,
    create_wallet_page: CreateWalletPage,
    backup_or_not_wallet_page: BackupOrNotWalletPage,
):
    """前置，创建钱包

    Args:
        cpage (PlayWright): _description_
        login_page (LoginPage): _description_
        create_wallet_page (CreateWalletPage): _description_
        backup_or_not_wallet_page (BackupOrNotWalletPage): _description_
    """
    cpage.goto(config.TEST_URL)
    login_page.click_create_wallet_button()
    create_wallet_page.input_wallet_name(config.TEST_WALLET_NAME)
    create_wallet_page.input_wallet_pwd(config.TEST_WALLET_PWD)
    create_wallet_page.input_wallet_confirm_pwd(config.TEST_WALLET_PWD)
    create_wallet_page.input_wallet_pwd_hint(config.TEST_WALLET_PWD)
    create_wallet_page.click_user_agreement_checkbox()
    create_wallet_page.click_create_wallet_submit_button()
    backup_or_not_wallet_page.click_skip_backup_mnemonic_button()
    backup_or_not_wallet_page.click_backup_abort_button()
    # 断言首页元素可见
    expect(home_page.recharge_invite_dialog_close_button).to_be_visible()


@pytest.fixture
def cpage(page: Page) -> PlayWright:
    """返回封装后的playwright对象

    Returns:
        PlayWright: _description_

    Yields:
        Iterator[PlayWright]: _description_
    """
    cpage = PlayWright(page)
    yield cpage


@pytest.fixture
def login_page(page: Page) -> Generator[LoginPage, None, None]:
    """登录页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[LoginPage]: _description_
    """
    login_page = LoginPage(page)
    yield login_page


@pytest.fixture
def create_wallet_page(page: Page) -> Generator[CreateWalletPage, None, None]:
    """创建钱包页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[CreateWalletPage]: _description_
    """
    create_wallet_page = CreateWalletPage(page)
    yield create_wallet_page


@pytest.fixture
def restore_wallet_page(page: Page) -> Generator[RestoreWalletPage, None, None]:
    """恢复钱包页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[RestoreWalletPage]: _description_
    """
    restore_wallet_page = RestoreWalletPage(page)
    yield restore_wallet_page


@pytest.fixture
def backup_or_not_wallet_page(
    page: Page,
) -> Generator[BackupOrNotWalletPage, None, None]:
    """是否备份页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[BackupOrNotWalletPage]: _description_
    """
    backup_or_not_wallet_page = BackupOrNotWalletPage(page)
    yield backup_or_not_wallet_page


@pytest.fixture
def backup_mnemonic_page(page: Page) -> Generator[BackupMnemonicPage, None, None]:
    """备份助记词页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[BackupMnemonicPage]: _description_
    """
    backup_mnemonic_page = BackupMnemonicPage(page)
    yield backup_mnemonic_page


@pytest.fixture
def confirm_mnemonic_page(page: Page) -> Generator[ConfirmMnemonicPage, None, None]:
    """确认助记词页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[ConfirmMnemonicPage]: _description_
    """
    confirm_mnemonic_page = ConfirmMnemonicPage(page)
    yield confirm_mnemonic_page


@pytest.fixture
def home_page(page: Page) -> Generator[HomePage, None, None]:
    """首页模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[HomePage]: _description_
    """
    home_page = HomePage(page)
    yield home_page


@pytest.fixture
def transfer_page(page: Page) -> Generator[TransferPage, None, None]:
    """转账页面模型实例

    Args:
        page (Page): _description_

    Yields:
        Generator[TransferPage, None, None]: _description_
    """
    transfer_page = TransferPage(page)
    yield transfer_page


@pytest.fixture
def asset_detail_list_page(page: Page) -> Generator[AssetDetailListPage, None, None]:
    """资产详情列表页面

    Args:
        page (Page): _description_

    Yields:
        Generator[AssetDetailListPage, None, None]: _description_
    """
    asset_detail_list_page = AssetDetailListPage(page)
    yield asset_detail_list_page


@pytest.fixture
def select_asset_page(page: Page) -> Generator[SelectAssetPage, None, None]:
    """选择币种页面实例

    Args:
        page (Page): _description_

    Yields:
        Generator[SelectAssetPage, None, None]: _description_
    """
    select_asset_page = SelectAssetPage(page)
    yield select_asset_page
