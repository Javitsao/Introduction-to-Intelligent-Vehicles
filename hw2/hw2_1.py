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
    num_iterations = 1000000
    num_to_shuffle = 17
    for _ in range(num_iterations): 
        # Randomly select indices of the messages to shuffle
        indices_to_shuffle = random.sample(range(len(messages)), num_to_shuffle)
        
        # Extract the priorities to shuffle
        priorities_to_shuffle = [messages[i][0] for i in indices_to_shuffle]
        
        # Shuffle the selected priorities
        random.shuffle(priorities_to_shuffle)
        
        # Create a new list of messages with the shuffled priorities
        shuffled_messages = list(messages)  # Make a copy of the original messages
        for index, priority in zip(indices_to_shuffle, priorities_to_shuffle):
            # Replace the priority in the message while keeping the rest of the message intact
            shuffled_messages[index] = (priority,) + messages[index][1:]
        
        final_sum = 0
        for i, (priority, transmission_time, period) in enumerate(shuffled_messages):
            max_val = 0
            for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                if priority_1 >= priority:
                    if transmission_time_1 > max_val:
                        max_val = transmission_time_1
            sum = 0
            q = max_val
            for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                if priority_1 < priority:
                    sum += math.ceil((q + tau) / period_1) * transmission_time_1
            while(q != max_val + sum and (max_val + sum + transmission_time) <= period):
                q = max_val + sum
                sum = 0
                for j, (priority_1, transmission_time_1, period_1) in enumerate(shuffled_messages):
                    if priority_1 < priority:
                        sum += math.ceil((q + tau) / period_1) * transmission_time_1
            if (max_val + sum + transmission_time) > period:
                #print("invalid")
                final_sum = -1
                num_to_shuffle = min(num_to_shuffle + 1, 17)
                break
            else:
                final_sum += q + transmission_time
        #print(f"Final sum: {final_sum:.2f}")
        if final_sum != -1 and final_sum < min_sum:
            min_sum = final_sum
            min_message = [pr[0] for pr in shuffled_messages]
            num_to_shuffle = 2
    print(f"Minimum sum: {min_sum:.2f}")
    print(f"Priority with minimum sum: {min_message}")
            
input_filename = "input.dat"
n, tau, messages = read_input_file(input_filename)
findworstcase(n, tau, messages)

