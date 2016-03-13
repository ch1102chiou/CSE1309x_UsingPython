# Type your code here
def create_grades_dict(file_name):

    # define a function to update 
    def updateScoreDict(scdict, stuid, studict, testitem):
        if testitem in studict.keys():
           scdict[stuid].append(studict[testitem])
        else:
            scdict[stuid].append(0)
        return

    # define a function to compute student avg.
    
    def computeAvg(scdict):
        for student in scdict.keys():
            total = 0
            for i in range(1,len(scdict[student])):
                total = total + scdict[student][i]
            avg = total / len(scdict[student][1:])
            scdict[student].append(avg)
        return
    
    # read a file
    scorefile = open(file_name, 'r')

    # create dictionary scoreDict
    scoreDict = {}

    line = scorefile.readline()
    while len(line) != 0:
        # remove space and get the list L by splitting the string by ','

        line = line.replace(" ", "")
        line = line.strip("\n")
        L = line.split(",")
        # studentId = L[0]
        # studentName = L[1]
        studentId = int(L[0])
        studentName = L[1]

        # create student studentScoreDict
        studentScoreDict = {}

        # trace the List from L[2] to L[N]
        # studentScoreDict[L[2+2i]] = L[3+2i] from i = 0 to k = ( N-4 ) /2 + 1
        for i in range (int((len(L) - 3)/2) + 1):
            studentScoreDict[L[2+2*i]] = int(L[3+2*i])

        # update scoreDict
        scoreDict[studentId] = [studentName]
        updateScoreDict(scoreDict, studentId, studentScoreDict, "Test_1")
        updateScoreDict(scoreDict, studentId, studentScoreDict, "Test_2")
        updateScoreDict(scoreDict, studentId, studentScoreDict, "Test_3")
        updateScoreDict(scoreDict, studentId, studentScoreDict, "Test_4")

        line = scorefile.readline()

    computeAvg(scoreDict)

    return scoreDict

# Your main program starts below this line
def print_grades(file_name):
    title = "{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format("ID","Name","Test_1","Test_2","Test_3","Test_4","Avg.")
    print (title)
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    studentIdList = list(grades_dict.keys())
    studentIdList.sort()
    for studentId in studentIdList:
        grades_list = grades_dict[studentId]
        s = "{0:<10d} | {1:<16s} | {2:>6d} | {3:>6d} | {4:>6d} | {5:>6d} | {6:>6.2f} |".format(int(studentId),grades_list[0],grades_list[1],grades_list[2],grades_list[3],grades_list[4], grades_list[5])
        print (s)




print_grades("as3.test")