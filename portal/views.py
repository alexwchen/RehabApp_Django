from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from portal.models import article
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_protect
from portal.forms import Registration_Form
from portal.forms import DocumentForm
from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from portal.models import user_extra_field
from portal.models import user_audio

"""
If users are authenticated, direct them to the main page. Otherwise, take
them to the login page.
"""
@csrf_protect
@login_required
def portal_main_page(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = user_audio(user=request.user, docfile = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect('/portal/')
        else:
            form = DocumentForm()

    all_article = article.objects.all()
    default = article.objects.filter(id = 1)[0]

    return render_to_response('portal/portal.html',
    {
        'article':all_article,
        'default':default,
        'form':DocumentForm()

    },
     context_instance=RequestContext(request)
    )

#test how to call the article specificly
def get_article_text(request, article_name):
    link = article_name.split('_')
    link = ' '.join(link)
    specific_article = article.objects.filter(title = link)[0]

    return HttpResponse(specific_article.text)
   
def get_article_author(request, article_name):
    link = article_name.split('_')
    link = ' '.join(link)
    specific_article_author = article.objects.filter(title = link)[0]

    return HttpResponse(specific_article_author.authors)

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
            print register_form
            return render(request, 'registration/register.html', {'form': register_form})
        
    else:
        register_form = Registration_Form()
    return render(request, 'registration/register.html', {'form': register_form})






