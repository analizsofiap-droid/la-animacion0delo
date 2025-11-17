test_science = int(input("enter science test score:"))
test_chemestry = int(input("enter chemestry test score:"))
test_math = int(input("enter math test score:"))
total_test= test_science + test_chemestry + test_math
print("The total of your test is",total_test)
avegare_test= total_test/3
print("And the avegare is ",avegare_test)

homework_Science = int(input("enter science homework score:"))
homework_chemestry = int(input("enter chemestry homework score:"))
homework_math = int(input("enter math homework score:"))
total_homework = homework_Science + homework_chemestry + homework_math
print("the total score for your homework is ", total_homework)
avegare_homework = total_homework/3
print("And the avegare is ",avegare_homework)
participation = int(input("enter your participation score:"))
final_grade = (avegare_test * .5) + (avegare_homework * .3) + 

