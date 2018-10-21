# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.login_user import LoginUser  # noqa: E501
from swagger_server.models.new_user import NewUser  # noqa: E501
from swagger_server.models.unexpected_error import UnexpectedError  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        Creates a new user
        """
        body = NewUser()
        response = self.client.open(
            '/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_user(self):
        """Test case for del_user

        Deletes a user
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Retrieves a user
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_users(self):
        """Test case for list_users

        Returns all users in the database.
        """
        query_string = [('offset', 1),
                        ('limit', 1000)]
        response = self.client.open(
            '/v1/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update a user
        """
        body = User()
        response = self.client.open(
            '/v1/users/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_login(self):
        """Test case for user_login

        Logs in already registered users and admin
        """
        body = LoginUser()
        response = self.client.open(
            '/v1/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_logout(self):
        """Test case for user_logout

        Logs out the given user
        """
        response = self.client.open(
            '/v1/users/{id}/logout'.format(id=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
