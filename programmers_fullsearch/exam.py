def solution(answers):
    def base_(answer,base):
        base_mul= base*(len(answer)//len(base))+base[:len(answer)%len(base)]
        return base_mul

    def matching(answer, base_mul):
        answer_match=0
        for i in range(len(answer)):
            if answer[i] == base_mul[i]:
                answer_match+=1
        return answer_match

    def winning(answer):
        base1=[1, 2, 3, 4, 5]
        base2=[2, 1, 2, 3, 2, 4, 2, 5]
        base3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        bases=[base1, base2, base3]
        base_score=[]
        for base in bases:
            base_score.append(matching(answer, base_(answer, base)))

        score_final=[]
        for i, score in enumerate(base_score):
            if score == (max(base_score)):
                score_final.append(i+1)
        return score_final

    return winning(answers)