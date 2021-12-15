# def solution(bridge_length, weight, truck_weights):
#     from collections import deque
    
#     bridge = deque([0 for _ in range(bridge_length)])
#     total_weight,step = 0,0
#     truck_weights = deque(truck_weights)

#     while truck_weights:
#         total_weight -= bridge.popleft()
#         if total_weight + truck_weights[0] > weight:
#             bridge.append(0)
#         else:
#             truck = truck_weights.popleft()
#             bridge.append(truck)
#             total_weight += truck
#         step += 1

#     step += bridge_length
#     return step
###################### 시간 복잡도는?

def solution(bridge_length, weight, truck_weights):
    from collections import deque

    second = deque([1])
    total_weight = deque([truck_weights.pop(0)])
    total,answer,sec = total_weight[0],0,1

    for i in truck_weights: # 트럭 입장!

        if i+total <= weight: # 트럭 입장 가능한가? 네! # 들어간 시간 1초, 추가된 무게 i를 처리한다.
                second.append(1)
                sec += 1
                total_weight.append(i)
                total += i

                if sec - second[0] == bridge_length: # 시간이 지난 결과 트럭이 나갔다면 처리
                    temp = second.popleft()
                    answer += temp
                    sec -= temp
                    total -= total_weight.popleft()

                continue

        while i+total > weight: # 다음 트럭이 들어가기 위한 무게를 마련한다. 통과할 최소한의 시간만 남기고 시간을 추가한다.
            total -= total_weight.popleft()
            temp = second.popleft()
            answer += temp
            sec -= temp

        total_weight.append(i) # 트럭 입장
        total += i

        temp = bridge_length-sec # 통과할 최소한의 시간을 더한다.
        second.append(temp)
        sec += temp

    answer += sec+bridge_length # 통과할 최소한의 시간을 더한다.

    return answer