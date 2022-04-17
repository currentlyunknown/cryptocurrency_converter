from sqlalchemy import Column, String, Float, Integer, DateTime

from settings import db


class Exchange(db.Model):
    __tablename__ = 'exchange'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crypto = Column(String(20), nullable=False)
    fiat = Column(String(3), nullable=False)
    rate = Column(Float, nullable=False)
    crypto_amount = Column(Float, nullable=False)
    fiat_amount = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)
