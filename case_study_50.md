# Case Study 50: Tuple-Based Route Distance Analysis

## 1. Problem Statement
Store a sequence of geographical route waypoints as (x, y) coordinate tuples, compute distances between successive waypoints using the Euclidean distance formula, calculate total route length, and identify the longest route segment.

## 2. Objectives
- To store 2D coordinates as tuples inside a route list.
- To unpack consecutive coordinate tuples and compute segment distances using arithmetic operators.
- To determine the total route distance and identify the longest individual segment.

## 3. Assumptions
- Coordinates (x, y) are expressed in kilometers on a planar grid.
- At least 2 waypoints are required to form a route.
- Distance between (x1, y1) and (x2, y2) is calculated as ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5.

## 4. Algorithm
1. Start the program.
2. Input number of waypoints n (validate n >= 2).
3. Initialize an empty list waypoints.
4. For i from 1 to n: input name, x, and y, and append tuple (name, x, y) to waypoints.
5. Initialize total_distance = 0.0, max_dist = -1.0, and longest_segment = ''.
6. Loop i from 0 to n - 2: unpack (name1, x1, y1) = waypoints[i] and (name2, x2, y2) = waypoints[i + 1].
7. Compute dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5, add to total_distance, and update max_dist if dist > max_dist.
8. Print segment breakdown, total distance, and longest segment.
9. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
  / Input n waypoints (>=2) /
           |
           v
[ Store (name, x, y) tuples in waypoints ]
           |
           v
 < Loop i = 0 to n - 2 > -- Done --> [ Print Total & Longest Segment ]
           |                                         |
          Next                                       v
           |                                      [ End ]
           v
[ Unpack waypoints[i] & waypoints[i+1] ]
           |
           v
[ Compute Euclidean dist & Update total / max ]
```

## 6. Pseudocode
```text
BEGIN
    READ n
    SET waypoints = []
    FOR i FROM 1 TO n DO
        READ name, x, y
        APPEND (name, x, y) TO waypoints
    ENDFOR

    SET total_dist = 0.0
    SET max_dist = -1.0
    SET longest_label = ""

    FOR i FROM 0 TO n - 2 DO
        SET (n1, x1, y1) = waypoints[i]
        SET (n2, x2, y2) = waypoints[i + 1]
        SET dist = ((x2 - x1) ^ 2 + (y2 - y1) ^ 2) ^ 0.5
        SET total_dist = total_dist + dist
        PRINT n1, "->", n2, dist
        IF dist > max_dist THEN
            SET max_dist = dist
            SET longest_label = n1 + " to " + n2
        ENDIF
    ENDFOR

    PRINT total_dist, longest_label, max_dist
END
```

## 7. Python Source Code
```python
# Case Study 50: Tuple-Based Route Distance Analysis

n = int(input("Enter number of waypoints along the route (minimum 2): "))
while n < 2:
    print("A route requires at least 2 waypoints.")
    n = int(input("Re-enter number of waypoints: "))

waypoints = []
for i in range(1, n + 1):
    print(f"\nWaypoint {i}:")
    label = input("  Location Name: ").strip()
    x = float(input("  X-coordinate (km): "))
    y = float(input("  Y-coordinate (km): "))
    waypoints.append((label, x, y))

total_distance = 0.0
max_segment_dist = -1.0
longest_segment = ""

print("
================ ROUTE SEGMENT ANALYSIS ================")
for i in range(n - 1):
    name1, x1, y1 = waypoints[i]
    name2, x2, y2 = waypoints[i + 1]

    segment_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    total_distance += segment_dist

    print(f"Segment {i + 1}: {name1} ({x1}, {y1}) -> {name2} ({x2}, {y2}) = {segment_dist:.2f} km")

    if segment_dist > max_segment_dist:
        max_segment_dist = segment_dist
        longest_segment = f"{name1} -> {name2}"

print("--------------------------------------------------------")
print(f"Total Route Distance : {total_distance:.2f} km")
print(f"Longest Segment      : {longest_segment} ({max_segment_dist:.2f} km)")
print("========================================================")
```

## 8. Test Cases
- **Waypoints:** `("Gate", 0, 0)`, `("Library", 3, 4)`, `("Hostel", 3, 16)`, `("Stadium", 8, 16)`
- **Segment 1:** `(0,0) -> (3,4)` = **5.00 km**
- **Segment 2:** `(3,4) -> (3,16)` = **12.00 km** (Longest Segment)
- **Segment 3:** `(3,16) -> (8,16)` = **5.00 km**
- **Total Route Distance:** **22.00 km**.

## 9. Sample Output
```text
Enter number of waypoints along the route (minimum 2): 4

Waypoint 1:
  Location Name: Gate
  X-coordinate (km): 0
  Y-coordinate (km): 0

Waypoint 2:
  Location Name: Library
  X-coordinate (km): 3
  Y-coordinate (km): 4

Waypoint 3:
  Location Name: Hostel
  X-coordinate (km): 3
  Y-coordinate (km): 16

Waypoint 4:
  Location Name: Stadium
  X-coordinate (km): 8
  Y-coordinate (km): 16

================ ROUTE SEGMENT ANALYSIS ================
Segment 1: Gate (0.0, 0.0) -> Library (3.0, 4.0) = 5.00 km
Segment 2: Library (3.0, 4.0) -> Hostel (3.0, 16.0) = 12.00 km
Segment 3: Hostel (3.0, 16.0) -> Stadium (8.0, 16.0) = 5.00 km
--------------------------------------------------------
Total Route Distance : 22.00 km
Longest Segment      : Library -> Hostel (12.00 km)
========================================================
```

## 10. Conclusion
Storing waypoints as tuples and using tuple unpacking simplifies pairwise coordinate geometry calculations and route segment comparisons.
