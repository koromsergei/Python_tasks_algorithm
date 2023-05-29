class ConnectionError(Exception):
    """Класс исключения при соединении"""


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = True

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        self._fl_connection_open = True
        raise ConnectionError('Error')

    def close(self):
        self._fl_connection_open = False


with DatabaseConnection() as conn:
    print(conn)
