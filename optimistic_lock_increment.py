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
    while True:
        value = distributed_map.get(KEY)  # Read value
        new_value = value + 1  # Increment value
        success = distributed_map.replace_if_same(KEY, value, new_value)  # Optimistic lock: replace only if the value has not changed
        if success:
            break  # Exit the retry loop if the update was successful

end_time = time.time()

# Print execution time
print(f"Finished in {end_time - start_time:.2f} seconds.")

# Retrieve final value
final_value = distributed_map.get(KEY)
print(f"Final value in '{KEY}': {final_value}")

client.shutdown()