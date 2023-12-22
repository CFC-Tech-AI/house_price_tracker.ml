from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from .models import House
import pandas as pd

def predict_price(house):
   
    dataset = pd.read_csv('predictor_app/price_data.csv')

    
    X = dataset[['bedrooms', 'location', 'square_footage']]
    y = dataset['price']

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

 
    preprocessor = ColumnTransformer(
        transformers=[
            ('location', OneHotEncoder(handle_unknown='ignore'), ['location'])
        ],
        remainder='passthrough'
    )

   
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    model.fit(X_train, y_train)

 
    input_data = pd.DataFrame([[house.bedrooms, house.location, house.square_footage]], columns=['bedrooms', 'location', 'square_footage'])
    predicted_price = model.predict(input_data)
    return predicted_price[0]




