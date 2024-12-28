"""Test the wise API wrapper."""


def test_no_transactions(wise, transfers):
    """Check that by default, we do not see transactions."""
    assert wise.transfers == []


def add_a_transfer_and_it_turns_up(wise, transfers):
    """We add a transfer and see if it is there."""
    transfers.add("EUR", 1, "2022-01-01", "test")
