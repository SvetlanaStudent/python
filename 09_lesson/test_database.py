import pytest
from sqlalchemy.orm import sessionmaker
from database import engine, Student

# Создаем фикстуру для сессии
@pytest.fixture(scope='function')
def session():
    """Создаем новую сессию для каждого теста."""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session  # Возвращаем сессию для тестов

    session.close()
    transaction.rollback()
    connection.close()

# Тест на добавление студента
def test_add_student(session):
    new_student = Student(name='John Doe', age=25)
    session.add(new_student)
    session.commit()

    assert new_student.id is not None  # Проверяем, что ID был присвоен

# Тест на изменение студента
def test_update_student(session):
    new_student = Student(name='Jane Doe', age=22)
    session.add(new_student)
    session.commit()

    new_student.age = 23
    session.commit()

    updated_student = session.query(Student).filter_by(id=new_student.id).first()
    assert updated_student.age == 23  # Проверяем, что возраст обновился

# Тест на удаление студента
def test_delete_student(session):
    new_student = Student(name='Mark Smith', age=30)
    session.add(new_student)
    session.commit()

    session.delete(new_student)
    session.commit()

    deleted_student = session.query(Student).filter_by(id=new_student.id).first()
    assert deleted_student is None  # Проверяем, что студент был удален