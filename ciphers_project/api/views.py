from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import caesar_encode

# Create your views here.
def greeting(request):
    result = {"message": "Welcome to the Ciphers API!"}
    return JsonResponse(result)

def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caesar_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})
