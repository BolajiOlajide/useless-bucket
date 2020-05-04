from sqlalchemy import Integer, Column, String, func, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from database import Base
from .bucket import Bucket


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    done = Column(Boolean, default=False)
    bucket_id = Column(Integer, ForeignKey("buckets.id"))
    bucket = relationship(
        Bucket, backref=backref("items", uselist=True, cascade="delete,all")
    )
