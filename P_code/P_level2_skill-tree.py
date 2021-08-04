def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        temp = ""
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                temp+=skill_trees[i][j]
        skill_trees[i] = temp

    can_skill = []
    for i in range(0,len(skill)+1):
        temp = skill[:i]
        can_skill.append(temp)

    for i in range(0, len(skill_trees)):
        if skill_trees[i] in can_skill:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))