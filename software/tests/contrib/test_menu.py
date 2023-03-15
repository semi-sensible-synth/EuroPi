import sys
import pytest
import utime
from contrib.menu import EUROPI_SCRIPTS
from bootloader import BootloaderMenu


@pytest.fixture
def mock_time_module(monkeypatch):
    """the time module isn't as easily mocked as the utime module is,
    but we can just swap it out for our mock for this test"""
    monkeypatch.setitem(sys.modules, "time", utime)


def test_menu_imports(mock_time_module):
    """User the bootloader code to test that every script declared in EUROPI_SCRIPTS can be imported."""
    bootloader = BootloaderMenu(EUROPI_SCRIPTS)
    classes = bootloader.load_script_classes(bootloader.scripts)
    assert EUROPI_SCRIPTS == list(classes.keys()), "Some EUROPI_SCRIPTs were not able to be loaded."