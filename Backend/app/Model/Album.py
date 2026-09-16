from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Album(Base):
    __tablename__ = "Album"

    Album_id = Column(Integer, primary_key=True, index=True)
    Album_name = Column(Text, nullable=False, unique=True)

    # Relationships
    songs = relationship("Song", back_populates="album")
