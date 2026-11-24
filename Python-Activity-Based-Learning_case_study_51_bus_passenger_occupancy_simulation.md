# Case Study 51: Bus Passenger Occupancy Simulation

## 1. Problem Statement
Simulate passenger boarding and alighting counts across multiple bus stops, track live passenger occupancy at each stop, validate against negative occupancy errors, and flag any stops where bus capacity is exceeded.

## 2. Objectives
- To process stop-by-stop boarding and alighting records stored as tuples.
- To compute cumulative passenger occupancy at every stop along a route.
- To detect capacity violations and identify peak occupancy stops.

## 3. Assumptions
- The bus starts empty (0 passengers) before Stop 1.
- Maximum seating + standing capacity of the bus is specified by the user (e.g., 40 passengers).
- Alighting passengers cannot exceed the number of passengers currently onboard.

## 4. Algorithm
1. Start the program.
2. Input maximum bus capacity max_cap and number of stops n.
3. Read stop name, boarding count, and alighting count for each stop into tuples stored in stops_data.
4. Initialize current_passengers = 0, peak_passengers = 0, peak_stop = '', and violations = 0.
5. Loop through stops_data unpacking (stop_name, boarded, alighted):
6.   If alighted > current_passengers: report error and cap alighting at current_passengers.
7.   Update current_passengers = current_passengers - alighted + boarded.
8.   Check if current_passengers > max_cap; if so, increment violations and flag OVERLOAD.
9.   Track peak_passengers and peak_stop.
10. Print stop-by-stop occupancy log and summary statistics.
11. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
 / Input max_cap, n stops /
           |
           v
[ Store (stop_name, boarded, alighted) tuples ]
           |
           v
 < Unpack Stop Tuple > -- Done --> [ Print Peak & Violation Summary ]
           |                                      |
          Next                                    v
           |                                   [ End ]
           v
[ current = current - alighted + boarded ]
           |
           v
 < current > max_cap ? > -- Yes --> [ Flag Capacity Violation ]
           |
          No
           |
           v
[ Update Peak Occupancy ]
```

## 6. Pseudocode
```text
BEGIN
    READ max_cap, n
    SET stops = []
    FOR i FROM 1 TO n DO
        READ s_name, boarded, alighted
        APPEND (s_name, boarded, alighted) TO stops
    ENDFOR

    SET current = 0
    SET peak = 0
    SET violations = 0

    FOR EACH (s_name, boarded, alighted) IN stops DO
        IF alighted > current THEN
            SET alighted = current
        ENDIF
        SET current = current - alighted + boarded
        IF current > max_cap THEN
            SET violations = violations + 1
            PRINT s_name, current, "OVERLOAD"
        ELSE
            PRINT s_name, current, "OK"
        ENDIF
        IF current > peak THEN
            SET peak = current
        ENDIF
    ENDFOR

    PRINT peak, violations
END
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
- **Bus Capacity:** `40` passengers.
- **Stop 1 (Main Gate):** Board 25, Alight 0 -> Onboard = **25** (WITHIN LIMIT).
- **Stop 2 (Tech Park):** Board 22, Alight 5 -> Onboard = **42** (**OVERLOAD +2**).
- **Stop 3 (City Mall):** Board 8, Alight 15 -> Onboard = **35** (WITHIN LIMIT).
- **Stop 4 (Railway Station):** Board 0, Alight 35 -> Onboard = **0** (WITHIN LIMIT).

## 9. Sample Output
```text
Enter maximum bus passenger capacity: 40
Enter number of bus stops on the route: 4

Stop 1:
  Stop Name: Main Gate
  Passengers Boarding: 25
  Passengers Alighting: 0

Stop 2:
  Stop Name: Tech Park
  Passengers Boarding: 22
  Passengers Alighting: 5

Stop 3:
  Stop Name: City Mall
  Passengers Boarding: 8
  Passengers Alighting: 15

Stop 4:
  Stop Name: Railway Station
  Passengers Boarding: 0
  Passengers Alighting: 35

================ BUS OCCUPANCY SIMULATION REPORT ================
Bus Capacity Limit: 40 passengers
-----------------------------------------------------------------
Stop Name       | Alighted | Boarded | Onboard | Status
-----------------------------------------------------------------
Main Gate       |    0     |   25    |   25    | WITHIN LIMIT
Tech Park       |    5     |   22    |   42    | OVERLOAD (+2)
City Mall       |    15    |    8    |   35    | WITHIN LIMIT
Railway Station |    35    |    0    |    0    | WITHIN LIMIT
-----------------------------------------------------------------
Peak Occupancy      : 42 passengers at 'Tech Park'
Capacity Violations : 1 stop(s)
=================================================================
```

## 10. Conclusion
The simulation tracks cumulative passenger counts across stops using tuples and conditional checks, accurately flagging overcrowding and peak load points.
