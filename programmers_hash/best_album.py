

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
    return final
    # return answer

genres = ["classic", "pop", "classic", "classic"]
plays = [500, 600, 150, 800]

solution(genres, plays)