import connexion
from connexion import NoContent
from orm import get_db, User


def add_user(body):  
    """
    Creates a new user
    Only the admin user can create users.
    :param body: The user account to create
    :type body: dict | bytes
    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(User(**body))
            get_db().commit()
            return NoContent, 201
        return NoContent, 400
    except Exception as e:
        return {'message': str(e)}, 500


def del_user(id):  
    """
    Deletes a user
    Users can only delete their own account, admin can delete everyone else.
    :param id: ID of the object to fetch
    :type id: int
    :rtype: None
    """
    try:
        user = get_db().query(User).filter(User.id == id).one_or_none()
        if user is not None:
            get_db().query(User).filter(User.id == id).delete()
            get_db().commit()
            return NoContent, 204
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def get_user(id):  
    """
    Retrieves a user
    Users can only retrieve their own account, except for the admin, who can retrieve anyone.
    :param id: ID of the object to fetch
    :type id: int
    :rtype: User
    """
    try:
        user = get_db().query(User).filter(User.id == id).one_or_none()
        return user.dump() if user is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_users(offset=None, limit=None):  
    """
    Returns all users in the database.
    Only the admin can access this.
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


def update_user(id, body):  
    """
    Update a user
    Users can only update their own account, except the admin, who can edit anyone.
    :param id: ID of the object to fetch
    :type id: int
    :param body: The user account to create
    :type body: dict | bytes
    :rtype: None
    """
    try:
        user = get_db().query(User).filter(User.id == id).one_or_none()
        if user is not None:
            if connexion.request.is_json:
                user.update(**body)
                get_db().commit()
                return NoContent, 204
            return NoContent, 400
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def user_login(body):  
    """
    Logs in already registered users and admin
    :param body: The login credentials
    :type body: dict | bytes
    :rtype: InlineResponse200
    """
    try:
        raise NotImplementedError('Not Implemented')
    except Exception as e:
        return {'message': str(e)}, 500


def user_logout(id):  
    """
    Logs out the given user
    Users can only log themselves out, admin can log-out anyone.
    :param id: ID of the object to fetch
    :type id: int
    :rtype: None
    """
    try:
        raise NotImplementedError('Not Implemented')
    except Exception as e:
        return {'message': str(e)}, 500
