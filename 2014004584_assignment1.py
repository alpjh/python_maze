import queue
import heapq


class Tree(object):
    def __init__(self):
        self.left = None
        self.down = None
        self.right = None
        self.up = None
        self.parent = None
        self.data = None


fifoQueue = queue.Queue()
heapQueue = []
stack = queue.LifoQueue()

visited = []


def main():
    first_floor()
    second_floor()
    third_floor()
    fourth_floor()
    fifth_floor()


def first_floor():
    maze = inputMaze("first_floor.txt")
    # maze, start, end, path, time
    value = dfs(maze, findEntrance(maze)[0], 6, Tree(), 0)

    f = open("first_floor_output.txt", 'w')
    for i in maze:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")
    f.write("--\nlength="+str(value[0])+"\ntime="+str(value[1]))
    f.close()


def second_floor():

    maze = inputMaze("second_floor.txt")
    # maze, start, end, path, time
    value = dfs(maze, findEntrance(maze)[0], 6, Tree(), 0)

    f = open("second_floor_output.txt", 'w')
    for i in maze:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")
    f.write("--\nlength="+str(value[0])+"\ntime="+str(value[1]))
    f.close()

def third_floor():

    maze = inputMaze("third_floor.txt")
    # maze, start, end, path, time
    value = dfs(maze, findEntrance(maze)[0], 6, Tree(), 0)

    f = open("third_floor_output.txt", 'w')
    for i in maze:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")
    f.write("--\nlength="+str(value[0])+"\ntime="+str(value[1]))
    f.close()

def fourth_floor():

    maze = inputMaze("fourth_floor.txt")
    # maze, start, end, path, time
    value = aStar(maze, findEntrance(maze)[0], 6, Tree(), 0)

    f = open("fourth_floor_output.txt", 'w')
    for i in maze:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")
    f.write("--\nlength="+str(value[0])+"\ntime="+str(value[1]))
    f.close()

def fifth_floor():

    maze = inputMaze("fifth_floor.txt")
    # maze, start, end, path, time
    value = aStar(maze, findEntrance(maze)[0], 6, Tree(), 0)

    f = open("fifth_floor_output.txt", 'w')
    for i in maze:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")
    f.write("--\nlength="+str(value[0])+"\ntime="+str(value[1]))
    f.close()


def bfs(maze, start, endValue, root, time):

    visited.clear()
    while not fifoQueue.empty():
        fifoQueue.get()
    m = start[0]
    n = start[1]
    time = time
    curNode = root
    curNode.data = [m, n]

    while 1:
        visited.append([curNode.data[0], curNode.data[1]])
        # goal check
        if maze[curNode.data[0]][curNode.data[1]] == endValue:
            length = 0
            tmpNode = curNode
            while curNode.parent is not None:
                length += 1
                if endValue == 4:
                    if maze[curNode.data[0]][curNode.data[1]] != 4:
                        maze[curNode.data[0]][curNode.data[1]] = 5
                curNode = curNode.parent
            curNode = tmpNode
            break

        # 왼쪽 인큐
        if n - 1 >= 0 and [m, n-1] not in visited:
            if maze[m][n - 1] == 2 or maze[m][n - 1] == endValue:
                curNode.left = Tree()
                curNode.left.data = [m, n - 1]
                curNode.left.parent = curNode
                fifoQueue.put(curNode.left)
        # 아래쪽 인큐
        if m + 1 < len(maze) and [m + 1, n] not in visited:
            if maze[m + 1][n] == 2 or maze[m + 1][n] == endValue:
                curNode.down = Tree()
                curNode.down.data = [m + 1, n]
                curNode.down.parent = curNode
                fifoQueue.put(curNode.down)
        # 위쪽 인큐
        if m - 1 >= 0 and [m - 1, n] not in visited:
            if maze[m - 1][n] == 2 or maze[m - 1][n] == endValue:
                curNode.up = Tree()
                curNode.up.data = [m - 1, n]
                curNode.up.parent = curNode
                fifoQueue.put(curNode.up)
        # 오른쪽 인큐
        if n + 1 < len(maze[0]) and [m, n + 1] not in visited:
            if maze[m][n + 1] == 2 or maze[m][n + 1] == endValue:
                curNode.right = Tree()
                curNode.right.data = [m, n + 1]
                curNode.right.parent = curNode
                fifoQueue.put(curNode.right)

        time += 1
        curNode = fifoQueue.get()
        m = curNode.data[0]
        n = curNode.data[1]

    if endValue != 4:
        return bfs(maze, [m, n], 4, curNode, time)

    print("length: " + str(length))
    print("time: " + str(time))

    return [length, time]


