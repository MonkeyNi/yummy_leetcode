class Dijkstra:
    """
    Classic shortest path algorithm.
    TODO: multi statisfied pathes
    """

    def shortest_path(self, matrix):
        res = matrix[0]
        visited = [0]
        visiting = [i for i in range(len(matrix[0])) if not i in visited]

        while visiting:
            ind = visiting[0]
            for i in visiting:
                if res[i] < res[ind]:
                    ind = i
            visited.append(ind)
            visiting.remove(ind)

            for j in visiting:
                if res[j] > res[ind] + matrix[ind][j]:
                    res[j] = res[ind] + matrix[ind][j]
        return res


test = Dijkstra()
matrix = [[  0,  1,  12, 999, 999, 999],
 [999,   0,   9,   3, 999, 999],
 [999, 999,   0, 999,   5, 999],
 [999, 999,   4,   0,  13,  15],
 [999, 999, 999, 999,   0,   4],
 [999, 999, 999, 999, 999,   0]]
res = test.shortest_path(matrix)
print(res)
