from sqlalchemy import BigInteger, Column, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class SongDailyPlay(Base):
    __tablename__ = "song_daily_play"

    song_id = Column(BigInteger, ForeignKey("Song.Song_id"), primary_key=True)
    play_date = Column(Date, primary_key=True)
    play_count = Column(BigInteger, nullable=False, default=0)

    # Relationships
    song = relationship("Song", back_populates="daily_plays")
