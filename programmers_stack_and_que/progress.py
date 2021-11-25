


def solution(progresses, speeds):
    pointer = 0
    taskday = 0
    final = []
    for i, task in enumerate(progresses):
        if taskday != 0:
            if  100 - task <= speeds[i]*taskday:
                pointer += 1
                
            else:
                final.append(pointer)
                pointer = 0
                taskday = (100 - task)//speeds[i] if (100-task)%speeds[i] == 0 else (100 - task)//speeds[i]+1
                pointer +=1
                       
        else:
            taskday = (100 - task)//speeds[i] if (100-task)%speeds[i] == 0 else (100 - task)//speeds[i]+1
            pointer +=1 

        if i ==  len(progresses)-1:
                final.append(pointer)  
    return final





# progresses = [93, 30, 55]
progresses =  [80, 99, 70, 90, 50, 90]
# progresses = np.random
# speeds = [1, 30, 5]
speeds = [15, 100, 2, 3, 1, 1]
#return [1, 3, 2]
solution(progresses, speeds)