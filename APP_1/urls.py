from django.urls import path
from APP_1.views import *
app_name='something'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('devilers/',devilers,name='devilers'),
]