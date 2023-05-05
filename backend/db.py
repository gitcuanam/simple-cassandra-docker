import time
from cassandra.cluster import Cluster
from functools import lru_cache
from config import Settings

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


# _CLUSTER = Cluster(contact_points=['cassandra-seed'])
# print(_CLUSTER)
# session = _CLUSTER.connect('chi_url')
# print(session)
# user_add_stmt = session.prepare(
#     "INSERT INTO user (user_name, disabled, email, hashed_password) VALUES (?, TRUE, ?, ?)")  # prepared statement to add user
# session.execute(user_add_stmt,
#             ['jjj', 'jjj@gmail.com', 'jjj'])  # replace the pre_stmt with the actual values
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
