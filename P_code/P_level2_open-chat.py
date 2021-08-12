def solution(record):
    answer = []
    user = {}
    compiler = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for re in record:
        resplit = list(map(str, re.split()))
        if resplit[0] in ['Enter','Change']:
            user[resplit[1]] = resplit[2]
    for re in record:
        resplit = list(map(str, re.split()))
        if resplit[0] != "Change":
            answer.append(user[resplit[1]]+compiler[resplit[0]])
    return answer

def solution2(record):
    answer = []
    user = {}
    for re in record:
        resplit = list(map(str,re.split()))
        if resplit[0] == "Enter":
            user.update({resplit[1]:resplit[2]})
            if resplit[1] in user:
                del user[resplit[1]]
                user.update({resplit[1]: resplit[2]})
        elif resplit[0] == "Change":
            del user[resplit[1]]
            user.update({resplit[1]:resplit[2]})

    for status in record:
        st = list(map(str, status.split()))
        if st[0] == "Enter":
            answer.append(user[st[1]]+"님이 들어왔습니다.")
        elif st[0] == "Leave":
            answer.append(user[st[1]]+"님이 나갔습니다.")
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))