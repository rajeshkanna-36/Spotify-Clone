from sqlalchemy import BigInteger, Column, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class UserSession(Base):
    __tablename__ = "user_session"

    session_id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("User.user_id"), nullable=False)
    refresh_token_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    expire_at = Column(TIMESTAMP, nullable=False)

    # Relationships
    user = relationship("User", back_populates="sessions")
