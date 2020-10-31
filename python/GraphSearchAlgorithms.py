import numpy as np
import networkx as nx
from plotly.offline import plot
import pandas as pd
from queue import Queue, PriorityQueue
import operator

##                     A B C D E F G H I L M N O P R S T U V Z 
array = np.array(   [ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,140,118,0,0,75), # Arad
                      (0,0,0,0,0,211,90,0,0,0,0,0,0,101,0,0,0,85,0,0), # Bucharest
                      (0,0,0,120,0,0,0,0,0,0,0,0,146,138,0,0,0,0,0,0), # Craiova
                      (0,0,120,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0), # Dobreta
                      (0,0,0,0,0,0,0,86,0,0,0,0,0,0,0,0,0,0,0,0), # Eforie
                      (0,211,0,0,0,0,0,0,0,0,0,0,0,0,0,99,0,0,0,0), # Fagaras
                      (0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), # Girgiu
                      (0,0,0,0,86,0,0,0,0,0,0,0,0,0,0,0,0,86,0,0), # Hirsova
                      (0,0,0,0,0,0,0,0,0,0,0,87,0,0,0,0,0,0,92,0), # Iasi
                      (0,0,0,0,0,0,0,0,0,0,70,0,0,0,0,0,111,0,0,0), # Lugoj
                      (0,0,0,75,0,0,0,0,0,70,0,0,0,0,0,0,0,0,0,0), # Mehadia
                      (0,0,0,0,0,0,0,0,87,0,0,0,0,0,0,0,0,0,0,0), # Neamt
                      (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,151,0,0,0,171), # Oradea
                      (0,101,138,0,0,0,0,0,0,0,0,0,0,0,97,0,0,0,0,0), # Pitesti
                      (0,0,146,0,0,0,0,0,0,0,0,0,0,97,0,80,0,0,0,0), # Rimnicu Vilcea
                      (140,0,0,0,0,99,0,0,0,0,0,0,151,0,80,0,0,0,0,0), # Sibiu
                      (118,0,0,0,0,0,0,0,0,111,0,0,0,0,0,0,0,0,0,0), # Timisoara
                      (0,85,0,0,0,0,0,98,0,0,0,0,0,0,0,0,0,0,142,0), # Urziceni
                      (0,0,0,0,0,0,0,0,92,0,0,0,0,0,0,0,0,142,0,0), # Vaslui
                      (75,0,0,0,0,0,0,0,0,0,0,0,71,0,0,0,0,0,0,0)])# Zerind

#plotting.makeplot(array)

labels=["Arad","Bucharest","Criaova","Dobreta","Eforie","Fagaras","Girgiu","Hirsova","Iasi","Lugoj",
        "Mehadia","Neamt","Oradea","Pitesti","Rimicu Vilcea","Sibiu","Timisoara","Urzicenui","Vaslui","Zerind"]

heuristics = { 0:[366], 1:[0], 2:[160], 3:[242], 4:[161], 5:[178], 6:[77], 7:[151], 8:[226], 9:[244], 10:[241], 11:[234], 
              12:[380], 13:[98], 14:[193], 15:[253], 16:[329], 17:[80], 18:[199], 19:[374] }

def matrix_to_list(matrix):
    graph = {}
    weights = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
            key = str(i) + " " + str(j)
            weights.setdefault(key, [])
            weights[key].append(connected)
        graph[i] = adj
    return graph,weights

def weight(from_node, to_node):
    a = str(from_node) + " " + str(to_node)
    return weights.get(a)[0]

def bfs(graph, start,end):
  frontier = Queue()
  start = labels.index(start)
  end = labels.index(end)
  frontier.put((0,start))
  explored = []

  while True:
      if frontier.empty():
          raise Exception("No way Exception")
      cost, current_node = frontier.get()
      explored.append(current_node)
      print(labels[current_node],end = " ")
      if current_node == end:
         break

      for node in graph[current_node]:
         if node not in explored:
            frontier.put((cost + weight(current_node,node),node))
  return cost 

def ucs(graph, start, end, weights=None):
    
    frontier = PriorityQueue()
    start = labels.index(start)
    end = labels.index(end)
    frontier.put((0, start))
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")

        ucs_w, current_node = frontier.get()
        explored.append(current_node)
        print(labels[current_node],end = " -> ")
        if current_node == end:
            break

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((ucs_w + weight(current_node, node),node))
    return ucs_w 

def dfs(current_state, current_depth, end):
    global visit_order
    if current_depth < 0:
        return False
    else:
        visit_order.append(labels[current_state])
        if current_state == end:
            return True
        current_depth -= 1
        for next_state in graph[current_state]:
            if next_state not in visit_order:
                success = dfs(next_state, current_depth, end)
            if success == True:
                return True
        return False

def iddfs(start, end, max_depth):
    global visit_order
    start = labels.index(start)
    end = labels.index(end)
    for i in range(max_depth+1):
        visit_order = []
        success = dfs(start, i, end)
        prev = labels[start]
        cost = 0
        print("Iteration: " + str(i))
        for i in visit_order:
            print(i,end = " ->")
            cost = cost + weight(labels.index(prev),labels.index(i))
            prev = i
        print ("\nPath Found: " + str(success))
        if success == True:
            return True, i, cost
    return False, -1

def greedy_best_first_search(graph, start, end):
    
    frontier = PriorityQueue()
    start = labels.index(start)
    end = labels.index(end)
    frontier.put((heuristics.get(start)[0], start))  # (priority, node)
    explored = []
    cost = 0
    current_node = start
    
    while True:
        if frontier.empty():
            raise Exception("No way Exception")
        prev = current_node
        gbfs_w, current_node = frontier.get()
        explored.append(current_node)
        cost = cost + weight(prev,current_node)
        print(labels[current_node] + " heuristic value: " + str(gbfs_w),end = " -> ")
        if current_node == end:
            break

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((heuristics.get(node)[0],node))
    return cost

graph, weights= matrix_to_list(array)
cost_list = {}
print("\t\t****Breadth First Search path****")
cost_bfs = bfs(graph, 'Arad', 'Bucharest')
key = "Breadth First Search"
cost_list.setdefault(key, [])
cost_list[key].append(cost_bfs)
print(cost_bfs)
print("\t\t****Uniform Cost Search path****")
cost_ucs = ucs(graph, 'Arad', 'Bucharest', weights)
key = "Uniform Cost Search"
cost_list.setdefault(key, [])
cost_list[key].append(cost_ucs)
print(cost_ucs)
print("\t\t****Iterative Deepening Depth First Search path****")
cost_iddfs = iddfs('Arad', 'Bucharest', 3)
key = "Iterative Deepening DFS"
cost_list.setdefault(key, [])
if cost_iddfs[1] == -1:
    cost_list[key].append(cost_iddfs[1])
else:
    cost_list[key].append(cost_iddfs[2])
print(cost_iddfs)
print("\t\t****Greedy Best First Search path****")
cost_gbfs = greedy_best_first_search(graph, 'Arad', 'Bucharest')
key = "Greedy Best First Search"
cost_list.setdefault(key, [])
cost_list[key].append(cost_gbfs)
print(cost_gbfs)

print("Ascending Order of Cost")
cost_list = sorted(cost_list.items(), key=operator.itemgetter(1))
print(cost_list)
