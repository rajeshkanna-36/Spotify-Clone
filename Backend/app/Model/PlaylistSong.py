from sqlalchemy import BigInteger, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class PlaylistSong(Base):
    __tablename__ = "playlist_song"

    playlist_id = Column(BigInteger, ForeignKey("Playlist.playlist_id"), primary_key=True)
    song_id = Column(BigInteger, ForeignKey("Song.Song_id"), primary_key=True)
    position = Column(Integer, nullable=False)

    # Relationships
    playlist = relationship("Playlist", back_populates="playlist_songs")
    song = relationship("Song", back_populates="playlist_songs")
