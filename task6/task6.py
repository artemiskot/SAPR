import numpy as np


def makeMatrix(matrix):
    arrMatrix = []
    for k in range(0, len(matrix)):
        tmpRow = []
        for i in range(0, len(matrix[k])):
            for j in range(0, len(matrix[k])):
                if matrix[k][i] < matrix[k][j]:
                    tmpRow.append(1)
                elif matrix[k][i] == matrix[k][j]:
                    tmpRow.append(0.5)
                elif matrix[k][i] > matrix[k][j]:
                    tmpRow.append(0)
        arrMatrix.append(tmpRow)
    return arrMatrix


def makeOneMatrix(matrixs):
    oneMatrix = []
    for i in range(0, len(matrixs[0])):
        sum = 0
        for k in range(0, len(matrixs)):
            sum += matrixs[k][i]
        oneMatrix.append(sum / len(matrixs))
    return oneMatrix


def makeKMatrix(oneMatrix, k=[1 / 3, 1 / 3, 1 / 3]):
    kMatrix = list(split(oneMatrix, len(k)))
    n = len(kMatrix[0])
    kP = np.ones(n) / n
    kN = None
    while True:
        y = np.matmul(kMatrix, kP)
        lbd = np.matmul(np.ones(n), y)
        kN = (1 / lbd) * y
        diff = abs(kN - kP)
        max = diff.max()
        if max <= 0.001:
            break
        else:
            kP = kN
    return np.around(kN, 3)


def parseCSV(csv_file):
    with open(csv_file) as file:
        tmpResult = []
        result = []
        rowArr = []
        csvString = file.read()
        csvString = csvString.split("\n")
        for row in csvString:
            tmpResult.append(eval(row))
        for i in range(0, len(tmpResult[0])):
            for j in range(0, len(tmpResult[0])):
                rowArr.append(tmpResult[j][i])
            result.append(rowArr)
            rowArr = []
    return result


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


def task(csvString):
    res1 = parseCSV(csvString)
    res2 = makeMatrix(res1)
    res3 = makeOneMatrix(res2)
    res4 = makeKMatrix(res3)
    return res4


print(task("./task6_data.csv"))
