import pandas as pd
import numpy as np
from collections import defaultdict
from queue import SimpleQueue
import math

def find_r1_and_r2(l: dict, A: np.array) -> dict:
    for row in A:
        l[row[0]][0] += 1
        l[row[1]][1] += 1
    return l

#Прямое управление, подчинение,косвенное управление и подчинение
def find_r1to4(l: dict, A: np.array) -> dict:
    for row in A:
        main = row[0]
        sub = row[1]
        l[main][0] += 1
        l[sub][1] += 1
        for subrow in A:
            if subrow[0] == sub:
                l[main][2] += 1
                l[subrow[1]][3] += 1
    return l

#Соподчинение
def find_r5(d: dict, A: np.array) -> dict:
    q = SimpleQueue()
    q.put(1)

    r5 = {}

    while not q.empty():
        main = q.get()
        l = []
        for row in A:
            if row[0] == main:
                l.append(row[1])
                q.put(row[1])
        if len(l) > 1:
            for elem in l:
                d[elem][4] += l.__len__() - 1

    return d

def task(graph: np.array) -> float:
    def set_def():
        return [0, 0, 0, 0, 0]

    l = defaultdict(set_def)

    find_r1to4(l, graph)
    find_r5(l, graph)

    l = pd.DataFrame(l) # здесь будут колонка -- объект, строка -- сотояние
    l = l.to_numpy().T # А здесь они снова перевернутся, строка -- объект

    print(f"Матрица связности графа A = \n{l}")

    n = len(l) # количество объектов

    s = 0.0 # сумма
    for elem in l:
        for cond in elem:
            if cond > 0:
                p = cond / (n - 1)
                logp = math.log10(p)
                s += p * logp

    return -s # с минусом
    
def pipeline(files: list):
    for i, file in enumerate(files):
        A = pd.read_csv(file).to_numpy()
        print(f"=== Задача №{i} ==========")
        entropy = task(A)
        print(f"Ответ: энтропия равна {entropy:.4f} \n")