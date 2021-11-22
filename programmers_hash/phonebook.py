def solution(phone_book):
    phone_book.sort()
    for j, first in enumerate(phone_book):
        try:
            if first == phone_book[j+1][:len(first)]:
                return False
            else:
                pass
        except:
            pass
    return True