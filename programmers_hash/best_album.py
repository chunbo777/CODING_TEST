"""
album = {} #플레이수 딕셔너리 저장 
plays = {}
for index, genre, play in zip(genres, plays)
    if album[genre] not none:
        album[genre] = album[genre] + play
        plays.append()
    album[genre] =  play
# 재생 순서 많은 장르 순으로 정렬
sorted(album, key = lambda x : )
#재생 순서 많은 순으로 그 안에 들어가는 함수
def inner sort:


"""




def solution(genres, plays):
    album = {}
    playing = {}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if album.get(genre) != None:
            album[genre] = album[genre] + play
            if playing[genre].get(play) == None:
                playing[genre][play]=[index]
            else:
                playing[genre][play].append(index)
        else:
            album[genre] = play
            playing[genre] = {}
            playing[genre][play]=[index]
    sorted_list = sorted(list(album.items()), key = lambda x : x[1] , reverse =True) 
    final = []
    for genre, play in sorted_list:
        
        if len(sorted(list(playing[genre].items()), reverse = True)[0][1]) > 1: # 여러개가 있는 경우
            final.extend(sorted(sorted(list(playing[genre].items()), reverse = True)[0][1])[:2])
        else : 
            final.extend(sorted(list(playing[genre].items()), reverse = True)[0][1])
            try :
                final.extend(sorted(sorted(list(playing[genre].items()), reverse = True)[1][1])[:1])
            except:
                pass
    # return answer

genres = ["classic", "pop", "classic", "classic", "pop", "pop"]
plays = [500, 600, 150, 800, 2500, 2500]

solution(genres, plays)