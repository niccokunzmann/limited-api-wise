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
    value: float
    date: datetime
    reference: str


class Wise:
    """Wrapper for pywisetransfer.

    request_no_of_transfers - the number of transfers to request at the same time.
    """

    request_no_of_transfers: int = 100

    def __init__(self, client: pywisetransfer.Client, profile_id: int):
        """Create a new Wise wrapper."""
        self._client = client
        self._profile_id = profile_id

    @property
    def transfers(self) -> list[Transfer]:
        """Return all transactions."""
        wise_transfers = self._client.transfers.list(
            self._profile_id, offset=0, limit=self.request_no_of_transfers
        )
        return [
            Transfer(
                Currency(str(wise_transfer.targetCurrency)),
                wise_transfer.targetValue,
                datetime.strptime(wise_transfer.created, "%Y-%m-%d %H:%M:%S"),
                wise_transfer.reference,
            )
            for wise_transfer in wise_transfers
        ]

    @property
    def profiles(self):
        """Return all profiles."""
        return self._client.profiles.list()


__all__ = ["Wise"]
