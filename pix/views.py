from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import ImageForm, ProfileForm
from .models import Image, Profile, Comments



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your instagram account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.''<a href="/accounts/login/"> click here </a>')
    else:
        return HttpResponse('Activation link is invalid!''<br> If you have an account <a href="/accounts/login/"> Log in here </a>')

@login_required(login_url='/accounts/login/')
def index(request):
    """
    Function that renders the landing page
    """
    images = Image.get_images().order_by('-posted_on')

    return render(request, 'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def new_post(request):
    """
    Function that enables one to upload images
    """
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

        return redirect('landing')
    else:
        form = ImageForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def like_post(request):
    image = get_object_or_404(Image, id=request.POST.get('image_id'))
    image.likes.add(request.user)
    return redirect('landing')









