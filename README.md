# simple-cassandra-docker

## Problems monitoring cassandra cluster

[Unexpected connection timeout in datastax cassandra -com.datastax.shaded.netty.channel.ConnectTimeoutException](https://stackoverflow.com/questions/32086643/unexpected-connection-timeout-in-datastax-cassandra-com-datastax-shaded-netty-c)
```log
INFO  [main] 2023-05-04 13:41:24,292 ColumnFamilyStore.java:2652 - Truncate of system.table_estimates is complete
INFO  [main] 2023-05-04 13:41:24,300 QueryProcessor.java:181 - Preloaded 0 prepared statements
INFO  [main] 2023-05-04 13:41:24,301 StorageService.java:785 - Cassandra version: 4.1.1
INFO  [main] 2023-05-04 13:41:24,301 StorageService.java:786 - CQL version: 3.4.6
INFO  [main] 2023-05-04 13:41:24,301 StorageService.java:787 - Native protocol supported versions: 3/v3, 4/v4, 5/v5, 6/v6-beta (default: 5/v5)
INFO  [main] 2023-05-04 13:41:24,344 IndexSummaryManager.java:86 - Initializing index summary manager with a memory pool size of 97 MB and a resize interval of 60 minutes
INFO  [main] 2023-05-04 13:41:24,346 StorageService.java:804 - Loading persisted ring state
INFO  [main] 2023-05-04 13:41:24,346 StorageService.java:894 - Populating token metadata from system tables
INFO  [GossipStage:1] 2023-05-04 13:41:24,354 Gossiper.java:2041 - Adding /172.25.0.4:7000 as there was no previous epState; new state is EndpointState: HeartBeatState = HeartBeat: generation = 0, version = -1, AppStateMap = {}
INFO  [GossipStage:1] 2023-05-04 13:41:24,355 Gossiper.java:2041 - Adding /172.25.0.3:7000 as there was no previous epState; new state is EndpointState: HeartBeatState = HeartBeat: generation = 0, version = -1, AppStateMap = {}
INFO  [main] 2023-05-04 13:41:24,366 InboundConnectionInitiator.java:149 - Listening on address: (/172.26.0.2:7000), nic: eth0, encryption: unencrypted
INFO  [Service Thread] 2023-05-04 13:41:25,027 GCInspector.java:296 - ParNew GC in 461ms.  CMS Old Gen: 0 -> 15304496; Par Eden Space: 335544320 -> 0; Par Survivor Space: 26145296 -> 31339392
INFO  [Messaging-EventLoop-3-3] 2023-05-04 13:41:32,143 InboundConnectionInitiator.java:529 - /172.26.0.3:7000(/172.26.0.3:56752)->/172.26.0.2:7000-URGENT_MESSAGES-1fd35a08 messaging connection established, version = 12, framing = LZ4, encryption = unencrypted
INFO  [Messaging-EventLoop-3-3] 2023-05-04 13:41:32,167 NoSpamLogger.java:105 - /172.26.0.2:7000->/172.25.0.3:7000-URGENT_MESSAGES-[no-channel] failed to connect
io.netty.channel.ConnectTimeoutException: connection timed out: /172.25.0.3:7000
        at io.netty.channel.epoll.AbstractEpollChannel$AbstractEpollUnsafe$2.run(AbstractEpollChannel.java:576)
        at io.netty.util.concurrent.PromiseTask.runTask(PromiseTask.java:98)
        at io.netty.util.concurrent.ScheduledFutureTask.run(ScheduledFutureTask.java:170)
        at io.netty.util.concurrent.AbstractEventExecutor.safeExecute(AbstractEventExecutor.java:164)
        at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:472)
        at io.netty.channel.epoll.EpollEventLoop.run(EpollEventLoop.java:384)
        at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:989)
        at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74)
        at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30)
        at java.base/java.lang.Thread.run(Unknown Source)
INFO  [Messaging-EventLoop-3-2] 2023-05-04 13:41:32,170 OutboundConnection.java:1153 - /172.26.0.2:7000(/172.26.0.2:40286)->/172.26.0.3:7000-URGENT_MESSAGES-bd1b8f93 successfully connected, version = 12, framing = LZ4, encryption = unencrypted
INFO  [Messaging-EventLoop-3-3] 2023-05-04 13:41:32,492 InboundConnectionInitiator.java:529 - /172.26.0.4:7000(/172.26.0.4:44550)->/172.26.0.2:7000-URGENT_MESSAGES-e85f53af messaging connection established, version = 12, framing = LZ4, encryption = unencrypted
```

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