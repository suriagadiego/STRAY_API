## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)

# Stray API: Deep Dive
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae ultricies eget, tempor sit amet lectus. Maecenas congue urna at lorem tincidunt laoreet. Donec eu velit pretium, scelerisque diam nec, consectetur lorem. In hac habitasse platea dictumst. Vivamus vestibulum sagittis laoreet.


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

## Get total Stray Fed
This API endpoint returns the total number of the strays fed by the whole organization.

**GET** &nbsp;&nbsp;&nbsp; `https://www.google.com`

### Response 200
```json
{
  "status_code": 200,
  "data": {
    "total_strays_fed": "125,089",
  }
}
```

## Get total Stray Fed by Company
This API endpoint returns the total number of the strays fed by your company.

**GET** &nbsp;&nbsp;&nbsp; `https://www.sample_link.com/{Company_UUID}/`

### Response 200
```json
{
  "status_code": 200,
  "data": {
    "total_strays_fed": "125,089",
  }
}
```