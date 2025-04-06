def solution(n, m, section):
    answer = 0;
    need_fill = section
    nf_cursor = 0

    idx = 0;
    i = need_fill[0];
    while i <= n:
        # 가장 끝에 있는 채움필요 위치에 대해 현재 위치가 작거나 같고,
        # 현재 위치가 다음 채움필요 위치를 이미 넘긴 경우
        while i <= need_fill[-1] and i > need_fill[nf_cursor]:
            nf_cursor += 1;

        # 현재 위치가 채움필요 위치에 있는 경우
        if i == need_fill[nf_cursor]:
            i += m;
            answer += 1;
            continue;

        i += 1;
        
    
    return answer