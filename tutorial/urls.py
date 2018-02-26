from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
# from tasks.views import TaskViewSet
from users.views import ActivateUser, CreateUserView, UserViewSet
from snippets.views import SnippetViewSet

router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    # url(r'^', include('snippets.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url('^api-register/$', CreateUserView.as_view()),
    url(
        '^api-activate/(?P<token>.+?)/$',
        ActivateUser.as_view(),
        name='activate-user'
    ),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

# from django.conf.urls import url, include
# from django.conf.urls import include
# from rest_framework.schemas import get_schema_view
#
# schema_view = get_schema_view(title='Pastebin API')
#
# urlpatterns = [
#     url(r'^schema/$', schema_view),
#     url(r'^', include('snippets.urls')),
# ]
#
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]