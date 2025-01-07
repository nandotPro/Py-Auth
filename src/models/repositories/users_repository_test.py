import pytest
from src.models.repositories.users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock

class MockCursor:
    """Mock class for database cursor"""
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    """Mock class for database connection"""
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

@pytest.fixture
def users_repository():
    """Fixture that provides a repository instance with mock connection"""
    mock_connection = MockConnection()
    repo = UsersRepository(mock_connection)
    return repo, mock_connection

def test_register_user(users_repository):
    """Test user registration functionality"""
    repository_instance, mock_connection = users_repository

    repository_instance.register_user("John Doe", "123456")
    
    cursor = mock_connection.cursor.return_value
    assert cursor.execute.call_args[0][0] == "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)"
    assert cursor.execute.call_args[0][1] == ("John Doe", "123456", 0)
    mock_connection.commit.assert_called_once()

def test_edit_balance(users_repository):
    """Test balance editing functionality"""
    repository_instance, mock_connection = users_repository

    repository_instance.edit_balance(1, 100)

    cursor = mock_connection.cursor.return_value
    assert cursor.execute.call_args[0][0] == "UPDATE users SET balance=? WHERE id=?"
    assert cursor.execute.call_args[0][1] == (100, 1)
    mock_connection.commit.assert_called_once()

def test_get_user_by_id(users_repository):
    """Test retrieving user by ID functionality"""
    repository_instance, mock_connection = users_repository

    repository_instance.get_user_by_id(1)

    cursor = mock_connection.cursor.return_value
    assert cursor.execute.call_args[0][0] == "SELECT * FROM users WHERE id=?"
    assert cursor.execute.call_args[0][1] == (1,)

@pytest.mark.skip(reason="Test temporarily skipped")
def test_repository():
    """Integration test for repository with real database connection"""
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repo = UsersRepository(connection)
    repo.register_user("John Doe", "123456")
