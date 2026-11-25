# **CASE STUDY 51: BUS PASSENGER OCCUPANCY SIMULATION**

## **1. Problem Statement**

To develop a Python program that simulates passenger boarding and alighting at multiple bus stops. The program calculates the total number of passengers onboard, checks bus capacity, detects invalid alighting counts, and identifies the peak passenger occupancy.

## **2. Objectives**

1. To store passenger details using tuples.
2. To calculate passenger occupancy at each bus stop.
3. To detect invalid alighting counts.
4. To identify bus capacity violations.
5. To find the peak passenger occupancy and the corresponding stop.

## **3. Algorithm**

1. Start the program.
2. Input maximum bus capacity and number of stops.
3. Read stop name, boarding count, and alighting count.
4. Store the details as tuples in a list.
5. Initialize current passengers, peak passengers, peak stop, and violation count.
6. Read each stop's tuple.
7. Check whether alighting passengers exceed current passengers.
8. If invalid, adjust the alighting count to current passengers.
9. Calculate current passenger occupancy.
10. Check whether occupancy exceeds maximum bus capacity.
11. If exceeded, display OVERLOAD and increase violation count.
12. Otherwise, display WITHIN LIMIT.
13. Update peak passenger count and peak stop.
14. Display the final occupancy report and summary.
15. Stop the program.

## **4. Flowchart**

## CASE STUDY 51: BUS PASSENGER OCCUPANCY SIMULATION

### Flowchart – Box Model Format

text

```text
              ┌───────────────┐
              │     START     │
              └───────┬───────┘
                      │
                      ▼
          ╱────────────────────────╲
         ╱  Input max_cap and n     ╲
         ╲                          ╱
          ╲───────────┬────────────╱
                      │
                      ▼
          ┌────────────────────────┐
          │ Initialize stops_data │
          │        = []            │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Input stop name,       │
          │ boarded and alighted   │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Store details as       │
          │ (name, boarded,        │
          │ alighted) tuple        │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Initialize current=0,  │
          │ peak=0, violations=0   │
          └───────────┬────────────┘
                      │
                      ▼
                ╱──────────────╲
               ╱  Process next  ╲
               ╲   stop tuple   ╱
                ╲──────┬───────╱
                       │
                       ▼
                ◇────────────────◇
               ╱ Is alighted >    ╲
               ╲ current?         ╱
                ◇──────┬─────────◇
                   YES │     NO
                       │       │
                       ▼       │
             ┌────────────────┐│
             │ Adjust alighted││
             │ = current      ││
             └───────┬────────┘│
                     │         │
                     └────┬────┘
                          │
                          ▼
          ┌────────────────────────┐
          │ current = current      │
          │ - alighted + boarded   │
          └───────────┬────────────┘
                      │
                      ▼
                ◇────────────────◇
               ╱ Is current >     ╲
               ╲ max_cap?         ╱
                ◇──────┬─────────◇
                   YES │     NO
                       │       │
                       ▼       ▼
          ┌────────────────┐ ┌────────────────┐
          │ Display        │ │ Display        │
          │ OVERLOAD       │ │ WITHIN LIMIT   │
          │ violations += 1│ └───────┬────────┘
          └───────┬────────┘         │
                  │                  │
                  └────────┬─────────┘
                           │
                           ▼
          ┌────────────────────────┐
          │ Update peak occupancy  │
          │ and peak stop          │
          └───────────┬────────────┘
                      │
                      ▼
                ◇────────────────◇
               ╱ Are all stops    ╲
               ╲ processed?       ╱
                ◇──────┬─────────◇
                   NO  │     YES
                       │       │
                       │       ▼
                       │  ┌─────────────────────┐
                       │  │ Print peak          │
                       │  │ occupancy, peak    │
                       │  │ stop and violations│
                       │  └──────────┬──────────┘
                       │             │
                       │             ▼
                       │      ┌───────────────┐
                       │      │     STOP      │
                       │      └───────────────┘
                       │
                       └──────► Process
                                next stop
```




## **5. Pseudocode**

```
BEGIN
    READ max_cap, n
    SET stops_data = []

    FOR i FROM 1 TO n DO
        READ s_name, boarded, alighted
        APPEND (s_name, boarded, alighted)
        TO stops_data
    ENDFOR

    SET current = 0
    SET peak = 0
    SET peak_stop = ""
    SET violations = 0

    FOR EACH (s_name, boarded, alighted)
    IN stops_data DO

        IF alighted > current THEN
            SET alighted = current
        ENDIF

        SET current = current - alighted + boarded

        IF current > max_cap THEN
            INCREMENT violations
            PRINT "OVERLOAD"
        ELSE
            PRINT "WITHIN LIMIT"
        ENDIF

        IF current > peak THEN
            SET peak = current
            SET peak_stop = s_name
        ENDIF
    ENDFOR

    PRINT peak, peak_stop, violations
END
```

## **6. Python Source Code**

```
# Case Study 51: Bus Passenger Occupancy Simulationmax_cap = int(input("Enter maximum bus passenger capacity: "))n = int(input("Enter number of bus stops: "))stops_data = []for i in range(1, n + 1):    print(f"\nStop {i}:")    s_name = input("Stop Name: ").strip()    boarded = int(input("Passengers Boarding: "))    alighted = int(input("Passengers Alighting: "))    stops_data.append((s_name, boarded, alighted))current_passengers = 0peak_passengers = 0peak_stop = ""violation_count = 0print("\n========== BUS OCCUPANCY REPORT ==========")print("Stop Name       | Alighted | Boarded | Onboard | Status")for s_name, boarded, alighted in stops_data:    if alighted > current_passengers:        print("Invalid alighting count!")        alighted = current_passengers    current_passengers = current_passengers - alighted + boarded    if current_passengers > max_cap:        status = "OVERLOAD"        violation_count += 1    else:        status = "WITHIN LIMIT"    if current_passengers > peak_passengers:        peak_passengers = current_passengers        peak_stop = s_name    print(f"{s_name:<15} | {alighted:^8} | "          f"{boarded:^7} | {current_passengers:^7} | {status}")print("------------------------------------------")print("Peak Occupancy:", peak_passengers)print("Peak Stop:", peak_stop)print("Capacity Violations:", violation_count)print("==========================================")
```

## **7. Test Cases**

**Maximum Bus Capacity: 40 passengers**

| Bus Stop        | Boarded | Alighted | Onboard |
| --------------- | ------- | -------- | ------- |
| Main Gate       | 25      | 0        | 25      |
| Tech Park       | 22      | 5        | 42      |
| City Mall       | 8       | 15       | 35      |
| Railway Station | 0       | 35       | 0       |

## **8. Sample Output**

```
Enter maximum bus passenger capacity: 40
Enter number of bus stops: 4

========== BUS OCCUPANCY REPORT ==========

Stop Name       | Alighted | Boarded | Onboard | Status
Main Gate       |    0     |   25    |   25    | WITHIN LIMIT
Tech Park       |    5     |   22    |   42    | OVERLOAD
City Mall       |   15     |    8    |   35    | WITHIN LIMIT
Railway Station |   35     |    0    |    0    | WITHIN LIMIT

------------------------------------------
Peak Occupancy: 42
Peak Stop: Tech Park
Capacity Violations: 1
==========================================
```

## **9. Conclusion**

The Bus Passenger Occupancy Simulation successfully calculates the number of passengers at every bus stop using Python tuples and conditional statements. It detects invalid alighting counts, identifies overcrowding, and displays the peak occupancy and capacity violations.
