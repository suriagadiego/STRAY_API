## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)

# Stray API: Deep Dive
**Making a Difference for Strays, One API Call at a Time.**

The Stray API aims to address the issue of hunger among stray cats and dogs in the Philippines. Integrate this API with your website on every transaction. Doing so demonstrates your commitment to helping strays. However, feeding strays indiscriminately can have drawbacks. Therefore, we partner with charitable organizations to conduct these feeding programs efficiently and safely.

<br>

Access APIS on the cloud or local:
*django-server-production-1afa.up.railway.app/*
*http://127.0.0.1:8000/*

## Sign Up
This API endpoint allows companies to register for your service. Upon successful registration, a UUID is generated and assigned to the company for transactions and record-keeping.

**POST** &nbsp;&nbsp;&nbsp; `api_endpoint/signup/`

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

**POST** &nbsp;&nbsp;&nbsp; `api_endpoint/feed/{Company_UUID}`


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

**GET** &nbsp;&nbsp;&nbsp; `api_endpoint/total_strays_fed/`

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

**GET** &nbsp;&nbsp;&nbsp; `api_endpoint/total_stays_fed/{Company_UUID}/`

### Response 200
```json
{
  "status_code": 200,
  "data": {
    "total_strays_fed": "125,089",
  }
}
```
<br>
<br>

## Cloning the App
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/suriagadiego/stray_api.git 

2. Create a virtual environment (recommended) and activate it.

    ```bash
    pipenv shell
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Get env file from email <br>
*Or create your own database and own env file on the root of the project with these values*

    ```
    PGDATABASE=
    PGUSER=
    PGPASSWORD=
    PGHOST=
    PGPORT=
    ```

