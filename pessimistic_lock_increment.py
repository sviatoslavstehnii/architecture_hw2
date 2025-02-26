import hazelcast
import time

# Connect to Hazelcast Cluster
client = hazelcast.HazelcastClient()

# Get the distributed map
distributed_map = client.get_map("my-distributed-map").blocking()

# Number of iterations
NUM_ITERATIONS = 10_000
KEY = "counter"

# Ensure the key exists (only one client should initialize it)
if distributed_map.contains_key(KEY) is False:
    distributed_map.put(KEY, 0)

# Start Timing
start_time = time.time()

for _ in range(NUM_ITERATIONS):
    distributed_map.lock(KEY)  # Lock the key
    try:
        value = distributed_map.get(KEY)  # Read value
        distributed_map.put(KEY, value + 1)  # Increment and write
    finally:
        distributed_map.unlock(KEY)  # Unlock the key

end_time = time.time()

# Print execution time
print(f"Finished in {end_time - start_time:.2f} seconds.")

# Retrieve final value
final_value = distributed_map.get(KEY)
print(f"Final value in '{KEY}': {final_value}")

client.shutdown()
