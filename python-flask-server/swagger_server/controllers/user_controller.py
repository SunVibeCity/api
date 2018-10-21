import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.login_user import LoginUser  # noqa: E501
from swagger_server.models.new_user import NewUser  # noqa: E501
from swagger_server.models.unexpected_error import UnexpectedError  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(body):  # noqa: E501
    """Creates a new user

    Only the admin user can create users. # noqa: E501

    :param body: The user account to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_user(id):  # noqa: E501
    """Deletes a user

    Users can only delete their own account, admin can delete everyone else. # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_user(id):  # noqa: E501
    """Retrieves a user

    Users can only retrieve their own account, except for the admin, who can retrieve anyone. # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def list_users(offset=None, limit=None):  # noqa: E501
    """Returns all users in the database.

    Only the admin can access this. # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int

    :rtype: List[User]
    """
    return 'do some magic!'


def update_user(id, body):  # noqa: E501
    """Update a user

    Users can only update their own account, except the admin, who can edit anyone. # noqa: E501

    :param id: ID of the object to fetch
    :type id: int
    :param body: The user account to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_login(body):  # noqa: E501
    """Logs in already registered users and admin

     # noqa: E501

    :param body: The login credentials
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = LoginUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_logout(id):  # noqa: E501
    """Logs out the given user

    Users can only log themselves out, admin can log-out anyone. # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: None
    """
    return 'do some magic!'
