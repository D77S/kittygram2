from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# user/password: newuser1/pass123123
# "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5ODc2NTc5MCwianRpIjoiNjRjZThmMmU1Y2RkNDRmY2IxODk4MTIxNGVmMjdhZjYiLCJ1c2VyX2lkIjoxfQ._Of3dHseOXsIdc6lqU7ZIs2gJ_lugHxg0UJVNlz7Nyg",
#    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NzY1NzkwLCJqdGkiOiJiYmJkMWViZWVkNDE0OGU0OTlmZTEyNDg0Yzc0NGVhOCIsInVzZXJfaWQiOjF9.1ZcRowMsFjxzh_C2jORYvauJmmTRbwzmNdYVazDMV6s"
#
# user/password: newuser2/pass123123
# "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5ODc2NjIxMywianRpIjoiZGE0NzY0MzczMjNkNDNmMGFhZTIxYTVkOTQ1YmNlNGEiLCJ1c2VyX2lkIjoyfQ. lOHOGInJOpotFQQ44h1wR-CQ5tN5PSC9r5WkVGnb784",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NzY2MjEzLCJqdGkiOiI2YzhkYWJjZTg3NjQ0MzEyYTJmNjdiNDJkZDYyYmUxZSIsInVzZXJfaWQiOjJ9.PW5mtzUkHNg8R-txk3_RjxHbBE74evIyDnmD4YbXCQU"
