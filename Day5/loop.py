fruits = ["蘋果","草莓","香蕉"]
for fruit in fruits:
    print(fruit)

student_scores = [86,35,56,100,250,86,58]
# total_score = 0
# for score in student_scores:
#     total_score += score
# print(total_score)
max_score = 0
for score in student_scores:
    if(score > max_score):
        max_score = score

print(max_score)