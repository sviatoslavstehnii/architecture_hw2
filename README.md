
# Hazelcast Distributed Systems Lab

## Overview  
This lab demonstrates the use of Hazelcast for distributed computing with Python. It includes examples of distributed maps, queues, and concurrency control using optimistic and pessimistic locking. The Hazelcast node is run via console commands, and the Python client interacts with it.

## Setup  

### 1. Install Dependencies  
Create a virtual environment and install Hazelcast's Python client:  
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install hazelcast-python-client
```

### 2. Start Hazelcast Node  
Run the Hazelcast node using the provided configuration file:  
```bash
hz start --config=hazelcast.xml
```

## Files Description  

- **`hazelcast.xml`** - Configuration file for the Hazelcast cluster.  
- **`distributed_map.py`** - Demonstrates how to use a Hazelcast distributed map in Python.  
- **`increment.py`** - Basic example of distributed counter incrementing.  
- **`optimistic_lock_increment.py`** - Implements optimistic locking while updating shared data.  
- **`pessimistic_lock_increment.py`** - Demonstrates pessimistic locking in a distributed system.  
- **`queue_put.py`** - Adds items to a Hazelcast distributed queue.  
- **`queue_get.py`** - Retrieves items from the distributed queue.  

## Running Examples  

After starting the Hazelcast node, you can run the Python scripts to interact with it:  

### Distributed Map  
```bash
python distributed_map.py
```

### Queue Operations  
Put an item in the queue:  
```bash
python queue_put.py
```
Get an item from the queue:  
```bash
python queue_get.py
```

### Concurrency Control  
Optimistic Locking:  
```bash
python optimistic_lock_increment.py
```
Pessimistic Locking:  
```bash
python pessimistic_lock_increment.py
```

## Notes  
- Ensure that the Hazelcast node is running before executing the scripts.  
- The Python client connects to the node automatically based on the `hazelcast.xml` configuration.  
