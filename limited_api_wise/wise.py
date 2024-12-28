"""This contains adaptations for the Wise API."""

from datetime import datetime
import pywisetransfer
from dataclasses import dataclass
from iso4217 import Currency


@dataclass
class Transfer:
    """A transaction that adds or removed money from a sub-account.

    This limits the data that is exposed.
    """

    currency: Currency
    amount: float
    date: datetime
    reference: str


class Wise:
    """Wrapper for pywisetransfer."""

    def __init__(self, client: pywisetransfer.Client):
        """Create a new Wise wrapper."""
        self._client = client

    @property
    def transfers(self) -> list[Transfer]:
        """Return all transactions."""

    @property
    def profiles(self):
        """Return all profiles."""
        return self._client.profiles.list()

__all__ = ["Wise"]
