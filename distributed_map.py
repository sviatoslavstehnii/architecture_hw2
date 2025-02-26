import hazelcast

# Connect to the Hazelcast cluster
client = hazelcast.HazelcastClient()

# Create or get a distributed map
distributed_map = client.get_map("my-distributed-map").blocking()

# Insert 1000 key-value pairs
for i in range(1000):
    distributed_map.put(i, f"value-{i}")

print("Inserted 1000 values into the distributed map.")

# Retrieve and print a few values as a check
print("Value for key 0:", distributed_map.get(0))
print("Value for key 999:", distributed_map.get(999))

# Shutdown client
client.shutdown()
