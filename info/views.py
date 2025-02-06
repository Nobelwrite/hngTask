from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import JsonResponse

@api_view(["GET"])
def get_info(request):
    return Response ({
            'email': 'damilolajoseph91@gmail.com',
            'current_datetime': timezone.now().strftime('%Y-%m-%dtH:%M:%SZ'),
            'github_url': 'https://github.com/Nobelwrite/myinfo'
    })


