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

# Start Incrementing
start_time = time.time()

for _ in range(NUM_ITERATIONS):
    value = distributed_map.get(KEY)  # Read current value
    new_value = value + 1  # Increment
    distributed_map.put(KEY, new_value)  # Write back

end_time = time.time()

# Print execution time
print(f"Finished in {end_time - start_time:.2f} seconds.")

# Retrieve final value
final_value = distributed_map.get(KEY)
print(f"Final value in '{KEY}': {final_value}")

client.shutdown()
