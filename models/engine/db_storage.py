from sqlalchemy.orm import Session

class DBStorage:
    __session = None  # The SQLAlchemy session

    ...

    def close(self):
        """Calls remove() method on the private session attribute"""
        self.__session.remove()
        # or you can use close() on the class Session
        # Session.close(self.__session)
