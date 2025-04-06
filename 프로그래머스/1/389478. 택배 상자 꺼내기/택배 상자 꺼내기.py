import math

def solution(n, w, num):
    # 상자 레이어 만들기
    crate = []
    for i in range(1, math.ceil(n / w) + 1):
        isRequiredRev = i % 2 == 0 # 짝수번째 레이어면 뒤집음

        layer = [x for x in range(w * (i-1) + 1, w * i + 1)]
        
        if isRequiredRev:
            layer.reverse()

        crate.append(layer)
        
    print(crate)
    
    # 상자 좌표 찾기
    pos_x = 0
    pos_y = 0
    for i, layer in enumerate(crate):
        ok = False
        if ok:
            break
        for j, x in enumerate(layer):
            if num == x:
                ok = True
                pos_x = j
                pos_y = i
                break

    needRemoveBoxes = 0
    for i in range(pos_y, len(crate)):
        if crate[i][pos_x] <= n: # 위에 유효한 상자가 있는 경우
            needRemoveBoxes += 1
            
    return needRemoveBoxes