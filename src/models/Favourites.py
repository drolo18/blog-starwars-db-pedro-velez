from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey




class Favourite(db.Model):
    __tablename__ = "favourite"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.character_id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.planet_id"))
    login_id: Mapped[int] = mapped_column(ForeignKey("login.id"))
    


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "login_id": self.login_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
            
           
        }