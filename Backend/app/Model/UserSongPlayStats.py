from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class UserSongPlayStats(Base):
    __tablename__ = "user_song_play_stats"

    user_id = Column(BigInteger, ForeignKey("User.user_id"), primary_key=True)
    song_id = Column(BigInteger, ForeignKey("Song.Song_id"), primary_key=True)
    play_count = Column(BigInteger, nullable=False, default=0)

    # Relationships
    user = relationship("User", back_populates="song_play_stats")
    song = relationship("Song", back_populates="user_play_stats")
