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
