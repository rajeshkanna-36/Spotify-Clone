from sqlalchemy import BigInteger, Column, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Playlist(Base):
    __tablename__ = "Playlist"

    playlist_id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("User.user_id"), nullable=False)
    playlist_name = Column(Text, nullable=False)
    playlist_cover_key = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="playlists")
    playlist_songs = relationship("PlaylistSong", back_populates="playlist")
