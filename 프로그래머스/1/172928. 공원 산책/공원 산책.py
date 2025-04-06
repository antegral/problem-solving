def solution(park, routes):
    dog = []
    park_size = [len(park) - 1, len(park[0]) - 1]

    for i in range(0, len(park)):
        j = park[i].find("S")
        if j == -1:
            continue
        dog = [i, j]

    for route in routes:
        direction, move = route.split(" ")
        prediction = [0, 0]

        if direction == "N":
            prediction = [dog[0] - int(move), dog[1]] 
        elif direction == "S":
            prediction = [dog[0] + int(move), dog[1]] 
        elif direction == "W":
            prediction = [dog[0], dog[1] - int(move)] 
        elif direction == "E":
            prediction = [dog[0], dog[1] + int(move)] 
            
        if prediction[0] < 0 or prediction[1] < 0:
            continue
        
        if prediction[0] > park_size[0] or prediction[1] > park_size[1]:
            continue
            
        isColision = False
        A = range(dog[0], prediction[0] + 1)
        B = range(dog[1], prediction[1] + 1)
        
        if dog[0] + 1 > prediction[0] + 1:
            A = range(prediction[0], dog[0])
            
        if dog[1] + 1 > prediction[1] + 1:
            B = range(prediction[1], dog[1])
        
        for i in A:
            if park[i][prediction[1]] == "X":
                isColision = True

        for i in B:
            if park[prediction[0]][i] == "X":
                isColision = True
            
        if isColision:
            continue
            
        dog = prediction
    return dog