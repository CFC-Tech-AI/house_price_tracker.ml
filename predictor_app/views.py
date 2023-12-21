from django.shortcuts import render
from .forms import HouseForm
from .predict import predict_price

def predict(request):
    form = HouseForm(request.POST or None)
    predicted_price = None
    
    if form.is_valid():
        house = form.save(commit=False)
        predicted_price = round(predict_price(house))
        print(f"Input Data: {house.bedrooms} bedrooms, {house.location}, {house.square_footage} square footage")
        print(f"Predicted Price: Rs. {predicted_price}")
        house.price = predicted_price
        house.save()

    return render(request, 'predict.html', {'form': form, 'predicted_price': predicted_price})
