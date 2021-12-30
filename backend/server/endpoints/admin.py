from django.contrib import admin

from endpoints.models import Endpoint
from endpoints.models import MLAlgorithm
from endpoints.models import MLAlgorithmStatus
from endpoints.models import MLRequest
from endpoints.models import ABTest

admin.site.register(Endpoint)
admin.site.register(MLAlgorithm)
admin.site.register(MLAlgorithmStatus)
admin.site.register(MLRequest)
admin.site.register(ABTest)