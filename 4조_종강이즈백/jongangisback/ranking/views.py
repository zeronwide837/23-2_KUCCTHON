from django.shortcuts import render
from user.models import User
from django.contrib import auth

def ranking_view(request):
    store_id = request.GET.get('store_id')
    print(store_id)
    user = request.user
    try:
        user_id = user.user_id
        filtered_data = User.objects.filter(store_id=store_id)
        sorted_data = sorted(filtered_data, key = lambda x: x.alcohol, reverse=True)

        current_user_data = User.objects.filter(user_id = user_id).first()

        # 이름, 인원, 알콜, 소, 맥, 막
        top_three_quantities = [{
            'user_id':     sorted_data[0].user_id,
            'people': sorted_data[0].people,
            'percentage': sorted_data[0].alcohol,
            'soju_quantity': sorted_data[0].soju_quantity,
            'beer_quantity': sorted_data[0].beer_quantity,
            'makguli_quantity': sorted_data[0].makguli_quantity,},
            {
               'user_id': sorted_data[1].user_id,
            'people':sorted_data[1].people,
            'percentage':sorted_data[1].alcohol,
            'soju_quantity':sorted_data[1].soju_quantity,
            'beer_quantity':sorted_data[1].beer_quantity,
            'makguli_quantity': sorted_data[1].makguli_quantity,
            },
            {
            'user_id':sorted_data[2].user_id,
            'people':sorted_data[2].people,
            'percentage':sorted_data[2].alcohol,
            'soju_quantity':sorted_data[2].soju_quantity,
            'beer_quantity':sorted_data[2].beer_quantity,
            'makguli_quantity':sorted_data[2].makguli_quantity,
            },
            {
            'user_id':current_user_data.user_id,
            'people':current_user_data.people,
            'percentage':current_user_data.alcohol,
            'soju_quantity':current_user_data.soju_quantity,
            'beer_quantity':current_user_data.beer_quantity,
            'makguli_quantity':current_user_data.makguli_quantity,
            }
        ]
        context = {
            'top_three_quantities' : top_three_quantities,
        }
        print(context)
    except AttributeError:
        filtered_data = User.objects.filter(store_id=store_id)
        sorted_data = sorted(filtered_data, key = lambda x: x.alcohol, reverse=True)
    # 이름, 인원, 알콜, 소, 맥, 막
        top_three_quantities = [{
            'user_id':     sorted_data[0].user_id,
            'people': sorted_data[0].people,
            'percentage': sorted_data[0].alcohol,
            'soju_quantity': sorted_data[0].soju_quantity,
            'beer_quantity': sorted_data[0].beer_quantity,
            'makguli_quantity': sorted_data[0].makguli_quantity,},
            {
            'user_id': sorted_data[1].user_id,
            'people':sorted_data[1].people,
            'percentage':sorted_data[1].alcohol,
            'soju_quantity':sorted_data[1].soju_quantity,
            'beer_quantity':sorted_data[1].beer_quantity,
            'makguli_quantity': sorted_data[1].makguli_quantity,
            },
            {
            'user_id':sorted_data[2].user_id,
            'people':sorted_data[2].people,
            'percentage':sorted_data[2].alcohol,
            'soju_quantity':sorted_data[2].soju_quantity,
            'beer_quantity':sorted_data[2].beer_quantity,
            'makguli_quantity':sorted_data[2].makguli_quantity,
            },
        ]

        context = {
            'top_three_quantities' : str(top_three_quantities),
        }
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
        print(context)
    return render(request, 'ranking.html', (context))