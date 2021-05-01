
# import suitable packages
from django.shortcuts import render
import pyshorteners
from django.views import View


# Function Based Views to perform url shortner

'''
def url_shortner(request):
	short_url=""
	long_url = ""
	if request.method == "POST" and 'short-url' in request.POST:
		long_url = 'url' in request.POST and request.POST['url']
		pys = pyshorteners.Shortener()
		short_url = pys.tinyurl.short(long_url)


	return render(request,'urlShortner.html', context={'short_url':short_url,'long_url':long_url}) '''



# Class Based Views to perform url shortner

class url_shortner(View):

	def post(self,request):
		long_url = 'url' in request.POST and request.POST['url']
		pys = pyshorteners.Shortener()
		short_url = pys.tinyurl.short(long_url)
		return render(request,'urlShortner.html', context={'short_url':short_url,'long_url':long_url})

	def get(self,request):
		return render(request,'urlShortner.html')
		