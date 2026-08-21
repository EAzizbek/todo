from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health(request):
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    path('', health),
    path('health/', health),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/todos/', include('todos.urls')),
]
