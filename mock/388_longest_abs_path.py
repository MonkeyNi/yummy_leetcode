class Solution:
    def lengthLongestPath(self, input: str):
        i1 = input.split('\n')
        if len(i1) == 1:
            return len(i1[0]) if '.' in i1[0] else 0

        res = 0
        dirs = []
        for f in i1:
            ind = f.count('\t')
            if len(dirs) == ind:
                dirs.append([])
            if ind:
                path = dirs[ind-1][-1]+'/'+f[2*ind-ind:]
            else:
                path = f[2*ind:]
            if '.' in path:
                res = max(res, len(path))
            dirs[ind].append(path)
        return res