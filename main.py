class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if numCourses <= 0 or numCourses > 2000:
            return "wrong numCourses"
        if 0 > len(prerequisites) or len(prerequisites) > numCourses * (numCourses - 1):
            return "wrong prerequisites"
        for i in prerequisites:
            if len(i) != 2:
                return "wrong prerequisites"
        dic = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dic[crs].append(pre)
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in dic[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


#def main():
#    c = Solution()
#    print(c.findOrder(numCourses=1, prerequisites=[]))
#    return 0


#if __name__ == "__main__":
#    main()