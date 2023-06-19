# Property_Price_Prediction


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







