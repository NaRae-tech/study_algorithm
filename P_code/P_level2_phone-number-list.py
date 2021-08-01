def solution(phone_book):
    phone_book = sorted(phone_book, reverse=True)
    print(phone_book)
    for i in range(len(phone_book)-1):
        if(phone_book[i].startswith(phone_book[i+1])):
            return False
    return True

def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if(phone_book[i] in phone_book[i+1][0:len(phone_book)]):
            return False
    return True

phone_book = ["97674223", "1195524421","119"]
print(solution(phone_book))