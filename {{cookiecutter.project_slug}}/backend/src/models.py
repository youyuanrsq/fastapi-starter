from typing import Any
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import String, Integer, Boolean, DateTime


class Base(DeclarativeBase):
    """
    base定义
    """

    id: Any
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    create_by: Mapped[int] = mapped_column(Integer, nullable=True)
    update_by: Mapped[int] = mapped_column(Integer, nullable=True)
    is_del: Mapped[bool] = mapped_column(Boolean, default=False)

    description: Mapped[str | None] = mapped_column(String, nullable=True)
