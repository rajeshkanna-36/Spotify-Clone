from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Artist(Base):
    __tablename__ = "Artist"

    Artist_id = Column(Integer, primary_key=True, index=True)
    Artist_name = Column(Text, nullable=False)

    # Relationships
    songs = relationship("Song", secondary="Song_Artist", back_populates="artists")
