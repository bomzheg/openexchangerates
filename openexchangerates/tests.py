import os
from datetime import date
from decimal import Decimal

import pytest

from openexchangerates.client import OpenExchangeRatesClient


TEST_API_KEY = os.getenv("TEST_API_KEY")

_FIXTURE_CURRENCIES = {
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
}

_FIXTURE_HISTORICAL = {
    "disclaimer": "<Disclaimer data>",
    "license": "<License data>",
    "timestamp": 1358150409,
    "base": "USD",
    "rates": {
        "AED": Decimal(3.672941),
        "AFN": Decimal(51.374266),
        "ALL": Decimal(104.3625),
    },
}


@pytest.mark.asyncio
async def test_historical():
    """Tests OpenExchangeRateClient.historical"""
    float_eq = 0.0001
    async with OpenExchangeRatesClient(TEST_API_KEY) as client:
        day = date.fromtimestamp(_FIXTURE_HISTORICAL['timestamp'])
        historical = await client.historical(day)
        rates = historical['rates']
        assert (rates['AED'] - _FIXTURE_HISTORICAL['rates']['AED']) < float_eq
        assert (rates['AFN'] == _FIXTURE_HISTORICAL['rates']['AFN']) < float_eq
        assert (rates['ALL'] == _FIXTURE_HISTORICAL['rates']['ALL']) < float_eq

@pytest.mark.asyncio
async def test_currencies():
    """Tests OpenExchangeRateClient.currencies"""
    async with OpenExchangeRatesClient(TEST_API_KEY) as client:
        currencies = await client.currencies()
        assert 'AED' in currencies
        assert 'AFN' in currencies
        assert 'ALL' in currencies


@pytest.mark.asyncio
async def test_latest():
    """Tests OpenExchangeRateClient.latest``"""
    async with OpenExchangeRatesClient(TEST_API_KEY) as client:
        latest = await client.latest()
        rates = latest['rates']
        assert 'AED' in rates
        assert 'AFN' in rates
        assert 'ALL' in rates
