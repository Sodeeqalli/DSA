class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #using Kahn's algorithhm
        #we want to create a queue starting with every course with no prerequisite
        #to do that we need to create a prereq count using array
        #any number thats not in prereq will be added to initial queue
        #then at every stage we take and process number, we also need to keep track of courses that depend on that number so we can reduce its prereqs
        #if the prereqs become zero we continue
        #we keep track of processed courses and if we break out of our bfs and processed courses is not equal to numCourses, we return False, else we return true



        queue = deque([])
        preReqCount = [0] * numCourses
        dependentCourses = defaultdict(list)
        processed = 0

        for a, b in prerequisites:
            preReqCount[a] += 1
            dependentCourses[b].append(a)

        for course in range(len(preReqCount)):
            if preReqCount[course] == 0:
                queue.append(course)

        
        while queue:
            course = queue.popleft()
            processed += 1

            for nextCourse in dependentCourses[course]:
                preReqCount[nextCourse]-=1
                if preReqCount[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return processed == numCourses


               

        