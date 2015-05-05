from rest_easy.core.source import SourceBuilder

__author__ = 'David McInnis'



from rest_easy.core.main import RestEasy

RestEasy = RestEasy()
dpla = RestEasy.get_wrappers("dpla")
dpla("v2").apiKey()

