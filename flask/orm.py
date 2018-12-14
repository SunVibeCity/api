import os
import os.path
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(31), unique=True, nullable=False)
    password = Column(String(31))
    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    admin = Column(Boolean, default=False)
    investor = Column(Boolean, default=False)
    locale = Column(String(5), default='en_US')
    verified = Column(Boolean, default=False)
    blocked = Column(Boolean, default=False)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    bids = relationship("Bid", back_populates="bidder")
    asks = relationship("Ask", back_populates="investor")

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s', phone='%s', admin='%s', verified='%s', blocked='%s')>" % (
            self.id, self.username, self.email, self.phone, self.admin, self.verified, self.blocked
        )

    def update(self, **kwargs):
        if len(kwargs):
            p = ('username', 'password', 'name', 'email', 'phone', 'admin', 'investor', 'locale', 'verified', 'blocked')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Boolean, default=True)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    bidder = relationship("User", back_populates="bids")

    def __repr__(self):
        return "<Bid(id='%s', quantity='%s', price='%s', user_id='%s', status='%s')>" % (
            self.id, self.quantity, self.price, self.user_id, self.status
        )

    def update(self, **kwargs):
        if len(kwargs):
            p = ('quantity', 'price', 'bidder', 'status')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Ask(Base):
    __tablename__ = 'asks'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Boolean, default=True)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    investor = relationship("User", back_populates="asks")

    def __repr__(self):
        return "<Ask(id='%s', quantity='%s', price='%s', user_id='%s', status='%s')>" % (
            self.id, self.quantity, self.price, self.user_id, self.status
        )

    def update(self, **kwargs):
        if len(kwargs):
            p = ('quantity', 'price', 'bidder', 'status')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session


_db = None


def get_db():
    global _db
    if not _db:
        _db = init_db(os.environ.get("SQL_URL", default="sqlite:///sunvibe.db"))
    return _db
