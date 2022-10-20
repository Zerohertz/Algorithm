from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    tmp = deque([0 for _ in range(bridge_length)])
    tmpw = 0
    while tmp:
        time += 1
        tmpw -= tmp.popleft()
        if truck_weights:
            if tmpw + truck_weights[0] <= weight:
                tmpw += truck_weights[0]
                tmp.append(truck_weights.popleft())
            else:
                tmp.append(0)
    return time