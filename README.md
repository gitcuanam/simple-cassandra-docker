# simple-cassandra-docker

Sample docker compose file to create cassandra cluster

(https://gist.github.com/naumanbadar/aad6a25974b30adcb3c89b5f868627da)

```yml
version: "3.3"

# make sure that docker machine has enough memory to run the cluster.
# setting it up to 4GB seems to work.

services:

  cassandra-seed:
    image: cassandra:latest
#    ports:
#      - "9042:9042"
    volumes:
      - "cassandra_data_seed:/var/lib/cassandra"
    environment:
      - "CASSANDRA_SEEDS=cassandra-seed"
      - "CASSANDRA_CLUSTER_NAME=Test Cluster"
#      needed for setting up custom cluster name
      - "CASSANDRA_DC=se1"
      - "CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch"
#    restart: always


  cassandra1:
    image: cassandra:latest
    volumes:
      - "cassandra_data_1:/var/lib/cassandra"
    environment:
      - "CASSANDRA_SEEDS=cassandra-seed"
      - "CASSANDRA_CLUSTER_NAME=Test Cluster"
#      needed for setting up custom cluster name
      - "CASSANDRA_DC=se1"
      - "CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch"
    depends_on:
      - cassandra-seed
#    restart: always

  cassandra2:
    image: cassandra:latest
    volumes:
      - "cassandra_data_2:/var/lib/cassandra"
    environment:
      - "CASSANDRA_SEEDS=cassandra-seed"
      - "CASSANDRA_CLUSTER_NAME=Test Cluster"
#      needed for setting up custom cluster name
      - "CASSANDRA_DC=se1"
      - "CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch"
    depends_on:
      - cassandra-seed
#    restart: always

volumes:
  cassandra_data_seed:
  cassandra_data_1:
  cassandra_data_2:
```

(https://github.com/calvinlfer/compose-cassandra-cluster/blob/master/docker-compose.yml)

```yml
version: '2'

# 3 node cluster
# If you see exit code 137 (OOM killer) then ensure Docker has access to more resources
services:
  cassandra-seed:
    container_name: cassandra-seed-node
    image: cassandra:3.11.0
    ports:
      - "9042:9042"   # Native transport
      - "7199:7199"   # JMX
      - "9160:9160"   # Thrift clients

  cassandra-node-1:
    image: cassandra:3.11.0
    command: /bin/bash -c "echo 'Waiting for seed node' && sleep 30 && /docker-entrypoint.sh cassandra -f"
    environment:
      - "CASSANDRA_SEEDS=cassandra-seed-node"
    depends_on:
      - "cassandra-seed"

  # you cannot have multiple nodes join the cluster at the same time when
  # cassandra.consistent.rangemovement is true so we further delay it to give it time to stabilize
  cassandra-node-2:
    image: cassandra:3.11.0
    command: /bin/bash -c "echo 'Waiting for seed node' && sleep 80 && /docker-entrypoint.sh cassandra -f"
    environment:
      - "CASSANDRA_SEEDS=cassandra-seed-node"
    depends_on:
      - "cassandra-seed"
```

(https://github.com/logdeveloper/cassandra-docker-compose)

Create user-defined bridge network
```bash
docker network create --gateway 172.18.0.1 --subnet 172.18.0.0/16 broker-net
```

```yml
version: "3.8"
services:
  cassandra-0:
    image: cassandra:latest
    restart: always
    networks:
      broker:
        ipv4_address: 172.18.0.10
    ports:
      - 7000:7000
      - 9042:9042
    volumes:
      - /home/cassandra-node-0/commitlog:/var/lib/cassandra/commitlog
      - /home/cassandra-node-0/hints:/var/lib/cassandra/hints
      - /home/cassandra-node-0/data:/var/lib/cassandra/data
      - /home/cassandra-node-0/saved_caches:/var/lib/cassandra/saved_caches
      - /home/cassandra-node-0/logs:/var/log/cassandra
    environment:
      - CASSANDRA_SEEDS=cassandra-0
      - CASSANDRA_CLUSTER_NAME=cluster
      - CASSANDRA_NUM_TOKENS=8
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack0
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
      - MAX_HEAP_SIZE=8G
      - HEAP_NEWSIZE=200M

  cassandra-1:
    image: cassandra:latest
    networks:
      broker:
        ipv4_address: 172.18.0.11
    restart: always
    ports:
      - 1700:7000
      - 19042:9042
    volumes:
      - /home/cassandra-node-1/data:/var/lib/cassandra/data
      - /home/cassandra-node-1/commitlog:/var/lib/cassandra/commitlog
      - /home/cassandra-node-1/hints:/var/lib/cassandra/hints
      - /home/cassandra-node-1/saved_caches:/var/lib/cassandra/saved_caches
      - /home/cassandra-node-1/logs:/var/log/cassandra
    environment:
      - CASSANDRA_SEEDS=cassandra-0
      - CASSANDRA_CLUSTER_NAME=cluster
      - CASSANDRA_NUM_TOKENS=8
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack0
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch      
      - MAX_HEAP_SIZE=8G
      - HEAP_NEWSIZE=200M

  cassandra-2:
    image: cassandra:latest
    restart: always
    networks:
      broker:
        ipv4_address: 172.18.0.12
    ports:
      - 27000:7000
      - 29042:9042
    volumes:
      - /home/cassandra-node-2/data:/var/lib/cassandra/data
      - /home/cassandra-node-2/commitlog:/var/lib/cassandra/commitlog
      - /home/cassandra-node-2/hints:/var/lib/cassandra/hints
      - /home/cassandra-node-2/saved_caches:/var/lib/cassandra/saved_caches
      - /home/cassandra-node-2/logs:/var/log/cassandra      
    environment:
      - CASSANDRA_SEEDS=cassandra-0
      - CASSANDRA_CLUSTER_NAME=cluster
      - CASSANDRA_NUM_TOKENS=8
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack0
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
      - MAX_HEAP_SIZE=8G
      - HEAP_NEWSIZE=200M
      
networks:
  broker:
    external:
      name: broker-net     
```

Create virtaul environment for python3
```bash
virtualenv simple-cassandra-docker -p python3
```

Build backend docker image
```
cd backend
docker build -t python-cassandra .
```