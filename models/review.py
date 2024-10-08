#!/usr/bin/python
""" holds class Review"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_type == 'db':
        __tablename__ = 'reviews'
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
