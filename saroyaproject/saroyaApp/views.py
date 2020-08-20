from django.shortcuts import render

def index (request): 
    # kars = Car.objects.all()
    
    # # Cars = carListing.objects.order_by('-list_date') , {'kars':kars}
    return render(request, 'saroyaApp/index-2.html')

