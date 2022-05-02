from django.shortcuts import render

# Create your views here.

def Agent_dashboard(request):
    return render(request,'Agent/agent_dashbord.html',{})
    