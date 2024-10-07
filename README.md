# Introduction-to-Intelligent-Vehicles
## CAN Protocol Timing Analysis (hw1):

This program analyzes the worst-case response time (Ri) of messages in a Controller Area Network (CAN) protocol according to the provided benchmark "input.dat".

#### Requirements:

- The benchmark file format is as follows:
    - The first line contains two numbers separated by a space:
        - `n`: Number of messages in the benchmark
        - `τ`: Arbitration time of a CAN message
    - Each subsequent line contains three numbers separated by spaces:
        - `Pi`: Priority of the message (higher number = higher priority)
        - `Ci`: Transmission time of the message (including data, overhead, and synchronization bits)
        - `Ti`: Period of the message (time between message transmissions)

#### Functionality:

1. **Worst-Case Response Time Calculation:**
    - The program calculates the worst-case response time (Ri) for each message.
    - This represents the maximum time a message can wait before being successfully transmitted.
2. **Output:**
    - The program prints `n` lines, where each line represents the worst-case response time (Ri) of a corresponding message in the benchmark order.

## Simulated Annealing for CAN Priority Assignment (hw2)

This program utilizes Simulated Annealing to optimize message priorities in a Controller Area Network (CAN) protocol, aiming to minimize the total worst-case response time.

#### Requirements:

- The benchmark file format is identical to the previous CAN Protocol Timing Analysis.

#### Objective:

- Minimize the sum of worst-case response times (Ri) for all messages in the CAN network.

#### Constraints:

- Message priority (Pi):
    - Integer value between 0 and n-1 (n being the total number of messages)
    - Unique for each message
- Worst-case response time (Ri) must be less than or equal to the message's period (Ti).
- Initial priorities are provided in the benchmark file.
- Runtime should be less than 15 seconds.

#### Functionality:

1. **Simulated Annealing Optimization:**
    - The program employs Simulated Annealing to iteratively adjust message priorities.
    - It strives to minimize the total worst-case response time for all messages.
2. **Output:**
    - The program prints `n` lines, where each line represents the optimized priority (Pi) of a corresponding message in the benchmark order.
    - It then prints a single line indicating the best objective value (lowest total worst-case response time) achieved during the optimization process.
  
## Final Project

#### Introduction
This project addresses the scheduling problem for an intelligent vehicle rental company aiming to maximize profits. We propose a solution using **Mixed-Integer Linear Programming (MILP)** and a **heuristic algorithm** to handle rental orders across various stations with constraints such as car levels, employee working hours, and customer compensation for rejected orders. 

#### Methods

**1. MILP Approach**
- We formulated the scheduling problem as a MILP model.
- The objective was to maximize total profit while considering variables like car levels, order assignments, and vehicle transfer time between stations.
- MILP guarantees optimal solutions but is computationally expensive for large instances.

**2. Heuristic Approach**
- A heuristic algorithm was designed to handle large-scale problems more efficiently.
- The algorithm classifies and assigns orders based on car levels, pickup times, and allows transfers and upgrades to maximize scheduling efficiency.
- This method provides high-quality solutions quickly, making it practical for real-world applications.

#### Results
- **MILP:** Achieves the optimal solution but becomes computationally prohibitive for large datasets.
- **Heuristic:** Offers near-optimal solutions with an average gap of 1.81% from the optimal value while solving within a minute for large instances.

#### Conclusion
We successfully tackled the vehicle order scheduling problem by developing both an exact MILP model and a fast heuristic algorithm. The heuristic algorithm offers a practical trade-off between solution quality and computational time, making it suitable for real-world deployment in intelligent vehicle systems.
