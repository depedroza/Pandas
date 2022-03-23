import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

print(grades)

eva = grades["Eva"]

sam = grades.Sam

# using the loc and iloc methods

test2 = grades.loc["Test2"]
# loc may be a bit better since it does not relay on a 0-based index, it calls a direct custom index name
# that we can assign. This prevents confusion with indexes starting at 0.
test1 = grades.iloc[1]

# For consecutive rows
test1_thru_test3 = grades.loc["Test1":"Test3"]
# For non-consecutive rows
test1_and_test3 = grades.loc[["Test1", "Test2"]]

test1_and_test2_wrong = grades.iloc[0:1]
# this alone does NOT include the upper index, 1. We would need 0:2

test1_and_test2 = grades.iloc[0:2]

# view only Eva's and Katie's Grades for Test1 and Test2

eva_and_katie_test1_test2 = grades[["Eva", "Katie"]].loc["Test1":"Test2"]
# OR grades.loc[:'Test2',['Eva','Katie']]

# view only Sam's thru Bob's grades for Test 1 and Test3

sam_thru_bob_test1_test3 = grades.loc[["Test1", "Test3"], "Sam":]


# Boolean Indexing
# Select everyone wit han A grade

grades_A = grades[grades >= 90]

# create a dataframe for everyone with a B grade
grades_B = grades[(grades >= 80) & (grades < 90)]

# create a dataframe for everyone with an A or B grade
grades_A_or_B = grades[(grades >= 80) | (grades >= 80)]


# by student
pd.set_option("precision", 2)
print(grades.describe())

# by test
print(grades.T.describe())

# Exercise - Get the average of all the students grades on each test
print(grades.T.mean())

# sort rows by their indices (Test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

# sorted columns by their column names (student names)
# axis = 1 indicates to sort colun by indices
# axis = 0 indicates to sort by row indices

c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)

print()
