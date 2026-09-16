from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Song(Base):
    __tablename__ = "Song"

    Song_id = Column(BigInteger, primary_key=True, index=True)
    Song_Name = Column(Text, nullable=False, unique=True)
    Album_id = Column(Integer, ForeignKey("Album.Album_id"), nullable=False)
    Song_Key = Column(Text, nullable=False, unique=True)
    duration_ms = Column(Integer, nullable=False)

    # Relationships
    album = relationship("Album", back_populates="songs")
    artists = relationship("Artist", secondary="Song_Artist", back_populates="songs")
    playback_history = relationship("PlaybackHistory", back_populates="song")
    playlist_songs = relationship("PlaylistSong", back_populates="song")
    stats = relationship("SongStats", back_populates="song", uselist=False)
    daily_plays = relationship("SongDailyPlay", back_populates="song")
    user_play_stats = relationship("UserSongPlayStats", back_populates="song")
