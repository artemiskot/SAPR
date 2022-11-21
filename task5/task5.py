import numpy as np

import json
from io import StringIO

SEQ_LEN = 10

def createRow(visited: set, cur: int) -> np.array:
    row = []
    for i in range(SEQ_LEN):
        row.append(1 if i+1 in visited else 0)
    return np.array(row)

def createMatrix(data: list) -> np.array:
    visited = set()
    matrix = list()

    for elem in data:
        if type(elem) == str:
            visited.add(int(elem))
            row = createRow(visited=visited, cur=int(elem))
            matrix.append({'num': int(elem), 'row': row})
        else:
            for subelem in elem:
                visited.add(int(subelem))
            for subelem in elem:
                row = createRow(visited=visited, cur=int(subelem))
                matrix.append({'num': int(subelem), 'row': row})

    matrix.sort(key=(lambda x: x['num']))
    raw = [elem['row'] for elem in matrix]

    return np.array(raw)

def searchContradictions(json_path: str) -> list:
    data = json.loads(open(json_path).read())

    matrix1 = createMatrix(data['input1'])
    matrix2 = createMatrix(data['input2'])

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if not criterion[i][j]:
                answer.append([j+1, i+1])
    
    flag = True
    for row in data['output12']:
        flag *= ([int(row[0]), int(row[1])] in answer )
        if not flag:
            print(f"Error on {row}")
    if flag:
        print("Tests successfull!")

    return answer

def task(str1, str2) -> list:

    data = json.loads('{"input1":' + str1 + ', "input2":' + str2 + '}') 

    input1 = []
    input2 = []

    for s in data['input1']:
        if type(s) == str:
            input1.append(s)
        if type(s) == list:
            sub = []
            for subs in s:
                sub.append(subs)
            input1.append(sub)

    for s in data['input2']:
        if type(s) == str:
            input2.append(s)
        if type(s) == list:
            sub = []
            for subs in s:
                sub.append(subs)
            input2.append(sub)

    matrix1 = createMatrix(input1)
    matrix2 = createMatrix(input2)

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if not criterion[i][j]:
                answer.append([str(j+1), str(i+1)])

    return answer