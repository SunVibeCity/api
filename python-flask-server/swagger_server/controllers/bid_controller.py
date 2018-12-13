import connexion
import six

import swagger_server.utils.orm
from swagger_server import util
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def add_bid(body):  # noqa: E501
    """Add a new bid to the market

    Add a token buying offer to the marketplace.  # noqa: E501

    :param body: Bid object that needs to be added to the market quantity is the amount of token and price is VND price of one token
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # body = NewBid.from_dict(connexion.request.get_json())  # noqa: E501
        pass
    return 'do some magic!'


def del_bid(id):  # noqa: E501
    """Deletes and existing bid

    Deletes a single bet based on the ID supplied # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def fok_bid(body):  # noqa: E501
    """Fill or kill bids

    Only accept existing ask - selling request # noqa: E501

    :param body: Bid object that needs to be added to the market
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # body = NewBid.from_dict(connexion.request.get_json())  # noqa: E501
        pass
    return 'do some magic!'


def get_bid(id):  # noqa: E501
    """Get bid details by ID

    Returns a bid based on a single ID # noqa: E501

    :param id: ID of the object to fetch
    :type id: int

    :rtype: Bid
    """
    return 'do some magic!'


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
    return 'do some magic!'


def update_bid(id, body):  # noqa: E501
    """Update an existing bid

    Modify bid status only # noqa: E501

    :param id: ID of the object to fetch
    :type id: int
    :param body: Bid object that needs to be modified
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # body = Bid.from_dict(connexion.request.get_json())  # noqa: E501
        pass
    return 'do some magic!'
