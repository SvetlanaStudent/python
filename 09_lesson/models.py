
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для моделей
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)  # Поле ID
    name = Column(String, index=True)  # Поле имени студента
    age = Column(Integer)  # Поле возраста студента

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"