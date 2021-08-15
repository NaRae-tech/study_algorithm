from collections import deque
def solution(cacheSize,cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.appendleft(city)
            if len(cache) > cacheSize:
                cache.pop()
            answer+=5
        else:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize,cities))