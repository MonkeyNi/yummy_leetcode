from collections import defaultdict


class Dijkstra:
    """
    Classic shortest path algorithm.
    TODO: 
        1. save shortest path
        2. multi statisfied pathes
    """

    def shortest_path(self, matrix, start=0):
        """
        Calculate the shortest path from start to each nodes

        Args:
            matrix ([list]): weight matrix
            start (int, optional): [description]. Defaults to 0.

        Returns:
            [type]: [description]
        """
        res = matrix[0]

        visited = [start]
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
matrix = [
 [0,  1,  12, 999, 999, 999],
 [999,   0,   9,   3, 999, 999],
 [999, 999,   0, 999,   5, 999],
 [999, 999,   4,   0,  13,  15],
 [999, 999, 999, 999,   0,   4],
 [999, 999, 999, 999, 999,   0]]
res = test.shortest_path(matrix, start=1)
print(res)
