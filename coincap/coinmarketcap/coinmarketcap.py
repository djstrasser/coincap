""" coinmarketcap.py: Define the API client class"""

import requests

from .fiat import Fiat

class CoinmarketCap:
    """ Provides convenient access to the CoinmarketCap API

    https://coinmarketcap.com/api/
    """
    def __init__(self):
        self.base_url = "https://api.coinmarketcap.com/v1"
        self.session = requests.Session()


    def _make_request(self, method, url, params=None):
        """ Send the HTTP request with the provided arguments.

        Args:
            method: The HTTP method (get, put, post, delete, ...)
            url: The API endpoint url
            params: Query parameters for the HTTP request

        Returns:
            requests Response object with response of HTTP request
        """
        return self.session.request(method, url, params=params)


    def ticker(self, limit=None, convert=None):
        """ Get all ticker data

        args:
            limit: limit the number of coins to get data for
            convert: also get results for specific currency

        returns:
            list of dicts containing data on each coin
        """
        url = self.base_url + "/ticker/"
        params = {}
        if limit:
            params['limit'] = limit
        if convert:
            params['convert'] = Fiat(convert).name
        return self._make_request("get", url, params=params).json()


    def ticker_specific(self, coin_id, convert=None):
        """ Get specific ticker data

        args:
            coin_id: the speicific coin id to get (ex: ethereum-classic)
            convert: also get results for specific currency

        returns:
            list of dict containing data for the specific coin
        """
        url = self.base_url + "/ticker/{}/".format(coin_id)
        params = {}
        if convert:
            params['convert'] = Fiat(convert).name
        return self._make_request("get", url, params=params).json()


    def global_data(self, convert=None):
        """ Get global coinmarketcap data

        args:
            convert: also get results for specific currency

        returns:
            a dict with the various global data
        """
        url = self.base_url + "/global/"
        params = {}
        if convert:
            params['convert'] = Fiat(convert).name
        return self._make_request("get", url, params=params).json()
