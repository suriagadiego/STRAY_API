## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)

## Sign Up
This API endpoint allows companies to register for your service. Upon successful registration, a UUID is generated and assigned to the company for transactions and record-keeping.

**POST** &nbsp;&nbsp;&nbsp; `https://www.google.com`

### Request Body
| **Name**     | **Type** | **Description**                        |
|--------------|----------|----------------------------------------|
| Company Name | String   | Company or Entity Name                 |
| Description  | String   | Little detail of what the company does |

### Response 200
```json
{
  "status_code": 200,
  "data": {
    "company_name": "Emotive",
    "UUID": "0cbef9d3-4f16-4ee8-b485-c045dc8bb194",
  }
}
```

## Feed
This API endpoint allows companies to feed stray cats by entering the number of strays they want to feed.

**POST** &nbsp;&nbsp;&nbsp; `https://www.google.com`


### Request Body

| **Name** | **Type** | **Description**                    |
|----------|----------|------------------------------------|
| Count    | Integer  | Number of strays they want to feed |

### Response 200
```json
{
  "status_code": 200,
  "data": {
    "total_strays_fed": "25",
  }
}
```

