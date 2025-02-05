from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

class BaseModel(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, nullable=False, index=True)
    create_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    class Config:
         orm_model = True