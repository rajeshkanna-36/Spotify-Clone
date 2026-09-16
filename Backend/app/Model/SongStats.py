from sqlalchemy import BigInteger, Column

from app.database import Base


class SongStats(Base):
    __tablename__ = "song_stats"

    song_id = Column(BigInteger, primary_key=True)
    play_count = Column(BigInteger, nullable=False, default=0)
