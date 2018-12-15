import connexion
from connexion import NoContent
from orm import get_db, Wallet


def add_wallet(body):  
    """
    Add a new wallet and associates it with the owner 
    :param body: Wallet object that needs to be inserted
    :type body: dict | bytes
    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(Wallet(**body))
            get_db().commit()
            return NoContent, 201
        return NoContent, 400
    except Exception as e:
        return {'message': str(e)}, 500


def del_wallet(id):  
    """
    Deletes a wallet based on the ID supplied 
    :param id: ID of the object to fetch
    :type id: int
    :rtype: None
    """
    try:
        wallet = get_db().query(Wallet).filter(Wallet.id == id).one_or_none()
        if wallet is not None:
            get_db().query(Wallet).filter(Wallet.id == id).delete()
            get_db().commit()
            return NoContent, 204
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def get_wallet(id):  
    """
    Returns a wallet info based on a single ID 
    :param id: ID of the object to fetch
    :type id: int
    :rtype: Wallet
    """
    try:
        wallet = get_db().query(Wallet).filter(Wallet.id == id).one_or_none()
        return wallet.dump() if wallet is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_wallets(owner=None, offset=None, limit=None):  
    """
    Lists wallets
    List of wallets of the users  
    :param owner: Owner id as a filter
    :type owner: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :rtype: List[Wallet]
    """
    try:
        q = get_db().query(Wallet)
        if owner is not None:
            q = q.filter(Wallet.owner == owner)
        q = q.limit(limit).offset(offset)
        return [w.dump() for w in q]
    except Exception as e:
        return {'message': str(e)}, 500


def update_wallet(id, body):  
    """
    Update an existing wallet
    :param id: ID of the object to fetch
    :type id: int
    :param body: Wallet that needs to be modified
    :type body: dict | bytes
    :rtype: None
    """
    try:
        wallet = get_db().query(Wallet).filter(Wallet.id == id).one_or_none()
        if wallet is not None:
            if connexion.request.is_json:
                wallet.update(**body)
                get_db().commit()
                return NoContent, 204
            return NoContent, 400
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500
