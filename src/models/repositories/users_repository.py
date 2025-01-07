from sqlite3 import Connection

class UsersRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def register_user(self, username: str, password: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)",
            (username, password, 0)
        )
        self.__connection.commit()

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            "UPDATE users SET balance=? WHERE id=?",
            (new_balance, user_id)
        )
        self.__connection.commit()

    def get_user_by_id(self, user_id: int):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return cursor.fetchone()

