import re

def task(csvString):
    gNodes = re.findall(r'\d+', csvString)
    for i in range(len(gNodes)):
        gNodes[i] = int(gNodes[i])
    graph = {i: [] for i in range(1, max(gNodes) + 1)}

    csvString = csvString.split('\n')
    if csvString[-1] == '':
        del csvString[-1]

    for i in csvString:
        nodes = i.split(',')
        graph[int(nodes[0])].append(nodes[1])

    r1, r2, r3, r4, r5 = [], [], [], [], []

    for key in graph:
        if len(graph[key]) > 0:
            r1.append(key)
        for leaveNode in graph[key]:
            if int(leaveNode) not in r2:
                r2.append(int(leaveNode))

    for i in r1:
        if len(graph[i]) > 1:
            for leaveNode in graph[i]:
                if int(leaveNode) not in r5:
                    r5.append(int(leaveNode))
        for leaveNode_1 in graph[i]:
            for leaveNode_2 in graph[int(leaveNode_1)]:
                if i not in r3:
                    r3.append(i)
                if int(leaveNode_2) not in r4:
                    r4.append(int(leaveNode_2))

    return [r1, r2, r3, r4, r5]


def main():
    with open('data.csv') as file:
        csvString = file.read()
        result = task(csvString)
        print(result)


if __name__ == '__main__':
    main()