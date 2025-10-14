import heapq

tasks = []
heapq.heappush(tasks, (1, "Low Priority"))
heapq.heappush(tasks, (3, "High Priority"))
heapq.heappush(tasks, (2, "Medium Priority"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing: {task} (Priority {priority})")
print("All tasks processed.")