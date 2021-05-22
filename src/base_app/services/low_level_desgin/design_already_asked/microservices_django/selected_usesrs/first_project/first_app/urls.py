from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index),
#     # path('', views.index, name='index'),
#     # path('/$', views.index.as_view(), name='index'),
#     #     webservice URI. API endpoint.
# ]

urlpatterns = [
    # path('', views.Index_2),
    path('', views.index, name='index'),
    # path('/$', views.index.as_view(), name='index'),
    #     webservice URI. API endpoint.
]


# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url(r'/$', views.index.as_view()),
#     # url(r'^users/$', views.user_list.as_view()),
#     # url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail.as_view()),
# ]