def dfs(maze, start, endValue, root, time):

    visited.clear()
    while not stack.empty():
        stack.get()
    m = start[0]
    n = start[1]
    time = time
    curNode = root
    curNode.data = [m, n]

    while 1:
        visited.append([curNode.data[0], curNode.data[1]])
        # goal check
        if maze[curNode.data[0]][curNode.data[1]] == endValue:
            length = 0
            tmpNode = curNode
            while curNode.parent is not None:
                length += 1
                if endValue == 4:
                    if maze[curNode.data[0]][curNode.data[1]] != 4:
                        maze[curNode.data[0]][curNode.data[1]] = 5
                curNode = curNode.parent
            curNode = tmpNode
            break

        # 왼쪽 인큐
        if n - 1 >= 0 and [m, n-1] not in visited:
            if maze[m][n - 1] == 2 or maze[m][n - 1] == endValue:
                curNode.left = Tree()
                curNode.left.data = [m, n - 1]
                curNode.left.parent = curNode
                stack.put(curNode.left)
        # 아래쪽 인큐
        if m + 1 < len(maze) and [m + 1, n] not in visited:
            if maze[m + 1][n] == 2 or maze[m + 1][n] == endValue:
                curNode.down = Tree()
                curNode.down.data = [m + 1, n]
                curNode.down.parent = curNode
                stack.put(curNode.down)
        # 위쪽 인큐
        if m - 1 >= 0 and [m - 1, n] not in visited:
            if maze[m - 1][n] == 2 or maze[m - 1][n] == endValue:
                curNode.up = Tree()
                curNode.up.data = [m - 1, n]
                curNode.up.parent = curNode
                stack.put(curNode.up)
        # 오른쪽 인큐
        if n + 1 < len(maze[0]) and [m, n + 1] not in visited:
            if maze[m][n + 1] == 2 or maze[m][n + 1] == endValue:
                curNode.right = Tree()
                curNode.right.data = [m, n + 1]
                curNode.right.parent = curNode
                stack.put(curNode.right)

        time += 1
        curNode = stack.get()
        m = curNode.data[0]
        n = curNode.data[1]

    if endValue != 4:
        return dfs(maze, [m, n], 4, curNode, time)

    print("length: " + str(length))
    print("time: " + str(time))

    return [length, time]


def greed(maze, start, endValue, root, time):

    destination = findDestination(maze)
    visited.clear()
    while not len(heapQueue) == 0:
        heapq.heappop(heapQueue)
    m = start[0]
    n = start[1]
    time = time
    curNode = root
    curNode.data = [m, n]
    dummy = 0

    while 1:
        visited.append([curNode.data[0], curNode.data[1]])
        # goal check
        if maze[curNode.data[0]][curNode.data[1]] == endValue:
            length = 0
            tmpNode = curNode
            while curNode.parent is not None:
                length += 1
                if endValue == 4:
                    if maze[curNode.data[0]][curNode.data[1]] != 4:
                        maze[curNode.data[0]][curNode.data[1]] = 5
                curNode = curNode.parent
            curNode = tmpNode
            break

        # 왼쪽 인큐
        if n - 1 >= 0 and [m, n-1] not in visited:
            if maze[m][n - 1] == 2 or maze[m][n - 1] == endValue:
                curNode.left = Tree()
                curNode.left.data = [m, n - 1]
                curNode.left.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m, n-1], destination), dummy, curNode.left))
                dummy += 1

        # 아래쪽 인큐
        if m + 1 < len(maze) and [m + 1, n] not in visited:
            if maze[m + 1][n] == 2 or maze[m + 1][n] == endValue:
                curNode.down = Tree()
                curNode.down.data = [m + 1, n]
                curNode.down.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m + 1, n], destination), dummy, curNode.down))
                dummy += 1

        # 위쪽 인큐
        if m - 1 >= 0 and [m - 1, n] not in visited:
            if maze[m - 1][n] == 2 or maze[m - 1][n] == endValue:
                curNode.up = Tree()
                curNode.up.data = [m - 1, n]
                curNode.up.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m - 1, n], destination), dummy, curNode.up))
                dummy += 1

        # 오른쪽 인큐
        if n + 1 < len(maze[0]) and [m, n + 1] not in visited:
            if maze[m][n + 1] == 2 or maze[m][n + 1] == endValue:
                curNode.right = Tree()
                curNode.right.data = [m, n + 1]
                curNode.right.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m, n + 1], destination), dummy, curNode.right))
                dummy += 1

        time += 1
        curNode = heapq.heappop(heapQueue)
        curNode = curNode[2]
        m = curNode.data[0]
        n = curNode.data[1]

    if endValue != 4:
        return greed(maze, [m, n], 4, curNode, time)

    print("length: " + str(length))
    print("time: " + str(time))

    return [length, time]


