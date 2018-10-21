# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bid import Bid  # noqa: E501
from swagger_server.models.new_bid import NewBid  # noqa: E501
from swagger_server.models.unexpected_error import UnexpectedError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBidController(BaseTestCase):
    """BidController integration test stubs"""

    def test_add_bid(self):
        """Test case for add_bid

        Add a new bid to the market
        """
        body = NewBid()
        response = self.client.open(
            '/v1/bids',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_bid(self):
        """Test case for del_bid

        Deletes and existing bid
        """
        response = self.client.open(
            '/v1/bids/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fok_bid(self):
        """Test case for fok_bid

        Fill or kill bids
        """
        body = NewBid()
        response = self.client.open(
            '/v1/fok-bids',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bid(self):
        """Test case for get_bid

        Get bid details by ID
        """
        response = self.client.open(
            '/v1/bids/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_bids(self):
        """Test case for list_bids

        List Bids
        """
        query_string = [('status', 'available'),
                        ('offset', 1),
                        ('limit', 1000)]
        response = self.client.open(
            '/v1/bids',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_bid(self):
        """Test case for update_bid

        Update an existing bid
        """
        body = Bid()
        response = self.client.open(
            '/v1/bids/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
