from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from userprojectappone.serializers import UserSerializer, SuperUserSerializer
# from userprojectappone.models import Registration
# from django.contrib.auth.hashers import make_password, check_password
# from emailsend import OTGGenerator


# Create your views here.

@api_view(["POST"])
def RegisterUser(request):
    try:
        myuser = request.data
        username = myuser["username"]
        email = myuser["email"]
        password = myuser["password"]
        confirm_password = myuser["confirm_password"]
        # encryptedpassword=make_password(password)
        # checkpassword=check_password(password, encryptedpassword)
        first_name = myuser["first_name"]
        last_name = myuser["last_name"]

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return Response({"message": "Username taken"})
            
            elif User.objects.filter(email=email).exists():
                return Response({"message": "Email taken"})
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()

                serialized_registered_user = UserSerializer(user, many=False)
                return Response({"data": serialized_registered_user.data, "message": "Successful registration"}) 
        else:
            return Response({"message": "Unmatching password"})

    except Exception as ex:
        print(ex)
        return Response({"message": ex})
    


@api_view(["POST"])
def LoginUser(request):
    try:
        mylogin = request.data
        username = mylogin["username"]
        password = mylogin["password"]

        userlogin = auth.authenticate(request, username=username, password=password)
        if userlogin is not None:
            serialized_login_user = UserSerializer(userlogin, many=False)
            return Response({"data": serialized_login_user.data, "message": "Successful login"})
        else:
            return Response({"message": "Incorrect details"})
        
    except Exception as ex:
        print(ex)
        return Response({"message": ex})



@api_view(["POST"])
def RegisterSuperUser(request):
    try:
        mysuperuser = request.data
        username = mysuperuser["username"]
        email = mysuperuser["email"]
        password = mysuperuser["password"]
        confirm_password = mysuperuser["confirm_password"]
        first_name = mysuperuser["first_name"]
        last_name = mysuperuser["last_name"]

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return Response({"message": "Username taken"})
            
            elif User.objects.filter(email=email).exists():
                return Response({"message": "Email taken"})
            
            else:
                superuser = User.objects.create_superuser(username=username, email=email, password=password, first_name=first_name, last_name=last_name, is_superuser=True)
                superuser.save()

                serialized_registered_superuser = SuperUserSerializer(superuser, many=False)
                return Response({"data":serialized_registered_superuser.data, "message": "Successful registration"}) 
        else:

            return Response({"message": "Unmatching password"})

    except Exception as ex:
        print(ex)
        return Response({"message": ex})


  
@api_view(["POST"])
def LoginSuperUser(request):
    try:
        mylogin = request.data
        username = mylogin["username"]
        password = mylogin["password"]

        userlogin = auth.authenticate(request, username=username, password=password)
        if userlogin is not None:
            serialized_login_superuser = SuperUserSerializer(userlogin, many=False)
            return Response({"data": serialized_login_superuser.data, "message": "Authentication successful"})
        else:
            return Response({"message": "Incorrect details"})
        
    except Exception as ex:
        print(ex)
        return Response({"message": ex})    



# @api_view(["GET"])
# def GetUser(request, username):
#     try:
#         getuser = User.objects.filter(username=username)

#         serialized_get_user = UserSerializer(getuser, many=False)
#         return Response(serialized_get_user.data)
    
#     except Exception as ex:
#         print(ex)
#         return Response({"message": ex})



@api_view(["GET"])
def GetAllUsers(request):
    try:
        getallusers = User.objects.all()

        serialized_getall_user = UserSerializer(getallusers, many=True)
        return Response(serialized_getall_user.data)
    
    except Exception as ex:
        print(ex)
        return Response({"message": ex})
    


@api_view(["GET"])
def GetById(request, id):
    try:
        getiduser = User.objects.get(pk = id)

        serialized_getid_user =  UserSerializer(getiduser, many=False)
        return Response(serialized_getid_user.data)

    except Exception as ex:
        print(ex)
        return Response({"message": ex})



@api_view(["PUT"])
def UpdateUser(request, id):
    try:
        myupdateuser = request.data
        email = myupdateuser["email"]
        first_name = myupdateuser["first_name"]
        last_name = myupdateuser["last_name"]

        # if User.objects.filter(email=email).exists():
        #     return Response({"message": "Email taken"})
        # else:

        updateuser = User.objects.filter(id = id).first()
        updateuser.email=email
        updateuser.first_name=first_name
        updateuser.last_name=last_name

        updateuser.save()
        serialized_update_user = UserSerializer(updateuser, many=False)
        return Response({"data": serialized_update_user.data, "message": "Update successful"})
        
    except Exception as ex:
        print(ex)
        return Response({"message": ex})



@api_view(["DELETE"])
def DeleteUser(request, id):
    try:
        deleteuser = User.objects.get(pk = id).delete()
        
        return Response({"message": "User data deleted"})
    except Exception as ex:
        print(ex)
        return Response({"message": ex})



# @api_view(["POST"])
# def LogoutUser(request):
#     try:
#         request
#         return Response({"message": "Successfully logout"})
    
#     except Exception as ex:
#         print(ex)
#         return Response({"message": ex})
    


   








































































# from django.db import models
# from django.contrib.auth.models import AbstractUser
# import uuid

# # Create your models here.


# class Staff(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=250)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     dateregistered = models.DateTimeField(auto_now_add=True) 
#     last_login= models.DateTimeField(auto_now=True, verbose_name='last login')

#     USERNAME_FIELD = 'username'

#     REQUIRED_FIELDS = ['email', 'first_name']

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"







# @api_view(["POST"])
# def RegisterUser(request):
#     try:
#         myuser = request.data
#         username = myuser["username"]
#         email = myuser["email"]
#         password = myuser["password"]
#         confirm_password = myuser["confirm_password"]
#         encryptedpassword=make_password(password)
#         checkpassword=check_password(password, encryptedpassword)
#         first_name = myuser["first_name"]
#         last_name = myuser["last_name"]

#         if password==confirm_password:
#             if Registration.objects.filter(username=username).exists():
#                 return Response({"message": "Username taken"})
            
#             elif Registration.objects.filter(email=email).exists():
#                 return Response({"message": "Email taken"})
            
#             else:
#                 user = Registration(username=username, email=email, password=encryptedpassword, first_name=first_name, last_name=last_name)
#                 user.save()

#                 serialized_registered_user = RegistrationSerializer(user, many=False)
#                 return Response(serialized_registered_user.data) 
#         else:
#             return Response({"message": "Unmatching password"})

#     except Exception as ex:
#         print(ex)
#         return Response({"message": ex})
    
    

# @api_view(["POST"])
# def LoginUser(request):
#     try:
#         mylogin = request.data
#         username = mylogin["username"]
#         password = mylogin["password"]

#         userlogin = auth.authenticate(request, username=username, password=password)
#         if userlogin is not None:
#             auth.login(request, userlogin)

#             serialized_login_user = RegistrationSerializer(userlogin, many=False)
#             return Response(serialized_login_user.data)
#         else:
#             return Response({"message": "Incorrect details"})
        
#     except Exception as ex:
#         print(ex)
#         return Response({"message": ex})