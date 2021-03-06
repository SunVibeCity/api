import os
import os.path
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
import datetime

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
    book = relationship("Book", back_populates="owner")
    wallets = relationship("Wallet", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")
    sells = relationship("Exchange", back_populates="seller", primaryjoin="Exchange.seller_id==User.id")
    purchases = relationship("Exchange", back_populates="buyer", primaryjoin="Exchange.buyer_id==User.id")

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s', phone='%s', admin='%s', verified='%s', blocked='%s')>" % (
            self.id, self.username, self.email, self.phone, self.admin, self.verified, self.blocked
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('username', 'password', 'name', 'email', 'phone', 'admin', 'investor', 'locale', 'verified', 'blocked')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), ForeignKey('companies.id'), nullable=False)
    quantity = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    active = Column(Boolean, default=True)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    bidder = relationship("User", back_populates="bids")
    company = relationship("Company", back_populates="bids")

    def __repr__(self):
        return "<Bid(id='%s', symbol='%s', quantity='%s', price='%s', user_id='%s', active='%s')>" % (
            self.id, self.symbol, self.quantity, self.price, self.user_id, self.active
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('status')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Ask(Base):
    __tablename__ = 'asks'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), ForeignKey('companies.id'), nullable=False)
    quantity = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    active = Column(Boolean, default=True)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    investor = relationship("User", back_populates="asks")
    company = relationship("Company", back_populates="asks")

    def __repr__(self):
        return "<Ask(id='%s', symbol='%s', quantity='%s', price='%s', user_id='%s', active='%s')>" % (
            self.id, self.symbol, self.quantity, self.price, self.user_id, self.active
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('status')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), ForeignKey('companies.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    owner = relationship("User", back_populates="book")
    company = relationship("Company", back_populates="book")

    def __repr__(self):
        return "<Book(id='%s', symbol='%s', quantity='%s', user_id='%s')>" % (
            self.id, self.symbol, self.quantity, self.user_id
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('quantity')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def update(self, **kwargs):
        pass

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    currency = Column(String(3), nullable=False, default='VND')
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    owner = relationship("User", back_populates="wallets")

    def __repr__(self):
        return "<Wallet(id='%s', currency='%s', amount='%s', user_id='%s')>" % (
            self.id, self.currency, self.amount, self.user_id
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('amount')
            for k, v in kwargs.items():
                if k in p:
                    self.__setattr__(k, v)

    def update(self, **kwargs):
        pass

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    currency = Column(String(3), nullable=False, default='VND')
    sent = Column(Integer, nullable=False)
    received = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String)
    tags = Column(String)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return "<Transaction(id='%s', currency='%s', sent='%s', received='%s', user_id='%s', description='%s')>" % (
            self.id, self.currency, self.sent, self.received, self.user_id, self.description
        )

    def update(self, **kwargs):
        pass

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Exchange(Base):
    __tablename__ = 'exchanges'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), ForeignKey('companies.id'), nullable=False)
    quantity = Column(Integer)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    buyer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    seller = relationship("User", back_populates="sells", primaryjoin="User.id==Exchange.seller_id")
    buyer = relationship("User", back_populates="purchases", primaryjoin="User.id==Exchange.buyer_id")
    company = relationship("Company", back_populates="exchanges")

    def __repr__(self):
        return "<Exchange(id='%s', symbol='%s', quantity='%s', price='%s', seller_id='%s', buyer_id='%s')>" % (
            self.id, self.symbol, self.quantity, self.price, self.seller_id, self.buyer_id
        )

    def update(self, **kwargs):
        pass

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), unique=True, nullable=False)
    company_name = Column(String(255), nullable=False)
    industry = Column(String(255))
    website = Column(String(255))
    description = Column(String)
    sector = Column(String(255))
    tags = Column(String)
    created = Column(DateTime(), server_default=text("(datetime('now'))"))
    updated = Column(DateTime(), server_default=text("(datetime('now'))"))
    bids = relationship("Bid", back_populates="company")
    asks = relationship("Ask", back_populates="company")
    book = relationship("Book", back_populates="company")
    exchanges = relationship("Exchange", back_populates="company")

    def __repr__(self):
        return "<Company(id='%s', symbol='%s', company_name='%s', website='%s')>" % (
            self.id, self.symbol, self.company_name, self.website
        )

    def update(self, **kwargs):
        if len(kwargs):
            self.updated = datetime.datetime.utcnow()
            p = ('symbol', 'company_name', 'industry', 'website', 'description', 'sector', 'tags')
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
