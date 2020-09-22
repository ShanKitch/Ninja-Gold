from django.shortcuts import render,redirect
import random
from datetime import datetime 


def index(request):
    if "gold" not in request.session or "activities" not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render(request,'ninjagoldindex.html')

def process_money(request):
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    building = request.POST['building']
        
    if request.POST['building'] == 'farm':
        gold= random.randrange(10,20+1)
        result='win'
        
    elif request.POST['building'] == 'cave':
        gold= random.randrange(5,10+1)
        result='win'
        
    elif request.POST['building'] == 'house':
        gold= random.randrange(2,5+1)
        result='win'
       
    elif request.POST['building'] == 'casino':
        gold= random.randrange(-50,50+1)
        result='win'
    request.session['gold'] += gold
    
    if gold < 0:
        request.session['activities'].append("You entered a " + building + " and lost " + str(gold) + " gold! Bummer! " + time)
    else:
        request.session['activities'].append("You entered a " + building + " and earned " + str(gold) + " gold! " + time)
        result='win'
    request.session['gold'] += gold
    
    return redirect ('/')

def reset(request):
    if request.method == "POST":
        request.session['gold'] = 0
        request.session['activities'] = []
    return redirect('/')






        
            
   

    


