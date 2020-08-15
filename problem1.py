import operator


class Student:

    def __init__(self, name, age, marks, rollNumber):
        self.name = name
        self.age = age
        self.marks = marks
        self.rollNumber = rollNumber

    def __str__(self):
        return "name: {0}, age: {1}, marks:{2}, rollNumber:{3}".format(self.name, self.age, self.marks, self.rollNumber)


def printlist(listOfObjects):
    for obj in listOfObjects:
        print(str(obj))


# Time Complexity : O(nlogn)
def sort(students, criteria):
    keys = criteria.split(',')
    filteredKeys = []
    for key in keys:
        filteredKeys.append(key.strip())
    # todo: add validation for the keys if they actually exists in the Class
    return sorted(students, key=operator.attrgetter(*filteredKeys))


studentList = [Student("shashank", 25, 95, "13cse053"), Student("shashank2", 25, 92, "13cse052"),
               Student("shivam", 27, 89, "13cse045"), Student("vijay", 23, 98, "14cse050")]

printlist(studentList)
studentList = sort(studentList, "age, marks")
print("---After Sorting---")
printlist(studentList)
