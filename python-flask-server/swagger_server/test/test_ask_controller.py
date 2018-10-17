# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ask import Ask  # noqa: E501
from swagger_server.models.error_model import ErrorModel  # noqa: E501
from swagger_server.models.new_ask import NewAsk  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAskController(BaseTestCase):
    """AskController integration test stubs"""

    def test_add_ask(self):
        """Test case for add_ask

        Add a new ask to the market
        """
        body = NewAsk()
        response = self.client.open(
            '/v1/asks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_ask(self):
        """Test case for del_ask

        
        """
        response = self.client.open(
            '/v1/asks/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fok_ask(self):
        """Test case for fok_ask

        Fill or kill asks
        """
        body = NewAsk()
        response = self.client.open(
            '/v1/fok-asks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ask(self):
        """Test case for get_ask

        
        """
        response = self.client.open(
            '/v1/asks/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_asks(self):
        """Test case for list_asks

        List Asks
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/v1/asks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_ask(self):
        """Test case for update_ask

        Update an existing ask
        """
        body = Ask()
        response = self.client.open(
            '/v1/asks/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
