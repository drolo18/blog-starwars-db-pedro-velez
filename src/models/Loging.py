from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Boolean




class Loging(db.Model):
    __tablename__ = "loging"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name_loging: Mapped[str] = mapped_column(ForeignKey("user.user_name"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_loging: Mapped[bool] = mapped_column(Boolean, default=False)
    


    def serialize(self):
        return {
            "id": self.id,
            "user_name_loging":self.user_name_loging,
            "user_id": self.user_id,
            "user_loging": self.user_loging
           
        }