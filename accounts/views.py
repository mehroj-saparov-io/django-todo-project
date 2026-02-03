from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from django.contrib import messages

# from .models import User, EmailOTP
# from .tokens import generate_otp


def register_view(request):
    return HttpResponse('register')
# def register_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Bu email allaqachon mavjud")
#             return redirect('register')

#         user = User.objects.create_user(email=email)
#         user.set_unusable_password()
#         user.save()

#         otp = generate_otp()
#         EmailOTP.objects.create(user=user, otp=otp)

#         send_mail(
#             subject='Your OTP Code',
#             message=f'Your OTP code is: {otp}',
#             from_email='noreply@todo.com',
#             recipient_list=[email],
#         )

#         request.session['email'] = email
#         return redirect('verify-otp')

#     return render(request, 'accounts/register.html')

# def verify_otp_view(request):
#     if request.method == 'POST':
#         email = request.session.get('email')
#         otp_input = request.POST.get('otp')

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             messages.error(request, "User topilmadi")
#             return redirect('register')

#         otp_obj = EmailOTP.objects.filter(user=user, otp=otp_input).last()

#         if otp_obj and not otp_obj.is_expired():
#             user.is_active = True
#             user.save()
#             otp_obj.delete()
#             messages.success(request, "Account muvaffaqiyatli aktivlashtirildi")
#             return redirect('login')
#         else:
#             messages.error(request, "OTP noto‘g‘ri yoki eskirgan")

#     return render(request, 'accounts/verify_otp.html')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             messages.error(request, "Bunday user yo‘q")
#             return redirect('login')

#         if not user.is_active:
#             messages.error(request, "Account aktiv emas")
#             return redirect('login')

#         login(request, user)
#         return redirect('todo-list')

#     return render(request, 'accounts/login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')
