from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})
class SubView(APIView):
    def post(selfself,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})
class MulView(APIView):
    def post(selfself,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1*n2
        return Response({"msg":res})
class DivView(APIView):
    def post(selfself,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1/n2
        return Response({"msg":res})
class FactView(APIView):
    def post(self,request,*args,**kwargs):
        i = 1
        num = request.data.get("num1")
        fact = 1
        while (i <= num):
            fact = fact * i;
            i = i + 1
        return Response({"msg":fact})
class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        words=text.split()
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)