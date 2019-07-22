import pandas as pd
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User
from logica.Experience import Experience
from logica.Recomendation import Recomendation

class MachineLearning:
    def __init__(self, correlations = None):
    	if correlations is not None:
        	self.__setCorrelations(correlations)

    # def train(self, users):
    #     reviews = {"rating": [], "experience": []}
    #     for user in users:
    #         for review in user.getReviews():
    #             reviews["experience"].append(review.getExperience().getId())
    #             reviews["rating"].append(review.getRating().getValue())
    #     corrMatrix = pd.DataFrame(data=reviews).pivot(columns='experience',values='rating').corr(method='pearson', min_periods=1)
    #     self.__setCorrelations(corrMatrix)

    def train(self, users):
        reviews = {"rating": [], "experience": [], "user": []}
        for user in users:
            for review in user.getReviews():
                reviews["user"].append(user.getId())
                reviews["experience"].append(review.getExperience().getId())
                reviews["rating"].append(review.getRating().getValue())
        df = pd.DataFrame.from_dict(reviews)
        userRatings = df.pivot_table(index=['user'],columns=['experience'],values='rating')
        corrMatrix = userRatings.corr(method='pearson', min_periods=1)
        self.__setCorrelations(corrMatrix)

    def recomendate(self, user):
    	recomendations = {}
    	for experience in self.correlations:
    		recomendations[experience] = 0
    	# Recorremos las reviews del usuario.
    	for review in user.getReviews():
    		#regresión lineal y = mx + b. 1. Consigo el rating. 2. Set del rating.
    		for experience,correlation in self.correlations[review.getExperience().getId()].dropna().items():
    			recomendations[experience] += correlation*review.getRating().getValue()
    	for experience, rating in recomendations.items():
            #WIP:Esto hay que arreglarlo
    		user.addRecomendation(Recomendation(Experience("esto hay", "que arreglarlo", experience), rating))

    def __setCorrelations(self, correlations):
    	self.correlations = correlations

    def getCorrelations(self):
    	return self.correlations