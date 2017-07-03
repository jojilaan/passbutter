class Boter(object):
                #Constructor
		def __init__(self):
				self.gewicht = 500                          #initialiseer gewicht

                #Accessor
		def getGewicht(self):
				return self.gewicht                         #vraag gewicht op
		
                #Public Method
		def updateGewicht(self):
				self.gewicht = self.gewicht - 7.5           #er wordt boter gebruikt, update gewicht boter

		def resetGewicht(self):
				self.gewicht = 500                          #als de boter op en er wordt nieuwe boter in de boter vloot gedaan
