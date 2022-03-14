from django.http import JsonResponse

# api home
def api_home(request):
    return JsonResponse({'message': 'Hello World'})
