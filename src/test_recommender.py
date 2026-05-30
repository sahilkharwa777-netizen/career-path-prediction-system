from course_recommender import recommend_courses

career = "Systems Security Administrator"

courses = recommend_courses(career)

print("\nRecommended Courses:\n")

for course in courses:
    print("-", course)