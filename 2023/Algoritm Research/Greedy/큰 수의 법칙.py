# N == 입력받을 값들의 갯수
# M == 모든 값을 더할 수 있는 횟수
# K == 일정 값을 더할 수 있는 횟수
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수 를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력하여 받은 수들 정리하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 가장 작은 수 

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0 이라면 반복문 탈출
            break

        result += first
        m -= 1 # 더할 때 마다 1씩 빼기

    if m == 0: # m 이 0이라면 반복문 탈출
        break

    result += second # 두번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때 마다 1씩 빼기

print(result) # 최종답안 출력
print(len(data))