from django.shortcuts import render_to_response


def index(request):
	return render_to_response('pages/Simular1.html')

def simular2(request):
	rut = request.GET.get('rut')
	monto = request.GET.get('monto')
	renta = request.GET.get('renta')
	cuota = request.GET.get('cuota')
	
	monto2=int(monto)
	cuota2=int(cuota)
	mensual=monto2/cuota2

	return render_to_response('pages/Simular2.html', {'monto':monto, 'mensual':mensual, 'cuota':cuota})

def simular3(request):
    return render_to_response('pages/Simular3.html')
