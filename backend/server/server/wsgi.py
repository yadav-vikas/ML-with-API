"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from ml.income_classifier.extra_trees import ExtraTreesClassifier

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# Machine learning algorithms registry
import inspect
from ml.registry import MLRegistry
from ml.income_classifier.random_forest import RandomForestClassifier

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))

    et = ExtraTreesClassifier()

    registry.add_algorithm(
        endpoint_name="income_classifier",
        algorithm_object=et,
        algorithm_name="extra trees",
        algorithm_status="testing",
        algorithm_version="0.0.1",
        owner = "Piotr",
        algorithm_description="Extra Trees with simple pre- and post-processing",
        algorithm_code=inspect.getsource(ExtraTreesClassifier)
    )

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))

# The registry code is ready, we need to specify one place in the server code which will add ML algorithms 
# to the registry when the server is starting. 
# The best place to do it is wsgi.py