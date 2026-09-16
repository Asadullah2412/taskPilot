from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,Text,DateTime,func
from sqlalchemy.orm import Mapped, mapped_column
from  database.database_setup import Base
from datetime import datetime
from uuid_utils.compat import uuid7
import uuid
from database.database_setup import Base

class Task(Base):
    __tablename__ = "Tasks"
    id:Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid7
    )

    title:Mapped[str] = mapped_column(String(250))

    description: Mapped[str|None] = mapped_column(Text,default=None)

    completed:Mapped[bool] = mapped_column(
        default=False,
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )



