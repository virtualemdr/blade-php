"""vemdr_blade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('masterfile', views.masterfile, name="masterfile"),

    path('admin_invite', views.admin_invite, name="admin_invite"),  
    path('admin_confirmation', views.admin_confirmation, name="admin_confirmation"),  

    path('contact_acknowledgement', views.contact_acknowledgement, name="contact_acknowledgement"),
    path('story_acknowledgement', views.story_acknowledgement, name="story_acknowledgement"),

    path('mailing_list_signup', views.mailing_list_signup, name="mailing_list_signup"),
    path('sample_session_signup', views.sample_session_signup, name="sample_session_signup"),
    path('bibeats_signup', views.bibeats_signup, name="bibeats_signup"),
    path('webinar_signup', views.webinar_signup, name="webinar_signup"),
    path('ebook_signup', views.ebook_signup, name="ebook_signup"), 

    path('therapist_listing', views.therapist_listing, name="therapist_listing"),
    path('therapist_delisting', views.therapist_delisting, name="therapist_delisting"),  

    path('welcome_regular', views.welcome_regular, name="welcome_regular"),
    path('welcome_coaching', views.welcome_coaching, name="welcome_coaching"),
    path('welcome_gift', views.welcome_gift, name="welcome_gift"),
    path('welcome_gift_sender', views.welcome_gift_sender, name="welcome_gift_sender"),
    path('welcome_access_code', views.welcome_access_code, name="welcome_access_code"),
    path('welcome_first_responder', views.welcome_first_responder, name="welcome_first_responder"),

    path('coaching_confirmation', views.coaching_confirmation, name="coaching_confirmation"),
    path('coaching_reminder', views.coaching_reminder, name="coaching_reminder"),
    path('coaching_noshow', views.coaching_noshow, name="coaching_noshow"), 
    
    path('create_profile', views.create_profile, name="create_profile"),
    path('password_reset', views.password_reset, name="password_reset"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('change_plan', views.change_plan, name="change_plan"),
    path('account_lock', views.account_lock, name="account_lock"),

    path('trial_end', views.trial_end, name="trial_end"),
    path('gift_end', views.gift_end, name="gift_end"),
    path('renewal_upcoming', views.renewal_upcoming, name="renewal_upcoming"),
    path('renewal_confirmation', views.renewal_confirmation, name="renewal_confirmation"),

    path('cancellation', views.cancellation, name="cancellation"),
]
