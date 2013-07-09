from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from portal.models import project 
from portal.models import article
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_protect
from portal.forms import Registration_Form
from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from portal.models import user_extra_field

@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    all_article = article.objects.all()
    default = article.objects.filter(id = 1)[0]

    return render_to_response('portal/portal.html',
    {
        'article':all_article,
        'default':default
    }
    )

#test how to call the article specificly
def ourhistory(request, article_name):
    link = article_name.split('_')
    link = ' '.join(link)
    specific_article = article.objects.filter(title = link)[0]
    

    return render_to_response('portal/ourhistory.html',
    {
        'ourhistory':specific_article
    }
    )

#################################
# User Registration Handling
#################################
@csrf_protect
def register(request):
    if request.method == 'POST':

        register_form = Registration_Form(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            
            new_username = cd['username']
            new_pwd = cd['password1']
            new_gender = cd['gender']
            new_email = cd['email']

            usr = User.objects.create_user(username=new_username,
                                            email=new_email,
                                            password=new_pwd)
            extra = user_extra_field.objects.create(user=usr, gender = new_gender[0])
            usr.save()
            extra.save() 

            return HttpResponseRedirect('/login')
        else:
            print register_form.errors
            return render(request, 'registration/register.html', {'form': register_form})
        
    else:
        register_form = Registration_Form()
    return render(request, 'registration/register.html', {'form': register_form})


