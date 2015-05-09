from rest_easy.core.source import SourceBuilder

__author__ = 'David McInnis'



from rest_easy.core.main import RestEasy

RestEasy = RestEasy()
dpla = RestEasy.get_wrappers("dpla")
dpla("v2").apiKey("de61f325217108a6de996ea4fcf64092")
dpla('v2').Items.searchIn.title('calligraphy')
dpla('v2').Items.searchIn.language.name('chinese')
results = dpla('v2').Items.GET()


print (results[0])
