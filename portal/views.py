from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from portal.models import project 
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
#from django.views.decorators.csrf import csrf_protect
#@csrf_protect



@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('portal/portal.html')


def user_test(request):
    
    print "****Fields on User Objects****"
    print ''

    request.user.first_name = 'Alex'
    firstname = request.user.first_name
    print 'firstname:   '+ firstname
    
    request.user.last_name = 'Chen'
    lastname = request.user.last_name
    print 'lastname:    '+ lastname
    
    print 'request.user.email:  '+request.user.email

    print 'is_staff:    ' + str(request.user.is_staff)
    print 'is_active:   ' + str(request.user.is_active)
    print 'is_superuser:    ' + str(request.user.is_superuser)
    print 'last_login:  ' + str(request.user.last_login)
    print 'date_joined: ' + str(request.user.date_joined)
    print ''

    print "****Methods on User Objects****"
    auth = request.user.is_authenticated()
    print 'is_authenticated:   ' + str(auth)

    anoy = request.user.is_authenticated()
    print 'is_anonymous():  ' + str(anoy) + '(should avoid this generally)'

    getfullname = request.user.get_full_name() 
    print 'get_full_name(): ' + str(getfullname)

    request.user.set_password('appleslice')   
    request.user.check_password('appleslice')  
    
    
    print "\n****Retrieve Group Permission****\n"
    group_list = request.user.get_group_permissions()
    for g in group_list:
        print g
    
    print "\n****All Permission List****\n"

    perm_list = request.user.get_all_permissions()   
    for p in perm_list:
        print p

    print "\n****Add Group To User****\n"
    g = Group.objects.get(name='Boss') 
    g.user_set.add(request.user)
    

    print "\n****Retrieve User****\n"
    user_h = User.objects.get(username__exact='harrisonwr')
    print user_h

    #request.user.groups.add(name='Boss')

    request.user.save()

    return render_to_response('portal/test.html')
