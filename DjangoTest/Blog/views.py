from django.shortcuts import get_object_or_404, render
from .models import Table 

# Create your views here.

def index(request):
    AllObject = Table.objects.all();
    return render(request, 'Blog/index.html', {'object_list':AllObject})

def read(request, Number):
    Obj = get_object_or_404(Table, id=Number)
    return render(request, 'Blog/Detail.html', {'object':Obj})

'''
def update(request, page_id):
    Object = Table.objects.all()
    OneObj = Object[Object.index(page_id)]
    if request == ['POST']:
        XXXXXX여기서 부터 모르겠어요. 
제가 저번주에 Craete를 안배워서 PageForm이 뭔지를 모릅니다. update랑 craete는 모르겠어요.. 죄송합니다.
'''