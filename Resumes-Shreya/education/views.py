from django.template import RequestContext
from django.core.mail import EmailMessage
from django.core.mail import *
import smtplib
from .forms import CompanyForm
from .forms import SecondaryEducationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import SignUpForm
from django.utils import timezone
from .models import Education, Company
from django.db.models import Q
from .forms import SearchForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        # user.is_active = True
        # user.profile.email_confirmed = True
        # request.user.last_name = True
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        #request.user.last_name = 'True'
        #Education.CompanyForm.name =''
        # form = SignUpForm()
        # form.save(user)
        # user.save()
      #  form.save()


        login(request, user)
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            # #username = form.cleaned_data.get('username')
            # #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            user = form.save(commit=False)
            user.is_active = True

            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your All About Resumes Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            #email =EmailMessage(str(subject), str(message), to = [user.email_user])
            #email.send()
            user.email_user(subject, message)
            # email=EmailMessage('Subject', )
            # email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    #request.user.is_active = True
    #request.user.profile.email_confirmed = True
    #request.user.last_name = 'True'
    return render(request, 'education/mail_confirm.html')





def emailSection(request, id= id):
    # User = get_user_model()
    #email1 = request.user.email
    email1 = User.objects.filter(Q(id =id)).values('email')
    name1 = Education.objects.filter(Q(id=id)).values('name')
    # queryset = Education.objects.filter(Q(id = id))
    # for q in queryset:

    email = EmailMessage('Subject: All About Resumes Shortlisting', 'Body: Hello'+str(name1), to = [email1])
    email.send()
    return render(request, 'education/mail_confirm.html')


def results(request):
    form = SearchForm()
    query = request.GET.get("search")
    q_list = Education.objects.all().values('user_id','name', 'work', 'skills' ).order_by('name')
    if query:
        q_list = q_list.filter(Q(work = query)).order_by('name')
    return render (request, 'education/results.html', {'query': query,'q_list':q_list,  'form': form})

@login_required
def home(request):
    #name = request.user.username
    return HttpResponseRedirect(reverse(edu_new, args=[request.user.username]))


def company_no_edit(request, id=id):
    queryset = Company.objects.filter(Q(user_id=id))
    return render(request, 'education/company_uneditable.html', {'queryset': queryset})


def non_edit(request, id=id):
    queryset = Education.objects.filter(Q(id=id))
    return render(request, 'education/edu_uneditable.html', {'queryset': queryset})


def candidate_profile(request, id):
    queryset = Education.objects.filter(Q(user_id=id))
    return render(request, 'education/company_search_uneditable.html', {'queryset': queryset})


# def profile(request, name):
#     user = get_object_or_404(User, username=name)
#     return render(request, 'education/edu_edit.html', {'profile': user})

def login_success(request):
    test = request.user.first_name
    test1 = request.user.profile.email_confirmed
    if test1 == True:
        if test == '0':
            return redirect('education/')
        else:
            return redirect('company/')
    #else:
    return render(request, 'education/login_fail.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             # user = form.save()
#             # #user.is_active = False
#             # request.user.last_name = False
#             # user.save()
#             # current_site = get_current_site(request)
#             # subject = 'Activate Your All About Resumes Account'
#             # message = render_to_string('account_activation_email.html', {
#             #     'user': user,
#             #     'domain': current_site.domain,
#             #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             #     'token': account_activation_token.make_token(user),
#             # })
#             # user.email_user(subject, message)
#
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login/')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def edu_new(request, id=id):
    id = request.user.id
    # user = get_object_or_404(User, username = name)  #may be reques.id or id in function arguements
    if request.method == "POST":
        form = SecondaryEducationForm(request.POST)
        if form.is_valid():
            t, created = Education.objects.update_or_create(user_id = id)
            t_form= SecondaryEducationForm(request.POST, instance= t)
            t_form.save()
            t.save()
            return redirect('/unedit/%s/' %id)
            # t.user_id = request.user
            # t.created_date = timezone.now()
            # t.save()
    else:
        t, created = Education.objects.get_or_create(user_id = id)
        t_form = SecondaryEducationForm(instance= t)

        return render(request, 'education/edu_edit.html', {'form': t_form})


# def edu_new(request, id=id):
#     id = request.user.id
#     # user = get_object_or_404(User, username = name)  #may be reques.id or id in function arguements
#     if request.method == "POST":
#         form = SecondaryEducationForm(request.POST)
#         if form.is_valid():
#             t = Education.objects.get(user_id = id)
#             t_form= SecondaryEducationForm(request.POST, instance= t)
#             t_form.save()
#             t.save()
#             return redirect('/unedit/%s/' %id)
#             # t.user_id = request.user
#             # t.created_date = timezone.now()
#             # t.save()
#     else:
#         t = Education.objects.get(user_id = id)
#         t_form = SecondaryEducationForm(instance= t)
#
#         return render(request, 'education/edu_edit.html', {'form': t_form})

def password_reset(request):
    form = PasswordForm()
    query = request.GET.get("email1")
    q_list = User.objects.all().values('password')
    for q in q_list:
   # if query:
        q_list = q_list.filter(Q(email = query))
    email = EmailMessage('Subject: password for all about resume portal', 'Body: password'+str(q_list), to = [query])
    email.send()
    return render (request, 'education/password_reset.html', {'query': query,'q_list':q_list,  'form': form})







def company_new(request, id=id):
    id = request.user.id
    # p = Company.user_id
    # p.save()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            t, created = Company.objects.update_or_create(user_id = id)
            # t = Company.objects.get(user_id=id)
            t_form = CompanyForm(request.POST, instance=t)
            t_form.save()
            t.save()
            return redirect('/edit/%s/' %id)  # CHECK
            # t.user_id = request.user
            # t.created_date = timezone.now()
            # t.save()
    else:
        t, created = Company.objects.get_or_create(user_id = id)
        t_form = CompanyForm(instance=t)

        return render(request, 'education/edu_edit2.html', {'form': t_form}) # edu_edit2 is HTML for company form

