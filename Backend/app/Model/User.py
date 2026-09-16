from sqlalchemy import BigInteger, Column, Date, Text
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "User"

    user_id = Column(BigInteger, primary_key=True, index=True)
    user_name = Column(Text, nullable=False)
    email_id = Column(Text, nullable=False, unique=True)
    mobile_number = Column(Text, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    password_hash = Column(Text, nullable=False)

    # Relationships
    playlists = relationship("Playlist", back_populates="user")
    playback_history = relationship("PlaybackHistory", back_populates="user")
    sessions = relationship("UserSession", back_populates="user")
    song_play_stats = relationship("UserSongPlayStats", back_populates="user")