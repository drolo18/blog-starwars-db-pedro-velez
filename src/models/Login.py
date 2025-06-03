from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Boolean




class Login(db.Model):
    __tablename__ = "login"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_login: Mapped[bool] = mapped_column(Boolean, default=False)
    


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_login": self.user_login
           
        }