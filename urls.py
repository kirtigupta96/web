from django.conf.urls import url, include
from django.contrib import admin
from education import views as core_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from education import views as core_views

urlpatterns = [
    url(r'^signup/account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^signup/$', core_views.signup, name='signup'),







    url(r'^login_success/search/candidate_profile_(?P<id>.+)/$', core_views.candidate_profile, name='candidate_profile'),
    url(r'^login_success/candidate_shortlisted/(?P<id>.+)/$', core_views.emailSection, name='emailSection'),


    url(r'^admin/', admin.site.urls),
    url(r'login_success/$', core_views.login_success, name='login_success'),
    url(r'^accounts/profile/(?P<id>\d+)', core_views.edu_new, name='edu_new'),
    url(r'^login_success/education/$', core_views.edu_new, name='edu_new'),
   #  url(r'^login/education/', core_views.edu_editable, name='edu_editable'),
   #   url(r'^login/education/(?P<name>.+)/$', core_views.edu_editable, name='edu_editable'),
    url(r'^login_success/education/(?P<id>.+)/$', core_views.edu_new, name='edu_new'),
    url(r'^login_success/company/(?P<id>.+)/$', core_views.company_new, name='company_new'),
    url(r'^login_success/company/$', core_views.company_new, name='company_new'),
     url(r'^signup/login/education/(?P<id>.+)/$', core_views.edu_new, name='edu_new'),
     url(r'^signup/login/education/$', core_views.edu_new, name='edu_new'),
    url(r'^company/$', core_views.company_new, name='company_new'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^companyunedit/(?P<id>[0-9]+)/search/$', core_views.results, name='results'),
    # url(r'^profile/(?P<id>[0-9]+)/$', core_views.non_edit, name='non_edit'),
    url(r'^login_success/education/unedit/(?P<id>.+)/$', core_views.non_edit, name='non_edit'),
    url(r'^unedit/(?P<id>.+/)$', core_views.non_edit, name='non_edit'),
    url(r'edit/(?P<id>.+)/$', core_views.company_no_edit, name='company_no_edit'),
    url(r'^login_success/search/$', core_views.results, name='results'),
    # url(r'^companyunedit/(?P<id>[0-9]+)/$', core_views.company_no_edit, name='company_no_edit'),

    # url(r'^profile/emailsent/(?P<id>.+)/$', core_views.emailSection, name= 'emailSection'),










]
