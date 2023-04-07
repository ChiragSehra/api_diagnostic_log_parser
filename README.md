# Kibana log parser

## Shard information: ```shards.json```,

    - state of index could be 
        - UNASSIGNED: The shard is not currently assigned to any node in the cluster.
        - INITIALIZING: The shard is in the process of initializing on a node in the cluster.
        - RELOCATING: The shard is being moved from one node to another in the cluster.
        - STARTED: The shard is available and actively accepting requests.
        - POST_RECOVERY: The shard has completed recovery and is in the process of post-recovery operations.
        - CLOSED: The shard has been closed and is no longer accepting requests.

    - Extrac the size as well of the indexes. 
    - Count the number of shards with 0 size.

## Cluster stats: ```cluster_stats.json```
Contains `indices` and `nodes` information.

### Nodes
- nodes.count.total: Total count of nodes
 - nodes.count.data: Total data nodes
 - nodes.count.master: Total master nodes
 - nodes.version: Version of nodes
 - nodes.mem.total: Total Memory
 - nodes.mem.free: Free Memory
 - nodes.mem.used: Used Memory
 - nodes.mem.free_percent: Free Memory in %
 - nodes.mem.used_percent: Used Memory in %
 - nodes.jvm.mem.heap_used_in_bytes: JVM mem used in bytes
 - nodes.jvm.mem.heap_max_in_bytes: JVM mem max in bytes
 - JVM Memory Heap Indicator: division of above 2
 - nodes.fs.total: Total FS Memory
 - nodes.fs.free: Free FS Memory
 - nodes.fs.available: Available DS memory
 

### Indicies
- indices.count
- indices.shards.total
- indices.shards.primaries
- indices.shards.replication_factor
- indices.query_cache.memory_size

## Nodes Stats: `node_stats.json`
for each node:
- cluter_name
- nodes.{id}.name
- nodes.{id}ip
- nodes.{id}.indices.docs.count
- nodes.{id}.indices.shard_stats.total_count
- nodes.{id}.indices.indexing.is_throttled
- nodes.{id}.indices.