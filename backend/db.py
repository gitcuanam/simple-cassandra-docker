import time
from cassandra.cluster import Cluster
from functools import lru_cache
from config import Settings
import uuid

import logging

# @lru_cache()
# def db_cred():
#     return Settings()


# _cred = db_cred()  # Load the cred from the .env

# """
# Load the database credentials and keyspace name from the Environment Variables
# """
# _username = _cred.db_username
# _password = _cred.db_password
# _keyspace = _cred.keyspace

def connect():
    # keyspace = 'chi_url'
    keyspace = 'user'


    _CLUSTER = Cluster(contact_points=['node-seed'])
    print(_CLUSTER)
    session = _CLUSTER.connect(keyspace)
    print(session)

    if (session is not None):
        # session.execute(
        #     """
        #     INSERT INTO user (user_name, disabled, email, name, hased_password, verification_code)
        #     VALUES (%s, %i, %s, %s, %s, %s)
        #     """,
        #     (str(uuid.uuid4()), False, "johnorga@gmail.com", "John O'Reilly", "xxyyzz", "123456")
        # )
        
        session.execute(
            """
            INSERT INTO user (user_name, email, full_name, hased_password, verification_code)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (str(uuid.uuid4()), "johnorga@gmail.com", "John O'Reilly", "xxyyzz", "123456")
        )
# session.set_keyspace(keyspace)
# use_statement = 'USE %s', keyspace
# print(use_statement)
# session.execute(use_statement)
# while True:
#     try:
#         session = _CLUSTER.connect('chi_url')
#         print('try')

#         print(session)
#         logging.basicConfig(handlers=[logging.FileHandler(filename="../logs/main.log", encoding="utf-8")], level=logging.ERROR)
#         # user_add_stmt = session.prepare(
#         #     "INSERT INTO user (user_name, disabled, email, hashed_password) VALUES (?, TRUE, ?, ?)")  # prepared statement to add user
#         # session.execute(user_add_stmt,
#         #             ['jjj', 'jjj@gmail.com', 'jjj'])  # replace the pre_stmt with the actual values
#         break
#     except:
#         time.sleep(10)  # wait before reconnecting
#         print('exc')
