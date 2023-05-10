# from django.shortcuts import render
from django.http import HttpResponse
# def hello(requests):
# #     my_list = [1, 2, 3, 4]
# #     return HttpResponse(my_list)
#     body= """
#     <!DOCTYPE html> 
# <html lang="ru"> 
# <head> 
#   <meta charset="UTF-8"> 
#   <title>Базовая разметка HTML</title> 
# </head> 
# <body> 
#   <h1>Code Basics</h1> 
#   <p>Бесплатные уроки по программированию и HTML для новичков</p> 
# </body> 
# </html>
# """
#     return HttpResponse(body)

# def test_page(request):
#     print(request)
#     return HttpResponse("Test")


def get_contacts(request):
  return HttpResponse("Number", headers={"Name": "Alex"}, status=200)


def get_about(request):
  return HttpResponse("About", headers={"Name": "Alex"}, status=200)

def get_hello(request):
  return HttpResponse("Hello", headers={"Name": "Alex"}, status=500)


