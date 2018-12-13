import os
import os.path
import sqlite3
from swagger_server.utils.sv_io import print_stderr

_db = None
_new = False


def create_tables(conn):
    """ create a tables
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT,
            name TEXT,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            admin INTEGER CHECK( admin IN (0,1) ) NOT NULL DEFAULT 0,
            investor INTEGER CHECK( investor IN (0,1) ) NOT NULL DEFAULT 0,
            created INTEGER NOT NULL DEFAULT (strftime('%s','now')),
            updated INTEGER NOT NULL DEFAULT (strftime('%s','now'))
        );
        """)
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS bids (
            id INTEGER PRIMARY KEY,
            quantity INTEGER NOT NULL,
            price INTEGER NOT NULL,
            bidder INTEGER NOT NULL,
            status INTEGER CHECK( status IN (0,1) ) NOT NULL DEFAULT 1,
            created INTEGER NOT NULL DEFAULT (strftime('%s','now')),
            updated INTEGER NOT NULL DEFAULT (strftime('%s','now')),
            FOREIGN KEY (bidder) REFERENCES users (id)
        );   
        """)
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS asks (
            id INTEGER PRIMARY KEY,
            quantity INTEGER NOT NULL,
            price INTEGER NOT NULL,
            bidder INTEGER NOT NULL,
            status INTEGER CHECK( status IN (0,1) ) NOT NULL DEFAULT 1,
            created INTEGER NOT NULL DEFAULT (strftime('%s','now')),
            updated INTEGER NOT NULL DEFAULT (strftime('%s','now')),
            FOREIGN KEY (bidder) REFERENCES users (id)
        );
        """)
    conn.commit()


def create_connection(sqlite3_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param sqlite3_file: database file provided in ENV
    :return: Connection object or None
    """
    global _new

    _new = not os.path.isfile(sqlite3_file)
    conn = sqlite3.connect(sqlite3_file)
    if _new:
        print_stderr("Database {} is missing. New one will be created.".format(sqlite3_file))
        create_tables(conn)
    return conn


def get_db():
    global _db
    if not _db:
        sqlite3_file = os.environ.get("SQLITE3_FILE", default="sunvibe.sqlite3")
        _db = create_connection(sqlite3_file)
    return _db
