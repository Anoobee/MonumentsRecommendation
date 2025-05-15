# API Reference

## Endpoints

### Get Recommendations

```
POST /getRecommendations
```

Returns a list of monument recommendations based on location and preferences.

#### Request Parameters

| Parameter       | Type   | Description                     |
| --------------- | ------ | ------------------------------- |
| latitude        | float  | Latitude of your location       |
| longitude       | float  | Longitude of your location      |
| preferred\_type | string | Your preferred type of monument |

#### Available Monument Types

* Hindu Temple
* Buddhist Temple
* Historical Monument
* Garden
* Historical Site
* Museum
* Park
* Cave

#### Example Request

```bash
curl -X POST "http://localhost:8000/getRecommendations" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "latitude=27.7104&longitude=85.3487&preferred_type=Hindu Temple"
```

#### Response

```json
[
  {
    "id": 1,
    "name": "Pashupatinath Temple",
    "latitude": 27.7104,
    "longitude": 85.3487,
    "type": "Hindu Temple",
    "popularity": 0.95,
    "indoor": false,
    "description": "Ancient Hindu temple dedicated to Lord Shiva located on the banks of the Bagmati River.",
    "location": "Kathmandu, Nepal"
  }
]
```

### Say Hello

```
GET /say_hello
```

A simple endpoint to test if the API is running.

#### Response

```json
{
  "message": "Hello World"
}
```
