from django.shortcuts import render

def activation_view(request):
    verification_code = request.GET.get('verification')
    return render(request, 'email_verify.html', {'verification_code': verification_code})