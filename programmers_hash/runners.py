def solution(participant, completion):

    completion.append("하하하 한국어는 마지막")
    participant.sort()
    completion.sort()
    for participant, completion in zip(participant, completion):
        if participant!=completion:
            return participant
            break 
        else:
             pass