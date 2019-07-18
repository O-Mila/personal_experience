import sys
sys.path.append('../')

import mysql.connector
from logica.Review import *
from logica.Rating import *

class AdminReview:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addReview(self, review, user):
		query = "INSERT INTO reviews(id_exp, id_user, rating) VALUES (%i, %i, %f)" \
		%(review.getExperience().getId(), user.getId(), review.getRating().getValue())
		self.__cursor.execute(query)
		self.__cnx.commit()

	def getAll(self):
		query = "SELECT * from reviews"
		self.__cursor.execute(query)
		reviews_db = self.__cursor.fetchall()
		reviews = []
		for review in reviews_db:
			experience = AdminExperience.getById(review[0])
			reviews.append(Review(experience, review[2]))
		return reviews

	def getReviewsFromUser(self, user):
		query = "SELECT r.rating, e.name, e.id_exp, t.name, t.id_type from reviews r " \
				"JOIN users u ON u.id_user = r.id_user " \
				"JOIN experiences e ON e.id_exp = r.id_exp " \
				"JOIN types_experiences t ON e.id_type = t.id_type " \
				"WHERE u.id_user = %i" %(user.getId())
		self.__cursor.execute(query)
		reviews_db = self.__cursor.fetchall()
		print(reviews_db)
		reviews = []
		for review_db in reviews_db:
			experience = Experience(review_db[1], review_db[3], review_db[2])
			rating = Rating(review_db[0])
			review = Review(experience, rating)
			reviews.append(review)
		return reviews

	# def getById(self, id_review):
	# 	query = "SELECT * from reviews WHERE id_user =%i and id_exp = %i" %(id_review[0], id_review[1])
	# 	self.__cursor.execute(query)
	# 	review_db = self.__cursor.fetchone()
	# 	review = ''
	# 	if len(review_db) > 0:
	# 		review = Review(review_db[1], review_db[2])
	# 	return user

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()