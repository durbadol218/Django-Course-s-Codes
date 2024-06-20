from django.shortcuts import render


# D:\Phitron\Software Development Track\Software Development\Django Course\project_2\templates
def index(request):
    return render(request,'index.htm')