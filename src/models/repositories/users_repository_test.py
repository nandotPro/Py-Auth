from src.models.repositories.users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_repository():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UsersRepository(connection)
    repository.register_user("John Doe", "123456")

