import matplotlib.pyplot as plt
import random
from itertools import permutations
from math import sqrt
import time

# path의 길이를 리턴하는 함수
def path_length(graph, path):
    sum = 0
    cur = 0
    for p in path:
        sum += graph[cur][p]
        cur = p
    return sum + graph[cur][0]

# 무차별 대입으로 구하기
def bruth_force(graph):
    # n = 도시의 개수
    n = len(graph)
    solution = [0]
    minimum = float('inf')

    # 모든 path의 총 길이를 구하고 가장 짧은 경로 선택
    path = min(permutations(range(1,n)), key=lambda x: path_length(graph, x))
    return [0]+list(path)+[0], path_length(graph, path)

# NN 알고리즘
def nearest_neighbor_tsp(graph):
    n = len(graph)
    visited = [False] * n
    tour = []
    
    # 방문하지 않는 도시 중 가장 가까운 도시 구하기
    def nearest(current):
        nearest_city = None
        min_dist = float('inf')
        for next_city in range(n):
            if not visited[next_city] and graph[current][next_city] < min_dist:
                min_dist = graph[current][next_city]
                nearest_city = next_city
        return nearest_city
    
    current_city = 0
    visited[current_city] = True
    tour.append(current_city)
    

    near_minimun = 0
    for _ in range(n - 1):
        next_city = nearest(current_city)
        near_minimun += graph[current_city][next_city]
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city
    
    near_minimun += graph[current_city][0]
    tour.append(tour[0])  # 처음 도시로 돌아가기
    return tour, near_minimun

n = 10
x = [4, 9, 18, 14, 7, 7, 4, 17, 12, 1]
y = [2, 13, 11, 13, 19, 2, 9, 8, 11, 6]
dots = list(zip(x,y))

graph = list(map(lambda x:list(
    map(lambda y:sqrt((dots[x][0]-dots[y][0])**2 + (dots[x][1]-dots[y][1])**2), range(n)
)), range(n)))

solution, path_len = nearest_neighbor_tsp(graph)

# Create a plot
plt.figure(figsize=(6, 6))
for i in range(10):
    plt.text(x[i], y[i], str(i + 1), fontsize=12, ha='center', va='center', color='b')

ggx = []
ggy = []
for t in solution:
    ggx.append(x[t])
    ggy.append(y[t])

plt.plot(ggx, ggy, color='r', linestyle='-', linewidth=1)

plt.title("NN Solution")
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
    
