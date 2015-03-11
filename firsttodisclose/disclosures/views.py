from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from disclosures.models import Disclosure
from forms import SubmissionForm

from django.http import HttpResponseRedirect

def index(request):
    return render_to_response("index.html", None, RequestContext(request))

def show_disclosure(request, pk):
    disc = Disclosure.objects.get(pk=pk)

    return render_to_response("disclosure_view.html", {'disclosure': disc}, RequestContext(request))

def search(request):
    query = request.REQUEST.get('q', '')

    context = {'query': query}
    if query:
        results = Disclosure.objects.filter(Q(title__icontains=query) |
                                            Q(abstract__icontains=query) |
                                            Q(body__icontains=query))
        context['results'] = results
    else:
        results = Disclosure.objects.all().order_by('-created')[:10]
        context['results'] = results

    return render_to_response("search.html", context, RequestContext(request))

def agreements(request):
    return render_to_response("agreements.html", None, RequestContext(request))

# def disclosure(request):
#     return render_to_response("disclosure.html", None, RequestContext(request))

def disclosure(request):
    # Validate all fields
    print "alive!"
    context = dict()

    if request.method == "POST":
        # Do something
        print "sending form"
        disclosure = SubmissionForm(request.POST)
        if disclosure:
            template = "disclosure_post.html"
            context['success_message'] = "Disclosure created" 
            ################
            # REFACTOR
            #
            # Save it in some manner
            if disclosure.is_valid():
                new_disclosure = Disclosure()
                new_disclosure.title = disclosure.cleaned_data.get("title", None)
                new_disclosure.abstract = disclosure.cleaned_data.get("abstract", None)
                new_disclosure.abstract_file = disclosure.cleaned_data.get("abstract_file", None)
                new_disclosure.body = disclosure.cleaned_data.get("body", None)
                new_disclosure.body_file = disclosure.cleaned_data.get("body_file", None)
                new_disclosure.owner = User.objects.all()[0]

                new_disclosure.save()
                disclosure_id = new_disclosure.id
                # 
                ################
            return HttpResponseRedirect('/disclosure/{0}'.format(disclosure_id))

    else:            
        template = "disclosure.html"
        context['error_message'] = "Invalid disclosure" 
        form = SubmissionForm()
        print "getting form"
        return render(request, template, {'form': form})

def tag(request):
    return render_to_response("tag.html", None, RequestContext(request))

def faq(request):
    return render_to_response("faq.html", None, RequestContext(request))
