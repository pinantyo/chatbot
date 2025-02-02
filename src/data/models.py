from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    messages: Mapped[List["Message"]] = relationship(
        back_populates="user_account", 
        cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r})"

class Message(Base):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] =mapped_column(Text())
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="messages")
    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, message={self.message!r})"
    
class ContextInformation(Base):
    __tablename__ = "context_information"
    id: Mapped[int] = mapped_column(primary_key=True)
    context: Mapped[str]
    def __repr__(self) -> str:
        return f"ContextInformation(id={self.id!r}, context={self.context!r})"