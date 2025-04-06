def solution(name, yearning, photo):
    answer = []
    yearning_dict = {}

    for i in range(0, len(name)):
        yearning_dict[name[i]] = yearning[i]

    for persons in photo:
        score = 0
        for person in persons:
            if not yearning_dict.get(person):
                continue
            score += yearning_dict[person]
        answer.append(score)

    return answer