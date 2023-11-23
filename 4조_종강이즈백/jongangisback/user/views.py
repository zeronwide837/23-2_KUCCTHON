from django.shortcuts import render, redirect
from user.models import User, UserManager
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    if request.method == 'POST':
        store_id = request.POST.get('store_id')
        return redirect(f'/ranking/?store_id={store_id}')
        # return render(request, "ranking.html", {'store_id' : store_id})
    return render(request, "map.html")  

def signup_view(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        people = request.POST.get('people')
        store_id = request.POST.get('store_id')
        soju_quantity = request.POST.get('soju_quantity')
        beer_quantity = request.POST.get('beer_quantity')
        makguli_quantity = request.POST.get('makguli_quantity')
        alcohol = (float(soju_quantity) * 0.076 + float(beer_quantity) * 0.031 + float(makguli_quantity) * 0.031) / float(people)
        password = "a1b2c3d4"
        # form의 완성도 검증
            # user 객체를 새로 생성
        user = User.objects.create_user(user_id = user_id,
                                        password= password,
                                        people =  people,
                                        store_id = store_id,
                                        soju_quantity = soju_quantity,
                                        beer_quantity = beer_quantity,
                                        makguli_quantity = makguli_quantity,
                                        alcohol = alcohol
                                        )
        # 로그인 한다
        auth.login(request, user)
        # home으로 돌려보내준다     
        return render(request, "modal.html")  
        # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    else:  
        return render(request, 'modal.html')

# def order_view(request):

    

# def order(request):
#     user = request.user
#     user_id = user.user_id
#     if request.method == 'POST':
