from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def masterfile(request):
    return render(request, "masterfile.html")  

def admin_invite(request):
    return render(request, "admin_invite.html")
    
def admin_confirmation(request):
    return render(request, "admin_confirmation.html") 



def contact_acknowledgement(request):
    return render(request, "contact_acknowledgement.html")

def story_acknowledgement(request):
    return render(request, "story_acknowledgement.html")



def mailing_list_signup(request):
    return render(request, "mailing_list_signup.html")

def sample_session_signup(request):
    return render(request, "sample_session_signup.html")

def bibeats_signup(request):
    return render(request, "bibeats_signup.html")

def webinar_signup(request):
    return render(request, "webinar_signup.html")

def ebook_signup(request):
    return render(request, "ebook_signup.html")



def therapist_listing(request):
    return render(request, "therapist_listing.html")

def therapist_delisting(request):
    return render(request, "therapist_delisting.html")



def welcome_regular(request):
    return render(request, "welcome_regular.html")

def welcome_coaching(request):
    return render(request, "welcome_coaching.html")

def welcome_gift(request):
    return render(request, "welcome_gift.html")

def welcome_gift_sender(request):
    return render(request, "welcome_gift_sender.html")

def welcome_access_code(request):
    return render(request, "welcome_access.html")

def welcome_first_responder(request):
    return render(request, "welcome_first_responder.html")



def coaching_confirmation(request):
    return render(request, "coaching_confirmation.html")

def coaching_reminder(request):
    return render(request, "coaching_reminder.html")

def coaching_noshow(request):
    return render(request, "coaching_noshow.html")



def create_profile(request):
    return render(request, "create_profile.html")

def password_reset(request):
    return render(request, "password_reset.html") 

def update_profile(request):
    return render(request, "update_profile.html") 

def change_plan(request):
    return render(request, "change_plan.html")

def account_lock(request):
    return render(request, "account_lock.html")

def trial_end(request):
    return render(request, "trial_end.html")

def gift_end(request):
    return render(request, "gift_end.html")

def renewal_upcoming(request):
    return render(request, "renewal_upcoming.html")

def renewal_confirmation(request):
    return render(request, "renewal_confirmation.html")

def cancellation(request):
    return render(request, "cancellation.html")
