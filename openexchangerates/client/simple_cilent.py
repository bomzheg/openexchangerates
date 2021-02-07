from datetime import date
from decimal import Decimal
from functools import partial
from typing import Dict, Union

from .client import OpenExchangeRatesClient
from openexchangerates.exceptions import OpenExchangeRatesClientException
from openexchangerates.current_json import json


loads = partial(json.loads, parse_int=Decimal, parse_float=Decimal)


class SimpleOpenExchangeRatesClient(OpenExchangeRatesClient):
    """This class is a client implementation for openexchangerate.org service

    """

    async def currencies(self) -> Dict[str, str]:
        """Fetches current currency data of the service

        :Example Data:

        {
            AED: "United Arab Emirates Dirham",
            AFN: "Afghan Afghani",
            ALL: "Albanian Lek",
            AMD: "Armenian Dram",
            ANG: "Netherlands Antillean Guilder",
            AOA: "Angolan Kwanza",
            ARS: "Argentine Peso",
            AUD: "Australian Dollar",
            AWG: "Aruban Florin",
            AZN: "Azerbaijani Manat"
            ...
        }
        """
        async with self.session.get(
                self.ENDPOINT_CURRENCIES,
                params={'app_id': self.api_key}
        ) as response:
            result = await response.json(loads=json.loads)
            if not response.ok:
                raise OpenExchangeRatesClientException(result)
            return result

    async def historical(self, day: date, base: str = 'USD') -> Dict[str, Union[str, int, Dict[str, Decimal]]]:
        """Fetches historical exchange rate data from service

        :Example Data:
            {
                disclaimer: "<Disclaimer data>",
                license: "<License data>",
                timestamp: 1358150409,
                base: "USD",
                rates: {
                    AED: 3.666311,
                    AFN: 51.2281,
                    ALL: 104.748751,
                    AMD: 406.919999,
                    ANG: 1.7831,
                    ...
                }
            }
        """
        async with self.session.get(
            self.ENDPOINT_HISTORICAL.format(day.strftime("%Y-%m-%d")),
            params={'base': base, 'app_id': self.api_key}
        ) as response:
            result_json = await response.json(loads=loads)
            if not response.ok:
                raise OpenExchangeRatesClientException(result_json)
            return result_json
