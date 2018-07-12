from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMessage


def home(request):
    return render(request,'index.html',{})

class sendMail(APIView):
    def post(self,request):
        mail_sub = request.data.get('subject')
        mail_mat = request.data.get('msg')
        name=request.data.get('name')
        email = EmailMessage('Contact you soon', 'Hii '+name+' thanks for contacting us. We will get in touch with you soon.', to=(request.data.get('email'),))
        email.send()
        email = EmailMessage(mail_sub, mail_mat ,to=['contactus@justcling.com',])
        email.send()
        return Response({"hii":"hello"})