import connexion
from connexion import NoContent
import six
import json

from swagger_server.utils.orm import get_db, User
from swagger_server import util


def add_user(body):  # noqa: E501
    """Creates a new user

    Only the admin user can create users. # noqa: E501

    :param body: The user account to create
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(User(**body))
            get_db().commit()
            return NoContent, 201
        return 'do some magic!'
    except Exception as e:
        return {'message': str(e)}, 500


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
    try:
        user = get_db().query(User).filter(User.id == id).one_or_none()
        return user.dump() if user is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_users(offset=None, limit=None):  # noqa: E501
    """Returns all users in the database.

    Only the admin can access this. # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int

    :rtype: List[User]
    """
    try:
        q = get_db().query(User).limit(limit).offset(offset)
        return [u.dump() for u in q]
    except Exception as e:
        return {'message': str(e)}, 500

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
        # body = User.from_dict(connexion.request.get_json())  # noqa: E501
        pass
    return 'do some magic!'


def user_login(body):  # noqa: E501
    """Logs in already registered users and admin

     # noqa: E501

    :param body: The login credentials
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        # body = LoginUser.from_dict(connexion.request.get_json())  # noqa: E501
        pass
    return 'do some magic!'


def user_logout(id):  # noqa: E501
    """Logs out the given user

    Users can only log themselves out, admin can log-out anyone. # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: None
    """
    return 'do some magic!'
