# Device registry service

## Usage

All responses will have a form 

``` json 
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"

}
```

Subsequent response definition will only detail the expected value of the "data filed".

### List all devices 

**Definition**

`GET / devices`

**Response**

- `200 OK`