def aStar(maze, start, endValue, root, time):

    destination = findDestination(maze)
    visited.clear()
    while not len(heapQueue) == 0:
        heapq.heappop(heapQueue)
    m = start[0]
    n = start[1]
    time = time
    curNode = root
    curNode.data = [m, n]
    dummy = 0

    while 1:
        visited.append([curNode.data[0], curNode.data[1]])
        # goal check
        if maze[curNode.data[0]][curNode.data[1]] == endValue:
            length = 0
            tmpNode = curNode
            while curNode.parent is not None:
                length += 1
                if endValue == 4:
                    if maze[curNode.data[0]][curNode.data[1]] != 4:
                        maze[curNode.data[0]][curNode.data[1]] = 5
                curNode = curNode.parent
            curNode = tmpNode
            break

        # 왼쪽 인큐
        if n - 1 >= 0 and [m, n-1] not in visited:
            if maze[m][n - 1] == 2 or maze[m][n - 1] == endValue:
                curNode.left = Tree()
                curNode.left.data = [m, n - 1]
                curNode.left.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m, n-1], destination) + getDistince(start, [m, n-1]), dummy, curNode.left))
                dummy += 1

        # 아래쪽 인큐
        if m + 1 < len(maze) and [m + 1, n] not in visited:
            if maze[m + 1][n] == 2 or maze[m + 1][n] == endValue:
                curNode.down = Tree()
                curNode.down.data = [m + 1, n]
                curNode.down.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m + 1, n], destination) + getDistince(start, [m + 1, n]), dummy, curNode.down))
                dummy += 1

        # 위쪽 인큐
        if m - 1 >= 0 and [m - 1, n] not in visited:
            if maze[m - 1][n] == 2 or maze[m - 1][n] == endValue:
                curNode.up = Tree()
                curNode.up.data = [m - 1, n]
                curNode.up.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m - 1, n], destination) + getDistince(start, [m - 1, n]), dummy, curNode.up))
                dummy += 1

        # 오른쪽 인큐
        if n + 1 < len(maze[0]) and [m, n + 1] not in visited:
            if maze[m][n + 1] == 2 or maze[m][n + 1] == endValue:
                curNode.right = Tree()
                curNode.right.data = [m, n + 1]
                curNode.right.parent = curNode
                heapq.heappush(heapQueue, (getDistince([m, n + 1], destination) + getDistince(start, [m, n+1]), dummy, curNode.right))
                dummy += 1

        time += 1
        curNode = heapq.heappop(heapQueue)
        curNode = curNode[2]
        m = curNode.data[0]
        n = curNode.data[1]

    if endValue != 4:
        return aStar(maze, [m, n], 4, curNode, time)

    print("length: " + str(length))
    print("time: " + str(time))

    return [length, time]


def getDistince(start, destination):
    a = start[0] - destination[0]
    b = start[1] - destination[1]
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return a + b


def findDestination(maze):
    i = 0
    while maze[len(maze)-1]:
        if maze[len(maze)-1][i] == 4:
            return [len(maze)-1, i]
        else:
            i += 1


def inputMaze(path):
    text = open(path, 'r')
    info = text.readline().split()
    info = [int(i) for i in info]

    maze = [[0] * info[2] for _ in range(info[1])]

    for i in range(info[1]):
        temp = text.readline().split()
        for j in range(info[2]):
            maze[i][j] = int(temp[j])
    text.close()
    return maze


def findEntrance(maze):
    startList = []
    # Find Entrance
    i = 0
    while maze[0]:
        if maze[0][i] == 3:
            startList.append([0, i])
            break
        else:
            i += 1
    return startList


main()
