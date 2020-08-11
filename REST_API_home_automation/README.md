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

- `200 OK` on success


Define a data field with an array of objects. This collection could be emptly if there were no devices in the registry, but ususally it is going to return multiple objects, where each object represent a particular device.

```json

[
    {
        "idetified" : "floor-lamp",
        "name": "Floor Lamp",
        "device_type": "switch",
        "controller_gateway": "192.1.68.0.2"  
    },
    {
        "idetified" : "samsung-smarttv",
        "name": "Living Room TV",
        "device_type": "multimedia",
        "controller_gateway": "192.1.68.0.9"  
    }
]
``` 
### Registering a new device

**Definition**

`POST / devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type":string` the type fo the device as understood by the client
- `"controller_gateway":string` the IP addres of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "idetified" : "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"  
}
```

## Lookup device details 

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

So we are going to return a single object (like in previous example)

```json
{
    "idetified" : "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"  
}
```

## Delete a device

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No content` no useful data to return