import connexion
from connexion import NoContent
from orm import get_db, Bid


def add_bid(body):  # noqa: E501
    """Add a new bid to the market

    Add a token buying offer to the marketplace.  # noqa: E501

    :param body: Bid object that needs to be added to the market quantity is the amount of token and price is VND price of one token
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(Bid(**body))
            get_db().commit()
            return NoContent, 201
        return NoContent, 400
    except Exception as e:
        return {'message': str(e)}, 500


def del_bid(id):  # noqa: E501
    """Deletes and existing bid

    Deletes a single bet based on the ID supplied # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: None
    """
    try:
        bid = get_db().query(Bid).filter(Bid.id == id).one_or_none()
        if bid is not None:
            get_db().query(Bid).filter(Bid.id == id).delete()
            get_db().commit()
            return NoContent, 204
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def fok_bid(body):  # noqa: E501
    """Fill or kill bids

    Only accept existing ask - selling request # noqa: E501

    :param body: Bid object that needs to be added to the market
    :type body: dict | bytes

    :rtype: None
    """
    try:
        raise NotImplementedError('Not Implemented')
    except Exception as e:
        return {'message': str(e)}, 500


def get_bid(id):  # noqa: E501
    """Get bid details by ID

    Returns a bid based on a single ID # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: Bid
    """
    try:
        bid = get_db().query(Bid).filter(Bid.id == id).one_or_none()
        return bid.dump() if bid is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_bids(status=None, offset=None, limit=None):  # noqa: E501
    """List Bids

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int

    :rtype: List[Bid]
    """
    try:
        q = get_db().query(Bid)
        if status:
            db_status = status == 'available'
            q = q.filter(status == db_status)
        q = q.limit(limit).offset(offset)
        return [u.dump() for u in q]
    except Exception as e:
        return {'message': str(e)}, 500


def update_bid(id, body):  # noqa: E501
    """Update an existing bid

    Modify bid status only # noqa: E501

    :param id: ID of the object to fetch
    :type id: int
    :param body: Bid object that needs to be modified
    :type body: dict | bytes

    :rtype: None
    """
    try:
        bid = get_db().query(Bid).filter(Bid.id == id).one_or_none()
        if bid is not None:
            if connexion.request.is_json:
                bid.update(**body)
                get_db().commit()
                return NoContent, 204
            return NoContent, 400
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500
