# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NewAsk(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, quantity: int=None, price: int=None):  # noqa: E501
        """NewAsk - a model defined in Swagger

        :param quantity: The quantity of this NewAsk.  # noqa: E501
        :type quantity: int
        :param price: The price of this NewAsk.  # noqa: E501
        :type price: int
        """
        self.swagger_types = {
            'quantity': int,
            'price': int
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'price': 'price'
        }

        self._quantity = quantity
        self._price = price

    @classmethod
    def from_dict(cls, dikt) -> 'NewAsk':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewAsk of this NewAsk.  # noqa: E501
        :rtype: NewAsk
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quantity(self) -> int:
        """Gets the quantity of this NewAsk.


        :return: The quantity of this NewAsk.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this NewAsk.


        :param quantity: The quantity of this NewAsk.
        :type quantity: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def price(self) -> int:
        """Gets the price of this NewAsk.


        :return: The price of this NewAsk.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price: int):
        """Sets the price of this NewAsk.


        :param price: The price of this NewAsk.
        :type price: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price
