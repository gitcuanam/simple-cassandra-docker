# simple-cassandra-docker

## Problems monitoring cassandra cluster

### Unkown node exits from cluster (checked all 3 nodes, none of them have the ip 192.168.32.4)

Get masks of networks in docker [\[source\]](https://stackoverflow.com/questions/58764152/how-to-get-a-ip-addresses-for-all-docker-containers-from-the-host/58764153#58764153)
```bash
for e in $(docker network ls --format '{{.Name}}') ; do docker network inspect $e --format '{{ printf "%-40s" .Name}} {{.IPAM.Config}}'; done
```

```log
INFO  [GossipStage:1] 2023-05-05 04:05:51,594 TokenMetadata.java:539 - Updating topology for /192.168.32.3:7000
INFO  [GossipStage:1] 2023-05-05 04:05:51,596 TokenMetadata.java:539 - Updating topology for /192.168.32.3:7000
INFO  [GossipStage:1] 2023-05-05 04:05:51,605 Gossiper.java:1362 - InetAddress /192.168.32.3:7000 is now UP
INFO  [CompactionExecutor:1] 2023-05-05 04:05:51,668 CompactionTask.java:247 - Compacted (1fdbde60-eafa-11ed-97be-ff0bb7f99558) 4 sstables to [/var/lib/cassandra/data/system/peers-37f71aca7dc2383ba70672528af04d4f/nb-25-big,] to level=0.  1.634KiB to 0.541KiB (~33% of original) in 107ms.  Read Throughput = 15.154KiB/s, Write Throughput = 5.018KiB/s, Row Throughput = ~5/s.  8 total partitions merged to 3.  Partition merge counts were {2:2, 4:1, }. Time spent writing keys = 38ms
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,668 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers-37f71aca7dc2383ba70672528af04d4f/nb-24-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,669 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers-37f71aca7dc2383ba70672528af04d4f/nb-23-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,671 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers-37f71aca7dc2383ba70672528af04d4f/nb-22-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,673 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers-37f71aca7dc2383ba70672528af04d4f/nb-21-big
INFO  [CompactionExecutor:2] 2023-05-05 04:05:51,686 CompactionTask.java:247 - Compacted (1fe0e770-eafa-11ed-97be-ff0bb7f99558) 4 sstables to [/var/lib/cassandra/data/system/peers_v2-c4325fbb8e5e3bafbd070f9250ed818e/nb-25-big,] to level=0.  1.692KiB to 0.563KiB (~33% of original) in 92ms.  Read Throughput = 18.211KiB/s, Write Throughput = 6.063KiB/s, Row Throughput = ~6/s.  8 total partitions merged to 3.  Partition merge counts were {2:2, 4:1, }. Time spent writing keys = 25ms
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,689 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers_v2-c4325fbb8e5e3bafbd070f9250ed818e/nb-24-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,690 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers_v2-c4325fbb8e5e3bafbd070f9250ed818e/nb-21-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,692 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers_v2-c4325fbb8e5e3bafbd070f9250ed818e/nb-23-big
INFO  [NonPeriodicTasks:1] 2023-05-05 04:05:51,693 SSTable.java:127 - Deleting sstable: /var/lib/cassandra/data/system/peers_v2-c4325fbb8e5e3bafbd070f9250ed818e/nb-22-big
INFO  [Messaging-EventLoop-3-3] 2023-05-05 04:06:21,396 NoSpamLogger.java:105 - /192.168.32.2:7000->/192.168.32.4:7000-URGENT_MESSAGES-[no-channel] failed to connect
io.netty.channel.ConnectTimeoutException: connection timed out: /192.168.32.4:7000
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
INFO  [GossipTasks:1] 2023-05-05 04:06:53,307 Gossiper.java:1087 - FatClient /192.168.32.4:7000 has been silent for 30000ms, removing from gossip
INFO  [Messaging-EventLoop-3-3] 2023-05-05 04:06:53,468 NoSpamLogger.java:105 - /192.168.32.2:7000->/192.168.32.4:7000-URGENT_MESSAGES-[no-channel] failed to connect
io.netty.channel.ConnectTimeoutException: connection timed out: /192.168.32.4:7000
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
```


### Unable to lock JVM memory (ENOMEM)
Maximum number of memory map areas per process (vm.max_map_count) 65530 is too low, recommended value: 1048575

How to print sysctl value
```bash
sysctl ``<variable name>``
```
How to temporarily set sysctl value [\[source\]](https://gist.github.com/ntamvl/7c41acee650d376863fd940b99da836f)
```bash
sudo sysctl vm.max_map_count=1048575
sudo sysctl -p
```
```log
INFO  [main] 2023-05-05 01:29:19,642 GossipingPropertyFileSnitch.java:67 - Unable to load cassandra-topology.properties; compatibility mode disabled
INFO  [ScheduledTasks:1] 2023-05-05 01:29:19,964 StreamManager.java:260 - Storing streaming state for 3d or for 119156 elements
INFO  [main] 2023-05-05 01:29:19,968 JMXServerUtils.java:271 - Configured JMX server at: service:jmx:rmi://127.0.0.1/jndi/rmi://127.0.0.1:7199/jmxrmi
INFO  [main] 2023-05-05 01:29:19,996 CassandraDaemon.java:624 - Hostname: 4447b4918752:7000:7001
INFO  [main] 2023-05-05 01:29:19,996 CassandraDaemon.java:631 - JVM vendor/version: OpenJDK 64-Bit Server VM/11.0.18
INFO  [main] 2023-05-05 01:29:19,999 CassandraDaemon.java:632 - Heap size: 1.904GiB/1.904GiB
INFO  [main] 2023-05-05 01:29:20,006 CassandraDaemon.java:637 - CodeHeap 'non-nmethods' Non-heap memory: init = 2555904(2496K) used = 1318400(1287K) committed = 2555904(2496K) max = 5832704(5696K)
INFO  [main] 2023-05-05 01:29:20,025 CassandraDaemon.java:637 - Metaspace Non-heap memory: init = 0(0K) used = 24010128(23447K) committed = 24842240(24260K) max = -1(-1K)
INFO  [main] 2023-05-05 01:29:20,026 CassandraDaemon.java:637 - CodeHeap 'profiled nmethods' Non-heap memory: init = 2555904(2496K) used = 4434688(4330K) committed = 4456448(4352K) max = 122912768(120032K)
INFO  [main] 2023-05-05 01:29:20,028 CassandraDaemon.java:637 - Compressed Class Space Non-heap memory: init = 0(0K) used = 2802648(2736K) committed = 3145728(3072K) max = 1073741824(1048576K)
INFO  [main] 2023-05-05 01:29:20,028 CassandraDaemon.java:637 - Par Eden Space Heap memory: init = 335544320(327680K) used = 174533200(170442K) committed = 335544320(327680K) max = 335544320(327680K)
INFO  [main] 2023-05-05 01:29:20,029 CassandraDaemon.java:637 - Par Survivor Space Heap memory: init = 41943040(40960K) used = 0(0K) committed = 41943040(40960K) max = 41943040(40960K)
INFO  [main] 2023-05-05 01:29:20,029 CassandraDaemon.java:637 - CodeHeap 'non-profiled nmethods' Non-heap memory: init = 2555904(2496K) used = 913280(891K) committed = 2555904(2496K) max = 122912768(120032K)
INFO  [main] 2023-05-05 01:29:20,029 CassandraDaemon.java:637 - CMS Old Gen Heap memory: init = 1667235840(1628160K) used = 0(0K) committed = 1667235840(1628160K) max = 1667235840(1628160K)
INFO  [main] 2023-05-05 01:29:20,030 CassandraDaemon.java:639 - Classpath: /etc/cassandra:/opt/cassandra/lib/HdrHistogram-2.1.9.jar:/opt/cassandra/lib/ST4-4.0.8.jar:/opt/cassandra/lib/airline-0.8.jar:/opt/cassandra/lib/antlr-runtime-3.5.2.jar:/opt/cassandra/lib/apache-cassandra-4.1.1.jar:/opt/cassandra/lib/asm-9.1.jar:/opt/cassandra/lib/caffeine-2.9.2.jar:/opt/cassandra/lib/cassandra-driver-core-3.11.0-shaded.jar:/opt/cassandra/lib/checker-qual-3.10.0.jar:/opt/cassandra/lib/chronicle-bytes-2.20.111.jar:/opt/cassandra/lib/chronicle-core-2.20.126.jar:/opt/cassandra/lib/chronicle-queue-5.20.123.jar:/opt/cassandra/lib/chronicle-threads-2.20.111.jar:/opt/cassandra/lib/chronicle-wire-2.20.117.jar:/opt/cassandra/lib/commons-cli-1.1.jar:/opt/cassandra/lib/commons-codec-1.9.jar:/opt/cassandra/lib/commons-lang3-3.11.jar:/opt/cassandra/lib/commons-math3-3.2.jar:/opt/cassandra/lib/concurrent-trees-2.4.0.jar:/opt/cassandra/lib/ecj-4.6.1.jar:/opt/cassandra/lib/error_prone_annotations-2.5.1.jar:/opt/cassandra/lib/guava-27.0-jre.jar:/opt/cassandra/lib/high-scale-lib-1.0.6.jar:/opt/cassandra/lib/hppc-0.8.1.jar:/opt/cassandra/lib/ipaddress-5.3.3.jar:/opt/cassandra/lib/j2objc-annotations-1.3.jar:/opt/cassandra/lib/jackson-annotations-2.13.2.jar:/opt/cassandra/lib/jackson-core-2.13.2.jar:/opt/cassandra/lib/jackson-databind-2.13.2.2.jar:/opt/cassandra/lib/jackson-datatype-jsr310-2.13.2.jar:/opt/cassandra/lib/jamm-0.3.2.jar:/opt/cassandra/lib/java-cup-runtime-11b-20160615.jar:/opt/cassandra/lib/javax.inject-1.jar:/opt/cassandra/lib/jbcrypt-0.4.jar:/opt/cassandra/lib/jcl-over-slf4j-1.7.25.jar:/opt/cassandra/lib/jcommander-1.30.jar:/opt/cassandra/lib/jctools-core-3.1.0.jar:/opt/cassandra/lib/jflex-1.8.2.jar:/opt/cassandra/lib/jna-5.9.0.jar:/opt/cassandra/lib/json-simple-1.1.jar:/opt/cassandra/lib/jsr305-2.0.2.jar:/opt/cassandra/lib/jvm-attach-api-1.5.jar:/opt/cassandra/lib/log4j-over-slf4j-1.7.25.jar:/opt/cassandra/lib/logback-classic-1.2.9.jar:/opt/cassandra/lib/logback-core-1.2.9.jar:/opt/cassandra/lib/lz4-java-1.8.0.jar:/opt/cassandra/lib/metrics-core-3.1.5.jar:/opt/cassandra/lib/metrics-jvm-3.1.5.jar:/opt/cassandra/lib/metrics-logback-3.1.5.jar:/opt/cassandra/lib/mxdump-0.14.jar:/opt/cassandra/lib/netty-all-4.1.58.Final.jar:/opt/cassandra/lib/netty-tcnative-boringssl-static-2.0.36.Final.jar:/opt/cassandra/lib/ohc-core-0.5.1.jar:/opt/cassandra/lib/ohc-core-j8-0.5.1.jar:/opt/cassandra/lib/psjava-0.1.19.jar:/opt/cassandra/lib/reporter-config-base-3.0.3.jar:/opt/cassandra/lib/reporter-config3-3.0.3.jar:/opt/cassandra/lib/sigar-1.6.4.jar:/opt/cassandra/lib/sjk-cli-0.14.jar:/opt/cassandra/lib/sjk-core-0.14.jar:/opt/cassandra/lib/sjk-json-0.14.jar:/opt/cassandra/lib/sjk-stacktrace-0.14.jar:/opt/cassandra/lib/slf4j-api-1.7.25.jar:/opt/cassandra/lib/snakeyaml-1.26.jar:/opt/cassandra/lib/snappy-java-1.1.8.4.jar:/opt/cassandra/lib/snowball-stemmer-1.3.0.581.1.jar:/opt/cassandra/lib/stream-2.5.2.jar:/opt/cassandra/lib/zstd-jni-1.5.4-1.jar:/opt/cassandra/lib/jsr223/*/*.jar:
INFO  [main] 2023-05-05 01:29:20,031 CassandraDaemon.java:641 - JVM Arguments: [-ea, -da:net.openhft..., -XX:+UseThreadPriorities, -XX:+HeapDumpOnOutOfMemoryError, -Xss256k, -XX:+AlwaysPreTouch, -XX:-UseBiasedLocking, -XX:+UseTLAB, -XX:+ResizeTLAB, -XX:+UseNUMA, -XX:+PerfDisableSharedMem, -Djava.net.preferIPv4Stack=true, -XX:+UseConcMarkSweepGC, -XX:+CMSParallelRemarkEnabled, -XX:SurvivorRatio=8, -XX:MaxTenuringThreshold=1, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -XX:CMSWaitDuration=10000, -XX:+CMSParallelInitialMarkEnabled, -XX:+CMSEdenChunksRecordAlways, -XX:+CMSClassUnloadingEnabled, -Djdk.attach.allowAttachSelf=true, --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED, --add-exports=java.base/jdk.internal.ref=ALL-UNNAMED, --add-exports=java.base/sun.nio.ch=ALL-UNNAMED, --add-exports=java.management.rmi/com.sun.jmx.remote.internal.rmi=ALL-UNNAMED, --add-exports=java.rmi/sun.rmi.registry=ALL-UNNAMED, --add-exports=java.rmi/sun.rmi.server=ALL-UNNAMED, --add-exports=java.sql/java.sql=ALL-UNNAMED, --add-opens=java.base/java.lang.module=ALL-UNNAMED, --add-opens=java.base/jdk.internal.loader=ALL-UNNAMED, --add-opens=java.base/jdk.internal.ref=ALL-UNNAMED, --add-opens=java.base/jdk.internal.reflect=ALL-UNNAMED, --add-opens=java.base/jdk.internal.math=ALL-UNNAMED, --add-opens=java.base/jdk.internal.module=ALL-UNNAMED, --add-opens=java.base/jdk.internal.util.jar=ALL-UNNAMED, --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED, -Dio.netty.tryReflectionSetAccessible=true, -Xlog:gc=info,heap*=trace,age*=debug,safepoint=info,promotion*=trace:file=/opt/cassandra/logs/gc.log:time,uptime,pid,tid,level:filecount=10,filesize=10485760, -Xms1989M, -Xmx1989M, -Xmn400M, -XX:+UseCondCardMark, -XX:CompileCommandFile=/etc/cassandra/hotspot_compiler, -javaagent:/opt/cassandra/lib/jamm-0.3.2.jar, -Dcassandra.jmx.local.port=7199, -Dcom.sun.management.jmxremote.authenticate=false, -Dcom.sun.management.jmxremote.password.file=/etc/cassandra/jmxremote.password, -Djava.library.path=/opt/cassandra/lib/sigar-bin, -Dcassandra.libjemalloc=/usr/local/lib/libjemalloc.so, -XX:OnOutOfMemoryError=kill -9 %p, -Dlogback.configurationFile=logback.xml, -Dcassandra.logdir=/opt/cassandra/logs, -Dcassandra.storagedir=/opt/cassandra/data, -Dcassandra-foreground=yes]
WARN  [main] 2023-05-05 01:29:20,032 NativeLibrary.java:199 - Unable to lock JVM memory (ENOMEM). This can result in part of the JVM being swapped out, especially with mmapped I/O enabled. Increase RLIMIT_MEMLOCK.
INFO  [main] 2023-05-05 01:29:20,110 MonotonicClock.java:208 - Scheduling approximate time conversion task with an interval of 10000 milliseconds
INFO  [main] 2023-05-05 01:29:20,114 MonotonicClock.java:344 - Scheduling approximate time-check task with a precision of 2 milliseconds
INFO  [main] 2023-05-05 01:29:20,323 StartupChecks.java:204 - jemalloc seems to be preloaded from /usr/local/lib/libjemalloc.so
WARN  [main] 2023-05-05 01:29:20,323 StartupChecks.java:258 - JMX is not enabled to receive remote connections. Please see cassandra-env.sh for more info.
INFO  [main] 2023-05-05 01:29:20,335 SigarLibrary.java:46 - Initializing SIGAR library
WARN  [main] 2023-05-05 01:29:20,354 SigarLibrary.java:172 - Cassandra server running in degraded mode. Is swap disabled? : false,  Address space adequate? : true,  nofile limit adequate? : true, nproc limit adequate? : true 
WARN  [main] 2023-05-05 01:29:22,480 StartupChecks.java:493 - Maximum number of memory map areas per process (vm.max_map_count) 65530 is too low, recommended value: 1048575, you can change it with sysctl.
```

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