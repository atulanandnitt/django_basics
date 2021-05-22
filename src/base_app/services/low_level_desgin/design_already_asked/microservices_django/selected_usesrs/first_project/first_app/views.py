from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import requests
from rest_framework.response import Response

#  call 15th from 14th.

# class Index_2(APIView):
#     def get(self, request):
#         print("calling index 2")
#         uri = "http://127.0.0.1:8000/users/"
#         # requests.get('https://rent.591.com.tw', headers={'User-Agent': 'Custom'})
#         # print(requests.get(uri, headers={'User-Agent': 'Custom'}))
#         response = requests.get(uri, headers={'User-Agent': 'Custom'})
#         response_data = response.text
#         my_dict = {uri: response_data}
#         print("dict is : ")
#         print(my_dict.items())
#
#         # return render(request, 'first_app/index.html', context=my_dict)
#         return HttpResponse(my_dict.items())

# Create your views here. @working
def index(request):
    print("calling index 2")
    uri = "http://127.0.0.1:8000/users/"
    response = requests.get(uri, headers={'User-Agent': 'Custom'})
    response_data = response.text
    my_dict = {uri: response_data}
    print("dict is : , type: {0}".format(type(my_dict)))
    print(my_dict.items())
    print(my_dict.keys())
    print(my_dict.values())
    print(type(my_dict.values()))
    counter = 0
    for val in my_dict.values():
        print(val)
        print(counter)
        counter += 1
    selected_user = my_dict
    # my_dict['Alok']
    # return render(request, 'first_app/index.html', context=my_dict)
    return HttpResponse(selected_user.items())


# def index(request):
#     return HttpResponse("Hello World!")


# def index(request):
#     my_dict = {'insert_me':"Hello I am from views.py!"}
#     return render(request, 'first_app/index.html', context=my_dict)
