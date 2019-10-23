
from operator import itemgetter, attrgetter
from collections import OrderedDict
import operator          
import copy
# different testing
# jusge miinimum task
#  find in range
def JudgeMinTask(wbs, string_arr):
    l = len(wbs)
    is_MinTask = True
    subTask = []
    for string in string_arr:
        result = string.find(wbs,0,l)
        if result != -1:
            subTask.append(string)
            is_MinTask = False
    return is_MinTask, subTask

# use enumerate
# use dictionary sorting
l1 = {"1.14":0,"1.14.1":0,"1.14.2":0,"1.14.1.1":0,"1.14.2.1":0}
l1 = OrderedDict(sorted(l1.items(), key=lambda x: (x[0])))
for key, item in l1.items():
    ans = [k for ind,k in enumerate(l1) if k != key]
    judge, subTask = JudgeMinTask(key, ans)
    print("key: ",key)
    print("subTask: ",subTask)
    print("ismintask: ", judge)


# add string zero. E.g. 1.2.4->01.02.04
def AddZero(string):
    new_str = ""
    while (string):
        ind = string.find(".")
        if ind != -1:
            num = int(string[:ind])
            tmp = string[:ind]
            if num <10 and num > 0:
                tmp = "0" + tmp
            new_str += tmp + "."

            string = string[ind+1:]
        else:
            num = int(string)
            if num <10 and num > 0:
                string = "0" + string
            new_str += string
            string = ""
    return new_str

ans = AddZero("1")
ans = AddZero("1.2.1.14")
ans1 = AddZero("0.14.0.1")
l1 = ["1.14","1.2.1.14","1.14.1","1.14.2","1.14.1.1","1.14.2.1"]
for ind in range(len(l1)):
    l1[ind] = AddZero(l1[ind])

# only find substr from index 0 to 6
for string in l:
    result = string.find("1.14.1",0,6)
    if result != -1:
        print(string)


#  use get to avoid key error     
a = {1:23, 2:23, 3:25}
ans = a[1]
ans = a.get(4)
if ans:
    print(ans)
else:
    a[4] = 26