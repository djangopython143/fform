from django.shortcuts import render
from django.http.response import HttpResponse
from .models import FeedbackData
from .forms import FeedbackForm
from datetime import datetime
date1=datetime.now()
def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('Name')
            rating1=request.POST.get('Rating')
            feedback1=request.POST.get('Feedback')
            data=FeedbackData(name=name1,rating=rating1,feedback=feedback1,date=date1)
            x=data.rating
            data.save()
            fform=FeedbackForm()
            Feedbacks = FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'Feedbacks':Feedbacks})
        else:
            return HttpResponse('Invalid Form')
    else:
        fform=FeedbackForm()
        Feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'Feedbacks':Feedbacks})
