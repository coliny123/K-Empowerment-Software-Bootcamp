def sorting_ary(ary):
    for j in range(1, len(ary)):
        for i in range(j, 0, -1):
            if ary[i-1][1] > ary[i][1]:
                ary[i-1], ary[i] = ary[i], ary[i-1]

    return ary




score_ary = [["민지", 90], ["혜린", 85],["혜인", 50], ["하니", 65], ["다니엘", 42], ["카리나", 95]]

print(f"정렬 전 : {score_ary}")
score_ary = sorting_ary(score_ary)
print(f"정렬 후 : {score_ary}")
print("##조편성")

for i in range(len(score_ary) // 2):
    print(f"{score_ary[i][0]} : {score_ary[len(score_ary)-1-i][0]}")