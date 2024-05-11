import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, nullable=False, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)
    status = Column(Boolean, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "book_id": str(self.book_id),
            "status": str(self.status)
        }

    @staticmethod
    def serialize_copies(copies):
        serialized_copies = []
        for copy in copies:
            serialized_copy = {
                "id": str(copy.id),
                "book_id": str(copy.book_id),
                "status": str(copy.status)
            }
            serialized_copies.append(serialized_copy)
        return serialized_copies
