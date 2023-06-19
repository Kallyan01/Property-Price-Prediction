# Property_Price_Prediction


## How to Run ?

- Run the jupyter_notebook/property_price_predictor-2.ipynb

- It will create Model.pkl and cleaned_data.csv 
- Move them to root folder and run the flask application 


## API Reference



#### Get Price

```http
  POST /predict
```



| Body | Type     |  Description| 
| :-------- | :------- |  :------- | 
| `bhk`      | `String` | `BHK needed in number eg. 2 `
| `sqft`      | `String` | `Area in sqft unit eg. 1200` 
| `zipcode`      | `String` | `Zipcode of the area eg. 98178` 

Generate the predicted price for the Property







