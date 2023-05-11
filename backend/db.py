import time
from cassandra.cluster import Cluster, NoHostAvailable, UnresolvableContactPoints
from functools import lru_cache
from config import Settings
import uuid

import cassandra

import sys
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

    _CLUSTER = None
    session = None

    while True:
        try:
            # logging.basicConfig(handlers=[logging.FileHandler(filename="../logs/main.log", encoding="utf-8")], level=logging.ERROR)
            if _CLUSTER is None:
                print('connecting cluster')
                _CLUSTER = get_cluster(connect_cluster)
                print('connecting cluster')
                
            if session is None:
                print('connecting session')
                session = _CLUSTER.connect(keyspace)
                # session.set_keyspace(keyspace)
                # use_statement = 'USE %s', keyspace
                # print(use_statement)
                # session.execute(use_statement)
                print(session)

            print ('final session')
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
                    INSERT INTO user (user_name, email, full_name, hashed_password, verification_code)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (str(uuid.uuid4()), "johnorga@gmail.com", "John O'Reilly", "xxyyzz", "123456")
                )
            break
        except (UnresolvableContactPoints, NoHostAvailable) as e:
            pass
            # print(e)
        except Exception as e1:
            pass
            # print(e)
        finally:
            print('exchihi')
            time.sleep(5)  # wait before reconnecting

def connect_cluster():
    return Cluster(contact_points=['node-seed'],load_balancing_policy=None)

def get_cluster(connect_statement, keyspace, wait_timeout=300, quiet=False):
    start_at = time.time()
    wait_println_counter = 0

    while time.time() - start_at < wait_timeout:
        try:
            print(connect_statement)
            cluster = connect_statement()
            # return cluster.connect()
            return cluster
        except (cassandra.cluster.NoHostAvailable, cassandra.UnresolvableContactPoints) as e:
            if not quiet:
                print(repr(e))
            wait_println_counter += 3
            if wait_println_counter == 3:
                if not quiet:
                    print("Waiting 30 more seconds...")
                wait_println_counter = 0
            time.sleep(10)
        # else:
        #     sys.exit(0)
    else:
        if not quiet:
            print("Waiting time exceeded, aborting...")
        sys.exit(1)

