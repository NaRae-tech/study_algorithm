import re
def timecheck(start, end):
    st = list(map(int, start.split(':')))
    en = list(map(int, end.split(':')))
    if en[1]<st[1]:
        en[0]-=1
        en[1]+=60
    return (en[0]-st[0])*60+(en[1]-st[1])

def musiccheck(melody):
    for i in range(len(melody)):
        if '#' in melody[i]:
            melody[i] = melody[i][0].lower()
    return ''.join(melody)

def solution(m,musicinfos):
    info = []
    timelab=[]
    melody = re.findall('[\w][#]?',m)
    me = musiccheck(melody)

    for exam in musicinfos:
        start,end,title,music = exam.split(',')
        time = timecheck(start,end)
        score = re.findall('[\w][#]?',music)
        sc = musiccheck(score)

        if len(score)<time:
            temp = time//len(sc)
            sc=sc*temp+sc[:(time-temp*len(sc))]
        else:
            sc = sc[:time]

        if me in sc:
            info.append([title,time])
    if not info:
        return "(None)"
    else:
        info = sorted(info,key=lambda x:-x[1])
        return info[0][0]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,musicinfos))