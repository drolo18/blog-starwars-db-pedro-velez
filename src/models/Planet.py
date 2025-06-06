from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String 



class Planet(db.Model):
    __tablename__ = "planet"

    planet_id: Mapped[int] = mapped_column(primary_key=True)
    Planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    


    def serialize(self):
        return {
            "planet_id": self.planet_id,
            "Planet_name":self.Planet_name
           
        }