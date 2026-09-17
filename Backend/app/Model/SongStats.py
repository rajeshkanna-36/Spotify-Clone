from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class SongStats(Base):
    __tablename__ = "song_stats"

    song_id = Column(BigInteger, ForeignKey("Song.Song_id"), primary_key=True)
    play_count = Column(BigInteger, nullable=False, default=0)

    # Relationship back to Song
    song = relationship("Song", back_populates="stats")
