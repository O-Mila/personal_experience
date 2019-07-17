import sys
sys.path.append('../')

import mysql.connector
from logica.Experience import *
from AdminTypeExperience import *

class AdminExperience:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addExperience(self, experience):
		typeName = experience.getType()
		adminTypeExperience = AdminTypeExperience()
		id_type = adminTypeExperience.getByName(typeName)[0]
		query = "INSERT INTO experiences(name,id_type) VALUES ('%s',%i)" %(experience.getName(),id_type)
		self.__cursor.execute(query)
		self.__cnx.commit()

	def getAll(self):
		query = "SELECT e.name, t.name, e.id_exp from experiences e " \
			"JOIN types_experiences t ON t.id_type = e.id_type"
		self.__cursor.execute(query)
		experiences_db = self.__cursor.fetchall()
		experiences = []
		for experience in experiences_db:
			experiences.append(Experience(experience[0], experience[1], experience[2]))
		return experiences

	def getById(self, id):
		query = "SELECT e.name, t.name, e.id_exp from experiences e " \
			"JOIN types_experiences t ON t.id_type = e.id_type " \
			"WHERE e.id_exp = %i" %(id)
		self.__cursor.execute(query)
		experience_db = self.__cursor.fetchone()
		if len(experience_db) > 0:
			experience = Experience(experience_db[0], experience_db[1], experience_db[2])
		return experience

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()