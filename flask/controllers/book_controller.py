import connexion
from connexion import NoContent
from orm import get_db, Book


def add_entry(body):  
    """
    Enter a new entry to the book
    Add token buying offering 
    :param body: Book entry object that needs to be added to the book
    :type body: dict | bytes
    :rtype: None
    """
    try:
        if connexion.request.is_json:
            get_db().add(Book(**body))
            get_db().commit()
            return NoContent, 201
        return NoContent, 400
    except Exception as e:
        return {'message': str(e)}, 500


def del_entry(id):  
    """del_entry
    Deletes a single book entry based on the ID supplied 
    :param id: ID of the object to fetch
    :type id: int
    :rtype: None
    """
    try:
        entry = get_db().query(Book).filter(Book.id == id).one_or_none()
        if entry is not None:
            get_db().query(Book).filter(Book.id == id).delete()
            get_db().commit()
            return NoContent, 204
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500


def get_entry(id):  
    """get_entry
    Returns an entry from the book based on a single ID 
    :param id: ID of the object to fetch
    :type id: int
    :rtype: Book
    """
    try:
        entry = get_db().query(Book).filter(Book.id == id).one_or_none()
        return entry.dump() if entry is not None else ('Not found', 404)
    except Exception as e:
        return {'message': str(e)}, 500


def list_entries(symbol=None, owner=None, offset=None, limit=None):  
    """Lists the Book
    Lists entries from the book, and tells who own how many shares 
    :param symbol: Symbol as a filter
    :type symbol: str
    :param owner: Owner id as a filter
    :type owner: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :rtype: List[Book]
    """
    try:
        q = get_db().query(Book)
        if symbol is not None:
            q = q.filter(Book.symbol == symbol)
        q = q.limit(limit).offset(offset)
        return [e.dump() for e in q]
    except Exception as e:
        return {'message': str(e)}, 500


def update_entry(id, body):  
    """
    Update an existing entry of the book
    :param id: ID of the object to fetch
    :type id: int
    :param body: Book entry object that needs to be modified
    :type body: dict | bytes
    :rtype: None
    """
    try:
        entry = get_db().query(Book).filter(Book.id == id).one_or_none()
        if entry is not None:
            if connexion.request.is_json:
                entry.update(**body)
                get_db().commit()
                return NoContent, 204
            return NoContent, 400
        else:
            return NoContent, 404
    except Exception as e:
        return {'message': str(e)}, 500
