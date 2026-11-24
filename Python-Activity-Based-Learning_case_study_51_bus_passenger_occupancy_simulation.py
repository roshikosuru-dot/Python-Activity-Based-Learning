# Case Study 51: Bus Passenger Occupancy Simulation

max_cap = int(input("Enter maximum bus passenger capacity: "))
n = int(input("Enter number of bus stops on the route: "))

stops_data = []
for i in range(1, n + 1):
    print(f"\nStop {i}:")
    s_name = input("  Stop Name: ").strip()
    boarded = int(input("  Passengers Boarding: "))
    alighted = int(input("  Passengers Alighting: "))
    stops_data.append((s_name, boarded, alighted))

current_passengers = 0
peak_passengers = 0
peak_stop = ""
violation_count = 0

print("
================ BUS OCCUPANCY SIMULATION REPORT ================")
print(f"Bus Capacity Limit: {max_cap} passengers")
print("-----------------------------------------------------------------")
print("Stop Name       | Alighted | Boarded | Onboard | Status")
print("-----------------------------------------------------------------")

for s_name, boarded, alighted in stops_data:
    if alighted > current_passengers:
        print(f"  [Note: Adjusted alighting at {s_name} from {alighted} to {current_passengers}]")
        alighted = current_passengers

    current_passengers = current_passengers - alighted + boarded

    if current_passengers > max_cap:
        status = f"OVERLOAD (+{current_passengers - max_cap})"
        violation_count += 1
    else:
        status = "WITHIN LIMIT"

    if current_passengers > peak_passengers:
        peak_passengers = current_passengers
        peak_stop = s_name

    print(f"{s_name:<15} | {alighted:^8} | {boarded:^7} | {current_passengers:^7} | {status}")

print("-----------------------------------------------------------------")
print(f"Peak Occupancy      : {peak_passengers} passengers at '{peak_stop}'")
print(f"Capacity Violations : {violation_count} stop(s)")
print("=================================================================")
