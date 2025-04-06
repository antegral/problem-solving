import copy

def solution(friends, gifts):
    templete = {}
    for user in friends:
        templete[user] = 0     

    # 받은 선물 테이블 생성
    recv_table = {}
    for user in templete:
        recv_table[user] = copy.deepcopy(templete)
        del recv_table[user][user]
        
    for transection in gifts:
        parsed = transection.split(" ")
        user_from = parsed[0]
        user_to = parsed[1]
    
        # user_to의 선물 수신 카운트 올리기
        recv_table[user_to][user_from] += 1

    # 선물지수 테이블 생성
    result_table = {}
    for user in friends:
        result_table[user] = {
            "send_gift": 0,
            "recv_gift": 0,
            "gift_index": 0,
        }

    
    # 선물지수 테이블 채우기
    result = copy.deepcopy(templete)
    for user in recv_table:
        for e in recv_table[user]:
            # 선물 지수 테이블 완성하기
            result_table[user]["recv_gift"] += recv_table[user][e]
            result_table[e]["send_gift"] += recv_table[user][e]
                    
    # 선물지수 계산
    for user in result_table:
        gift_idx = result_table[user]["send_gift"] - result_table[user]["recv_gift"]
        result_table[user]["gift_index"] = gift_idx
        
    
    nextGiftTransection = []
    for user in recv_table:
        for e in recv_table[user]:
            a = user + " " + e
            b = e + " " + user
            if a in nextGiftTransection or b in nextGiftTransection:
                continue
                
            # 조건1. 서로 주고받는 경우 계산
            # user 수신함에 e가 선물 보낸 카운트가 있을 때
            if recv_table[user][e] != 0:
                # user가 e보다 선물을 더 많이 받았을 때
                if recv_table[user][e] > recv_table[e][user]:
                    # 다음달에 user가 e에게 선물
                    result[e] += 1
                    nextGiftTransection.append(user + " " + e)
                    
            a = user + " " + e
            b = e + " " + user
            if a in nextGiftTransection or b in nextGiftTransection:
                continue
                    
            ## 조건2. 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같을 때
            if recv_table[user][e] == recv_table[user][e]: 
                if result_table[user]["gift_index"] > result_table[e]["gift_index"]:
                    result[user] += 1 # e와 비교하여 User의 선물지수가 더 높으므로 선물 받음
                    nextGiftTransection.append(user + " " + e)
    
    max = 0
    for user in result:
        if max < result[user]:
            max = result[user]

    return max