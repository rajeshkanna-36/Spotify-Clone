from app.database import engine, Base
from app.Model import User, Album, Artist, PlaybackHistory, Playlist, PlaylistSong, Song, SongArtist, SongDailyPlay, SongStats, UserSession, UserSongPlayStats

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
