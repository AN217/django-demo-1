from rest_framework.routers import SimpleRouter
from api.controllers.views import DiagModelViewSet
s=SimpleRouter()
s.register('diag', DiagModelViewSet)
urlpatterns = [

]
urlpatterns += s.urls
