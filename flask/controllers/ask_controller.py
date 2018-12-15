import connexion
from connexion import NoContent
from orm import get_db, Ask


def add_ask(body):
    """
    Add a new ask to the market
    Add token buying offering
    :param body: Ask object that needs to be added to the market
    :type body: dict | bytes
    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(Ask(**body))
            get_db().commit()
            return NoContent, 201
        return NoContent, 400
    except Exception as e:
        return {'message': str(e)}, 500


def del_ask(id):
    """
    Deletes and existing ask
    Deletes a single bet based on the ID supplied
    :param id: ID of the object to fetch
    :type id: int
    :rtype: None
    """
    try:
        ask = get_db().query(Ask).filter(Ask.id == id).one_or_none()
        if ask is not None:
            get_db().query(Ask).filter(Ask.id == id).delete()
            get_db().commit()
            return NoContent, 204
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def fok_ask(body):
    """
    Fill or kill asks
    Only accept existing ask - selling request
    :param body: Ask object that needs to be added to the market
    :type body: dict | bytes
    :rtype: None
    """
    try:
        raise NotImplementedError('Not Implemented')
    except Exception as e:
        return {'message': str(e)}, 500


def get_ask(id):
    """
    Get ask details by ID
    Returns a user based on a single ID
    :param id: ID of the object to fetch
    :type id: int
    :rtype: Ask
    """
    try:
        ask = get_db().query(Ask).filter(Ask.id == id).one_or_none()
        return ask.dump() if ask is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_asks(active=None, symbol=None, offset=None, limit=None):
    """
    Lists Asks
    Lists of selling offers in the marketplace
    :param active: Active status. Available for sell or not anymore
    :type active: bool
    :param symbol: Company or share symbol
    :type symbol: str
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :rtype: List[Ask]
    """
    try:
        q = get_db().query(Ask)
        if active is not None:
            q = q.filter(Ask.active == active)
        if symbol is not None:
            q = q.filter(Ask.symbol == symbol)
        q = q.limit(limit).offset(offset)
        return [a.dump() for a in q]
    except Exception as e:
        return {'message': str(e)}, 500


def update_ask(id, body):
    """
    Update an existing ask
    Modify bid status only
    :param id: ID of the object to fetch
    :type id: int
    :param body: Ask object that needs to be added to the marketplace
    :type body: dict | bytes
    :rtype: None
    """
    try:
        ask = get_db().query(Ask).filter(Ask.id == id).one_or_none()
        if ask is not None:
            if connexion.request.is_json:
                ask.update(**body)
                get_db().commit()
                return NoContent, 204
            return NoContent, 400
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500
