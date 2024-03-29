from django.http import HttpResponseRedirect


def login_is_required(function=None, redirect_url='login'):
    def decorator(view_func):
        def wrapper (request, *args, **kwargs):
            if 'adminuser_email' not in request.session.keys():
                return HttpResponseRedirect(redirect_url)
            else:
                return view_func (request, *args, **kwargs)
                    
        return wrapper
    if function:
        return decorator(function)

    return decorator