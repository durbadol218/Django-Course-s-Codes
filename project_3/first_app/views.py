from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    dic = {'author':'Rahim','age':9,'lst':['python','is','best'],'birthday': datetime.datetime.now() ,'val':'','courses':[
        {
            'id':1,
            'name':'Python',
            'fee':4890
        },
        {
            'id':2,
            'name':'Flutter Dev',
            'fee':6000
        },
        {
            'id':3,
            'name':'Java',
            'fee':3000
        },
        {
            'id':4,
            'name':'Django',
            'fee':5000
        },
        {
            'id':5,
            'name':'HTML-CSS',
            'fee':2500
        }
    ]}
    return render(request,'home.html',dic)