import sys
sys.path.append('../')

from AdminUser import *
from AdminTypeExperience import *
from AdminExperience import *
from AdminReview import *
from AdminRecomendation import *
from logica.User import *
from logica.Experience import *
from logica.Review import *
from logica.Rating import *
from logica.Recomendation import *

# Testing AdminRecomendation
# adminRecomendation = AdminRecomendation()
# experience = Experience('Hotel Alfa', 'hotels', 2)
# user = User('James', 'dfjiog5075', [], [], 2)
# rating = Rating(3)
# recomendation = Recomendation(experience, rating)
# print(recomendation)

# adminRecomendation.addRecomendation(recomendation, user)

# Testing AdminReview
# adminReview = AdminReview()
# adminExperience = AdminExperience()
# #experience = Experience('Hotel Alfa', 'hotels', 2)
# experience = Experience('Hotel Beta', 'hotels', 25532)
# adminExperience.addExperience(experience)
# rating = Rating(5)
# review = Review(experience, rating)
# user = User('James', 'dfjiog5075', [], [], 2)
# adminReview.addReview(review, user)
# adminReview.getReviewsFromUser(user)

# Testing Admin User
# adminUser = AdminUser()
# user = User('James', 'dfjiog5075')
# adminUser.addUser(user)
# users = adminUser.getAll()
# for user in users:
# 	user_from_getById = adminUser.getById(user)
# 	print(user_from_getById.getId())

# Testing AdminTypeExperience
# adminTypeExperience = AdminTypeExperience()
# adminTypeExperience.addTypeExperience('restaurants')
# adminTypeExperience.addTypeExperience('hotels')
# print(adminTypeExperience.getAll())
# print(adminTypeExperience.getById(2))
# print(adminTypeExperience.getByName('hotels'))

# Testing AdminExperience
# adminExperience = AdminExperience()
# experience = Experience('Koh i Noor', 'restaurants')
# adminExperience.addExperience(experience)
#experience = Experience('Hotel Alfa', 'hotels')
# adminExperience.addExperience(experience)
# experiences = adminExperience.getAll()
# for exp in experiences:
# 	print(exp.getName())
# experience = adminExperience.getById(1)
# print(experience.getName())