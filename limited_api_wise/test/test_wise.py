"""Test the wise API wrapper."""

from iso4217 import Currency
from datetime import datetime


def test_no_transactions(wise, transfers):
    """Check that by default, we do not see transactions."""
    assert wise.transfers == []


def test_add_a_transfer_and_it_turns_up(wise, transfers):
    """We add a transfer and see if it is there."""
    transfers.add_standard(1, "test")
    assert len(wise.transfers) == 1
    transfer = wise.transfers[0]
    assert transfer.currency == Currency.USD
    assert transfer.value == 1
    assert transfer.reference == "test"
    assert transfer.date == datetime(2017, 11, 24, 10, 47, 0)
