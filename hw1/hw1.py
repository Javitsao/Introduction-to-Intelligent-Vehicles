import math
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

input_filename = "input.dat"
n, tau, messages = read_input_file(input_filename)
print("Number of messages:", n)
print("Tau:", tau)
print("Messages:")
for i, (priority, transmission_time, period) in enumerate(messages):
    print(f"Message {i+1}: Priority={priority}, Transmission Time={transmission_time}, Period={period}")
    max = 0
    for j, (priority_1, transmission_time_1, period_1) in enumerate(messages):
        if priority_1 >= priority:
            if transmission_time_1 > max:
                max = transmission_time_1
    #print(max)
    sum = 0
    q = max
    for j, (priority_1, transmission_time_1, period_1) in enumerate(messages):
        if priority_1 < priority:
            sum += math.ceil((q + tau) / period_1) * transmission_time_1
    while(q != max + sum and (max + sum + transmission_time) <= period):
        q = max + sum
        sum = 0
        for j, (priority_1, transmission_time_1, period_1) in enumerate(messages):
            if priority_1 < priority:
                #print((q + tau) / period_1)
                sum += math.ceil((q + tau) / period_1) * transmission_time_1
    print(f"{(q + transmission_time):.2f}")
            
    
