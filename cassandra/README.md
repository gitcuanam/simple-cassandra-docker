
Follow the tutorial from 

Build image
```bash
docker build -t simple-cassandra-docker .
```

Run container
```bash
docker run --rm -d \
    -p 9042:9042 \
    -v $PWD/data:/var/lib/cassandra \
    --name simple-cassandra-docker \
    simple-cassandra-docker
```

```test
docker exec -it simple-cassandra-docker bash
cqlsh
USE some_keyspace;
```

[Stack Overflow: Init script for Cassandra with docker-compose](https://stackoverflow.com/questions/40443617/init-script-for-cassandra-with-docker-compose)

[Github Gist: Initializing a Cassandra Docker container with keyspace and data](https://gist.github.com/derlin/0d4c98f7787140805793d6268dae8440)