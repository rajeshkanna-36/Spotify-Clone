from sqlalchemy import BigInteger, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class PlaybackHistory(Base):
    __tablename__ = "Playback_history"

    history_id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("User.user_id"), nullable=False)
    song_id = Column(BigInteger, ForeignKey("Song.Song_id"), nullable=False)
    played_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="playback_history")
    song = relationship("Song", back_populates="playback_history")
