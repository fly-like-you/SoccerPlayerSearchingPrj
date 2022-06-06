import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',       #사용할 DB
        'NAME': 'DEPPODB',                          #DB이름
        'USER': 'deppoDB',                          #사용자이름
        'PASSWORD': 'DEPPODB!!!q1w2e3r4',           # 패스워드
        'HOST': '203.255.57.227',                   # 아이피 주소
        'PORT': '3306',                             # 포트 번호
    }
}
SECRET_KEY = os.environ.get('SECRET_KEY','django-insecure-9hh7)3muc5^+u@_)7f-==dx1s1hmjbn9j3+1pe^%h&5n(88=i9')