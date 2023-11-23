from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함
class UserManager(BaseUserManager):
	# 필수로 필요한 데이터를 선언
    def create_user(self, user_id, people, store_id, soju_quantity, beer_quantity, makguli_quantity, alcohol, password = None):
        if not user_id:
            raise ValueError("Users must have id")
        user = self.model(
            user_id = user_id,
            people = people,
            store_id = store_id,
            soju_quantity = soju_quantity,
            beer_quantity = beer_quantity,
            makguli_quantity = makguli_quantity,
            alcohol = alcohol
        )
        user.set_password(password) # change user password
        user.save(using=self._db)
        return user 

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, user_id, people, store_id, soju_quantity, beer_quantity, makguli_quantity, alcohol, password=None):
        user = self.create_user(
            user_id = user_id,
            people = people,
            store_id = store_id,
            password = password,
            soju_quantity = soju_quantity,
            beer_quantity = beer_quantity,
            makguli_quantity = makguli_quantity,
            alcohol = alcohol
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    user_id = models.CharField("닉네임", max_length= 40, primary_key=True, unique=True)
    password = models.TextField("비밀번호")
    people = models.IntegerField("사람 수")
    store_id = models.CharField("가게이름", max_length= 40)
    soju_quantity = models.IntegerField("소주 병수")
    beer_quantity = models.IntegerField("맥주 병수")
    makguli_quantity = models.IntegerField("막걸리 병수")
    alcohol = models.DecimalField("알코올량", max_digits= 20, decimal_places= 5)

    # 활성화 여부 (기본값은 True)
    is_active = models.BooleanField(default=True)
    # 관리자 권한 여부 (기본값은 False)
    is_admin = models.BooleanField(default=False)
    # 
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['people', 'store_id', 'soju_quantity', 'beer_quantity', 'makguli_quantity','alcohol']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return f"{self.user_id}"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
 
