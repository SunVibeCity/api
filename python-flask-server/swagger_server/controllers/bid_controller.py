import connexion
import six

from swagger_server.models.bid import Bid  # noqa: E501
from swagger_server.models.error_model import ErrorModel  # noqa: E501
from swagger_server.models.new_bid import NewBid  # noqa: E501
from swagger_server import util


def add_bid(body):  # noqa: E501
    """Add a new bid to the market

    Add token buying offering # noqa: E501

    :param body: Bid object that needs to be added to the market
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewBid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_bid(id):  # noqa: E501
    """delete_bid

    deletes a single bet based on the ID supplied # noqa: E501

    :param id: ID of bid to delete
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_bid_by_id(id):  # noqa: E501
    """get_bid_by_id

    Returns a user based on a single ID, if the user does not have access to the pet # noqa: E501

    :param id: ID of bid to fetch
    :type id: int

    :rtype: Bid
    """
    return 'do some magic!'


def list_bids(status=None):  # noqa: E501
    """List Bids

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Bid]
    """
    return 'do some magic!'


def update_bid(id, body):  # noqa: E501
    """Update an existing bid

     # noqa: E501

    :param id: ID of bid to fetch
    :type id: int
    :param body: Bid object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Bid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
