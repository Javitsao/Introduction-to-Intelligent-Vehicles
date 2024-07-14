import math
import random
def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        tau = float(lines[1])
        messages = []
        for line in lines[2:]:
            parts = line.strip().split()
            priority = int(parts[0])
            transmission_time = float(parts[1])
            period = int(parts[2])
            messages.append((priority, transmission_time, period))
        return n, tau, messages

def findworstcase(n, tau, messages):
    print("Number of messages:", n)
    print("Tau:", tau)
    min_sum = 1000
    min_message = None
    num_iterations = 1280000
    for _ in range(num_iterations):  # Replace 5 with the number of times you want to execute the loop
        priorities = [priority for priority, _, _ in messages]
        rest_of_messages = [(transmission_time, period) for _, transmission_time, period in messages]
        # Shuffle the priorities
        random.shuffle(priorities)
        # Reconstruct the messages with shuffled priorities
        shuffled_messages = [(priority,) + rest for priority, rest in zip(priorities, rest_of_messages)]
        #sorted_messages = sorted(shuffled_messages, key=lambda message: message[0])
        #print(shuffled_messages)
        #print("shuffled_messages:")
        final_sum = 0
        for i, (priority, transmission_time, period) in enumerate(shuffled_messages):
            #print(f"Message {i+1}: Priority={priority}, Transmission Time={transmission_time}, Period={period}")
            max = 0
            for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                if priority_1 >= priority:
                    if transmission_time_1 > max:
                        max = transmission_time_1
            #print(max)
            sum = 0
            q = max
            for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                if priority_1 < priority:
                    sum += math.ceil((q + tau) / period_1) * transmission_time_1
            while(q != max + sum and (max + sum + transmission_time) <= period):
                q = max + sum
                sum = 0
                for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                    if priority_1 < priority:
                        #print((q + tau) / period_1)
                        sum += math.ceil((q + tau) / period_1) * transmission_time_1
            if (max + sum + transmission_time) > period:
                #print("invalid")
                final_sum = -1
                break
            else:
                #print(f"{(q + transmission_time):.2f}")
                final_sum += q + transmission_time
        #print(f"Final sum: {final_sum:.2f}")
        if final_sum != -1 and final_sum < min_sum:
            min_sum = final_sum
            min_message = [pr[0] for pr in shuffled_messages]
    print(f"Minimum sum: {min_sum:.2f}")
    print(f"Priority with minimum sum: {min_message}")
            
input_filename = "input.dat"
n, tau, messages = read_input_file(input_filename)
findworstcase(n, tau, messages)