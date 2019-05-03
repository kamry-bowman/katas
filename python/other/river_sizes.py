map = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [
    0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0], ]

# expected output [1, 2, 2, 2, 5]


def river_sizes(map):
    visitedPositions = set()
    rivers = []

    def walkMap():
        for rowIndex in range(len(map)):
            for colIndex in range(len(map[rowIndex])):
                position = (rowIndex, colIndex)
                if isRiver(position) and isNew(position):
                    walkRiver(position)

    def isRiver(position):
        rowIndex, colIndex = position
        return map[rowIndex][colIndex] == 1

    def isNew(position):
        return position not in visitedPositions

    def isOnMap(position):
        rowIndex, colIndex = position
        rowIsValid = rowIndex >= 0 and rowIndex < len(map)
        colIsValid = rowIsValid and colIndex >= 0 and colIndex < len(
            map[rowIndex])
        return rowIsValid and colIsValid

    def walkRiver(position):
        stack = []
        totalLength = 0

        def addEdgesToStack(pos, length):
            (rowIndex, colIndex) = pos
            for move in (-1, 1):
                stack.append(
                    {'position': (rowIndex + move, colIndex), 'length': length + 1})
                stack.append(
                    {'position': (rowIndex, colIndex + move), 'length': length + 1})

        def isValidStep(pos):
            return isOnMap(pos) and isRiver(pos) and isNew(pos)

        stack.append({'position': position, 'length': 1})

        while stack:
            current = stack.pop()

            if isValidStep(current['position']):
                totalLength = max(totalLength, current['length'])
                visitedPositions.add(current['position'])
                addEdgesToStack(current['position'], current['length'])

        rivers.append(totalLength)

    walkMap()
    return rivers


print(river_sizes(map))

