import hazelcast

# Connect to Hazelcast Cluster
client = hazelcast.HazelcastClient()

# Get the distributed queue
queue = client.get_queue("my-bounded-queue").blocking()

# Write values 1 to 100 to the queue
for i in range(1, 101):
    queue.put(i)  # This will block if the queue is full
    print(f"Wrote: {i}")

client.shutdown()