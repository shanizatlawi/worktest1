# input the length of the movie in minutes
movie_lengh_minutes = int(input("enter the length of the movie in minutes: "))

# calculate hours and minutes
hours = movie_lengh_minutes // 60
minutes = movie_lengh_minutes % 60

# print the result
print("the movie is", hours,"hours and", minutes, "minutes long.")
