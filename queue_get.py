import hazelcast
import time

# Connect to Hazelcast Cluster
client = hazelcast.HazelcastClient()

# Get the distributed queue
queue = client.get_queue("my-bounded-queue").blocking()

# Read values from the queue
while True:
    item = queue.take()  # This will block if the queue is empty
    print(f"Read: {item}")
    time.sleep(1)  # Simulate some processing time

client.shutdown()