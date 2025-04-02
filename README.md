# Mutual_Exclusion
Mutual Exclusion ensures that multiple processes do not enter the critical section (CS) simultaneously.  
- Essential for maintaining consistency in distributed systems.
- Used in OS, database systems, and multi-threading applications.

# Types of Mutual Exclusion
1. Centralized Approach - A single coordinator grants
access.

2. Distributed Approach - Processes coordinate without a
central entity.

3. Token-Based Approach - A token circulates among
processes to allow access.

#Ricart-Agrawala Algorithm
- A distributed mutual exclusion algorithm.

- Uses timestamped requests and message passing.

- Ensures fairness by granting access in order of
timestamps.

# Working of Ricart-Agrawala Algorithm
1. A process sends a request message to all other processes.

2. Other processes reply immediately if they are not in CS;
otherwise, they queue the request.

3. The process enters CS when all other processes have sent replies.

4. After execution, the process sends a release message to all waiting
processes.
