from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class Voice(Base):
    __tablename__ = "voices"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    elevenlabs_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True)
    status: Mapped[str] = mapped_column(String(50), default="training")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    samples: Mapped[List["VoiceSample"]] = relationship(
        back_populates="voice", cascade="all, delete-orphan"
    )


class VoiceSample(Base):
    __tablename__ = "voice_samples"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    voice_id: Mapped[int] = mapped_column(ForeignKey("voices.id", ondelete="CASCADE"), nullable=False)

    file_url: Mapped[str] = mapped_column(Text, nullable=False)
    duration_sec: Mapped[int] = mapped_column(default=0)

    voice: Mapped["Voice"] = relationship(back_populates="samples")