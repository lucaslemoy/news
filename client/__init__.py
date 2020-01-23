import requests

class News:
	API_KEY = '367f28d82c3b42e2bb224b79b0ef480e'
	BASIC_URL='https://newsapi.org/v2/top-headlines'
	
	def headlines(self,country):
		list_vide=[]
		payload={'apiKey':self.API_KEY,'country':country}	
		
		request = requests.get(self.BASIC_URL,params=payload)
		print('Cest la icicicicici')
		new_result = request.json()

		for article in new_result['articles'] :
			#print(article)
			list_vide.append(article)
		return list_vide
