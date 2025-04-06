def solution(wallpaper):
    left_upper = [60, 60]
    right_lower = [-1, -1]
    
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[i])):
            if wallpaper[i][j] != "#":
                continue

            if i < left_upper[0]:
                left_upper[0] = i
                
            if j < left_upper[1]:
                left_upper[1] = j
                
            if i + 1 > right_lower[0]:
                right_lower[0] = i + 1

            if j + 1 > right_lower[1]:
                right_lower[1] = j + 1
    
    return [left_upper[0], left_upper[1], right_lower[0], right_lower[1]]