from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home view</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consuem by JavaScript or Swift or Java/iOS/Android
    return json data
    """
    
    data = {
        "id" : tweet_id,
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = onj.content
    except:
        data['message'] = 'Not found'
        status = 404

    return JsonResponse(data, status=status) # json.dumps content_type='aplication/json'