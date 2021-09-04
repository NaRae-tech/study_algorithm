import re
def solution(files):
    answer = []
    num = [re.split(r"([0-9]+)",f) for f in files]
    splitsort= sorted(num, key = lambda x:(x[0].lower(), int(x[1])))
    for f in splitsort:
        answer.append("".join(f))
    return answer

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))