import time
from cassandra.cluster import Cluster
from functools import lru_cache
from config import Settings

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


_CLUSTER = Cluster(contact_points=['node-seed'])
print(_CLUSTER)

# while True:
#     try:
#         session = _CLUSTER.connect(_keyspace)
#         print('try')
#         break
#     except:
#         time.sleep(10)  # wait before reconnecting
#         print('exc')
