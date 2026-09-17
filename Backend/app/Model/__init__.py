# Import all model classes so SQLAlchemy can find them when mappers are configured
from .User import User
from .Playlist import Playlist
from .PlaylistSong import PlaylistSong
from .PlaybackHistory import PlaybackHistory
from .UserSession import UserSession
from .UserSongPlayStats import UserSongPlayStats
from .Song import Song
from .Album import Album
from .Artist import Artist
from .SongStats import SongStats
from .SongDailyPlay import SongDailyPlay
from .SongArtist import SongArtist
# Additional modules (schemas, etc.) can be imported here if needed
from .schemas import *
