from django.urls import path, include, re_path
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter

from endpoints.views import EndpointViewSet
from endpoints.views import MLAlgorithmViewSet
from endpoints.views import MLAlgorithmStatusViewSet
from endpoints.views import MLRequestViewSet
from endpoints.views import PredictView
from endpoints.views import ABTestViewSet
from endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")
router.register("abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    re_path(r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
    re_path(r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab"),
] # http://<server-ip>/api/v1/<object-name>