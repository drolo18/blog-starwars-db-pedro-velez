from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String 



class Character(db.Model):
    __tablename__ = "character"

    character_id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    


    def serialize(self):
        return {
            "character_id": self.character_id,
            "character_name":self.character_name
           
        }