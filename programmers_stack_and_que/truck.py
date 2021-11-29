from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     bridge = deque(maxlen=bridge_length)
#     all = 0
#     idx = 0
#     for truck in truck_weights:
#         if bridge == [] or all + truck < weight:
#             bridge.append(truck)
#             if bridge_length == 1:
#                 all = 0
#             elif len(bridge)==1:
#                 all = bridge[-1]
#             else:
#                 all = sum(list(bridge)[1:])
#             idx += 1
#         else: 
#             while all + truck >= weight:
#                 bridge.append(0)
#                 if bridge_length == 1:
#                     all = 0
#                 elif len(bridge)==1:
#                     all = bridge[-1]
#                 else:
#                     all = sum(list(bridge)[1:])
#                 idx += 1
#             bridge.append(truck)
#             if bridge_length == 1:
#                  all = 0
#             elif len(bridge)==1:
#                 all = bridge[-1]
#             else:
#                 all = sum(list(bridge)[1:])
#             idx += 1

    # return idx + bridge_length

def solution(bridge_length, weight, truck_weights):
    bridge = deque(maxlen=bridge_length)
    all = 0
    idx = 0
    for truck in truck_weights:
        if bridge_length==1:
            bridge.append(truck)
            idx += 1
            
        elif bridge_length>1:
            while all_(bridge) + truck > weight:
                bridge.append(0)
                idx += 1
            bridge.append(truck)
            idx += 1
            
    return idx + bridge_length

def all_(bridge, all = 0):
    if len(bridge) == 0:
        all = 0
    elif len(bridge) == 1:
        all = bridge[-1]
    elif len(bridge) > 1:
        all = sum(list(bridge)[1:])
    return all 



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)
print(solution(bridge_length, weight, truck_weights)
)