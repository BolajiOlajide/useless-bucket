from sqlalchemy import Integer, Column, String, func, DateTime

from database import Base


class Bucket(Base):
    __tablename__ = "buckets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())
