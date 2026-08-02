class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #using kahns algorithm
        #we build count of prereqs for all courses
        #also build a map of courses dependencies so we can upadte count
        #initial queue should have all courses with count O
        #the we pop and process that course and reduce number of prereq for its neighbours, then add any neighbour ready
        #we keep count of processed courses and also a list of courses processed
        #when we break out of the loop we return the list of courses processed if we processed all courses, else empty array


        preReqCount = [0] * numCourses
        dependentCourses = defaultdict(list)

        for a,b in prerequisites:
            preReqCount[a] += 1
            dependentCourses[b].append(a)
        
        queue = deque([])
    
        for course in range(numCourses):
            if preReqCount[course] == 0:
                queue.append(course)
        
        processed = 0
        processedCourses = []
        
        while queue:
            course = queue.popleft()
            processed += 1
            processedCourses.append(course)

            for nextCourse in dependentCourses[course]:
                preReqCount[nextCourse] -= 1
                if preReqCount[nextCourse] == 0:
                    queue.append(nextCourse)
        

        return processedCourses if processed == numCourses else []
        