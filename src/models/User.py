from database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String , DateTime
import datetime


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    pasword: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    


    def serialize(self):
        return {
            "id": self.id,
            "user_name":self.user_name,
            "firs_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date": self.date
           
        }