import math

a, b, v = map(int, input().split())
# a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

day = math.ceil((v-a)/(a-b)) + 1

# 나무높이에서 마지막 날에 올라간 거리를 뺀 수에서 a-b를 나누면 마지막에 a만큼 올라간 하루를 제외한 날짜를 구할 수 있다. (그후에 +1 을해줌)

# 원래식으로는 v = (a-b) * n + a

# a만큼 올랐다 b만큼 떨어지기를 반복하기 때문에 a-b의 거리만큼 올라가는 것을 n만큼 반복하고 마지막 날에는 a만큼 올라가고서 더 이상 떨어지지 않기 때문에

print(day)
