from django.shortcuts import render

def index (request): 
    kars = Car.objects.all()
    
    # Cars = carListing.objects.order_by('-list_date')
    return render(request, 'saroyaApp/index.html', {'kars':kars})

