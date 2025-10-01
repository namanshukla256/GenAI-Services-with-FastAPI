from datetime import UTC, datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Define the base class for declarative models
class Base(DeclarativeBase):
    pass

# Define the Conversation entity
class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # Primary key
    title: Mapped[str] = mapped_column()
    model_type: Mapped[str] = mapped_column(index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="conversation", cascade="all, delete-orphan"
    ) # One-to-many relationship with Message


# Define the Message entity
class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id", ondelete="CASCADE"), index=True
    ) # Foreign key to Conversation
    prompt_content: Mapped[str] = mapped_column()
    response_content: Mapped[str] = mapped_column()
    prompt_tokens: Mapped[int | None] = mapped_column()
    response_tokens: Mapped[int | None] = mapped_column()
    total_tokens: Mapped[int | None] = mapped_column()
    is_success: Mapped[bool | None] = mapped_column()
    status_code: Mapped[int | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages"
    ) # Many-to-one relationship with Conversation