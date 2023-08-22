def solution(arr):
    answer = []
    answer.extend(arr)

    if len(answer) > len(answer[0]):
        for i in range(len(answer)):
            answer[i].extend([0] * (len(answer) - len(answer[i])))

    elif len(answer[0]) > len(answer):
        for _ in range(len(answer[0]) - len(answer)):
            answer.append([0] * len(answer[0]))

    return answer

arr = [[11,11], [11,11]]
print(solution(arr))