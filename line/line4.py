import numpy as np


def solution(recs):
    def down(recs):
        recs_original= recs
        rec_maps = np.zeros((100,100), dtype=int)
        rec_list= sorted(recs, key = lambda x: x[1]) #우선순위
        for i, rec in enumerate(rec_list):
            while rec_list[i][1]!=0 and rec_maps[rec_list[i][1]][rec_list[i][3]]!=1:
                rec_list[i][1] -=1
                rec_list[i][3] -=1
            rec_maps[rec_list[i][1]][rec_list[i][3]]=1

    down(recs)







recs = [[0,2,1,3],[1,2,2,5],[3,3,4,4],[4,1,6,3],[1,6,5,7],[5,5,7,6],[5,8,6,10]]
solution(recs)