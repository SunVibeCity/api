import connexion
import six

from swagger_server.models.ask import Ask  # noqa: E501
from swagger_server.models.error_model import ErrorModel  # noqa: E501
from swagger_server.models.new_ask import NewAsk  # noqa: E501
from swagger_server import util


def add_ask(body):  # noqa: E501
    """Add a new ask to the market

    Add token buying offering # noqa: E501

    :param body: Ask object that needs to be added to the market
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewAsk.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_ask(id):  # noqa: E501
    """del_ask

    deletes a single bet based on the ID supplied # noqa: E501

    :param id: ID of ask to delete
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def fok_ask(body):  # noqa: E501
    """Fill or kill asks

    Only accept existing ask - selling request # noqa: E501

    :param body: Ask object that needs to be added to the market
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewAsk.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_ask(id):  # noqa: E501
    """get_ask

    Returns a user based on a single ID, if the user does not have access to the pet # noqa: E501

    :param id: ID of ask to fetch
    :type id: int

    :rtype: Ask
    """
    return 'do some magic!'


def list_asks(status=None):  # noqa: E501
    """List Asks

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Ask]
    """
    return 'do some magic!'


def update_ask(id, body):  # noqa: E501
    """Update an existing ask

     # noqa: E501

    :param id: ID of ask to fetch
    :type id: int
    :param body: Ask object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Ask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
