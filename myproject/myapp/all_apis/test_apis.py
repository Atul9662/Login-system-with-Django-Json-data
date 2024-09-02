import json
from django.http import JsonResponse
import logging

logger = logging.getLogger('myapp')

def testing_api(request):
    logger.debug("Logs in getting tested")

    data = {
        'message': 'Testing apis structures',
        'status': 200,

    }
    return JsonResponse(data)
