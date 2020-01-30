from psycopg2 import connect


class DatabaseConnector():
    """
    This class is responsible for connection with the database. As an input it requires connection details,
    connection cursor is returned
    """

    def __init__(self, dbname, user = 'postgres' ,password = 'password' , host = 'xxx.xxx.xxx.xxx'):
        """
        Initialization
        :param dbname:name of the database 
        :param user: user name
        :param password: password
        :param host: host ip
        """
        self._user = user
        self._password = password
        self._dbname = dbname
        self._host = host

    def connect(self):
        """Function used to connect with the database"""
        conn_dict = {'user': self._user, 'password': self._password, 'dbname': self._dbname, 'host': self._host}
        try:
            conn = connect(dbname=conn_dict['dbname'], user=conn_dict['user'], host=conn_dict['host'], password=conn_dict['password'])
        except EnvironmentError:
            print("I am unable to connect to the database")

        cur = conn.cursor()
        conn.set_isolation_level(0)

        return cur

    @property
    def dbname(self):
        return self._dbname

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def host(self):
        return self._host
