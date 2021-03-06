import sys
sys.path.append('../')

import mysql.connector
from logica.Experience import *
from db.AdminTypeExperience import *

class AdminExperience:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		
	def __getCursor(self):
		return self.__cnx.cursor()		

	def addExperience(self, experience):
		if experience == None or type (experience) != Experience:
			raise ExperienceNoValidException()		
		adminTypeExperience = AdminTypeExperience()
		retrievedExperience = self.getByName(experience.getName())
		if type(retrievedExperience) != Experience or retrievedExperience is None:
			typeName = experience.getType()
			type_db = adminTypeExperience.getByName(typeName)
			if len(type_db) == 0:
				adminTypeExperience.addTypeExperience(typeName)
				type_db = adminTypeExperience.getByName(typeName)
			id_type = type_db[0]
			cursor = self.__getCursor()
			query = "INSERT INTO experiences(name,id_type) VALUES ('%s',%i)" \
			%(experience.getName().replace("'", "''"), id_type)
			cursor.execute(query)

			self.__cnx.commit()
			cursor.close()
		else:
			return 'This experience already exists!'

	def getByName(self, name):
		cursor = self.__getCursor()
		query = "SELECT e.name, t.name, e.id_exp FROM experiences e " \
				"JOIN types_experiences t ON t.id_type = e.id_type WHERE e.name = '%s'" \
				%(str(name).replace("'", "''"))
		cursor.execute(query)

		experience_db = cursor.fetchone()
		if experience_db is None:
			experience = None
		else:
			experience = Experience(experience_db[0], experience_db[1], experience_db[2])			
		
		cursor.close()
		return experience

	def closeConnection(self):
		self.__cnx.close()

	def deleteAll(self):
		cursor = self.__getCursor()
		query = "DELETE FROM experiences"
		cursor.execute(query)
		self.__cnx.commit()
		cursor.close()

	def getAll(self):
		cursor = self.__getCursor()
		query = "SELECT e.name, t.name, e.id_exp from experiences e " \
			"JOIN types_experiences t ON t.id_type = e.id_type"
		cursor.execute(query)
		experiences_db = cursor.fetchall()
		experiences = []
		for experience in experiences_db:
			experiences.append(Experience(experience[0], experience[1], experience[2]))

		cursor.close()
		return experiences

	def getById(self, id):
		cursor = self.__getCursor()
		query = "SELECT e.name, t.name, e.id_exp from experiences e " \
			"JOIN types_experiences t ON t.id_type = e.id_type " \
			"WHERE e.id_exp = %i" %(id)
		cursor.execute(query)
		experience_db = cursor.fetchone()
		if len(experience_db) == 3:
			experience = Experience(experience_db[0], experience_db[1], experience_db[2])
		else:
			experience = None
		
		cursor.close()
		return experience