from sqlalchemy import BigInteger, Column, ForeignKey, Integer

from app.database import Base


class SongArtist(Base):
    __tablename__ = "Song_Artist"

    Song_id = Column(BigInteger, ForeignKey("Song.Song_id"), primary_key=True)
    Artist_id = Column(Integer, ForeignKey("Artist.Artist_id"), primary_key=True)
