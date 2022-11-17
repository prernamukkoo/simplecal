from multiprocessing import context

from django.shortcuts import render, redirect

# Create your views here.
def demo(request):
    template_name = "app/index.html"
    return render(request, template_name)

def result(request):
    template_name = "app/result.html"
    context={}
    firstNumber = float(request.POST.get('firstnumber'))
    secondNumber = float(request.POST.get('secondnumber'))
    calc = int(request.POST.get('calculate'))
    try:
        if calc==1:
            result=firstNumber+secondNumber
        elif calc==2:
            result=firstNumber-secondNumber 
        elif calc==3:
            result=firstNumber*secondNumber 
        elif calc==4:
            result=firstNumber/secondNumber 
        else:
            result=0 
        context |=({
            'result': result
        })                      
        return render(request, template_name, context)
    except:
        return redirect('demo')
