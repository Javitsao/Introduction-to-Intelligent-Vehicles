import random
import math

# Function to calculate the worst-case response time for a message
def calculate_response_time(i, priorities, transmission_times, periods):
    higher_priority_tasks = [j for j in range(len(priorities)) if priorities[j] < priorities[i]]
    interference = sum(math.ceil(periods[i] / periods[j]) * transmission_times[j] for j in higher_priority_tasks)
    response_time = transmission_times[i] + interference
    return response_time

# Objective function to minimize the summation of the worst-case response times
def objective_function(priorities, transmission_times, periods):
    return sum(calculate_response_time(i, priorities, transmission_times, periods) for i in range(len(priorities)))

# Function to generate a neighbor solution
def generate_neighbor(priorities):
    a, b = random.sample(range(len(priorities)), 2)
    new_priorities = list(priorities)
    new_priorities[a], new_priorities[b] = new_priorities[b], new_priorities[a]
    return new_priorities

# Simulated Annealing algorithm
def simulated_annealing(initial_priorities, transmission_times, periods, tau, max_time):
    current_priorities = initial_priorities
    best_priorities = list(initial_priorities)
    current_cost = objective_function(current_priorities, transmission_times, periods)
    best_cost = current_cost
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    start_time = time.time()

    while T > T_min:
        if time.time() - start_time > max_time:
            break
        i = 1
        while i <= 100:
            new_priorities = generate_neighbor(current_priorities)
            new_cost = objective_function(new_priorities, transmission_times, periods)
            if new_cost < best_cost and all(calculate_response_time(i, new_priorities, transmission_times, periods) <= periods[i] for i in range(len(new_priorities))):
                best_priorities = new_priorities
                best_cost = new_cost
            acceptance_probability = math.exp((current_cost - new_cost) / (T * tau))
            if new_cost < current_cost or random.random() < acceptance_probability:
                current_priorities = new_priorities
                current_cost = new_cost
            i += 1
        T = T * alpha

    return best_priorities, best_cost

# Benchmark data
n = 17
tau = 0.002
messages = [
    (0, 0.52, 50),
    (1, 0.60, 5),
    (2, 0.52, 5),
    (3, 0.60, 5),
    (4, 0.52, 5),
    (5, 0.60, 5),
    (6, 0.92, 10),
    (7, 0.52, 10),
    (8, 0.60, 10),
    (9, 0.68, 10),
    (10, 0.52, 50),
    (11, 0.76, 100),
    (12, 0.52, 100),
    (13, 0.52, 100),
    (14, 0.68, 1000),
    (15, 0.52, 1000),
    (16, 0.52, 1000)
]

# Extract initial priorities, transmission times, and periods
initial_priorities = [msg[0] for msg in messages]
transmission_times = [msg[1] for msg in messages]
periods = [msg[2] for msg in messages]

# Run Simulated Annealing
import time
start_time = time.time()
best_priorities, best_cost = simulated_annealing(initial_priorities, transmission_times, periods, tau, 15)

# Print out the results
for priority in best_priorities:
    print(priority)
print(best_cost)