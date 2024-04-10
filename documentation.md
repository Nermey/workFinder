# API Documentation

## Register Endpoint
### Description:
This endpoint is used to register a new user.

### Request:
- Method: POST
- URL: /register
- Body:
  - user: Data of the new user

### Response:
- Status Code 201: Success Register
- Status Code 401: User is already exist

## Login Endpoint
### Description:
This endpoint is used to authenticate a user.

### Request:
- Method: POST
- URL: /login
- Body:
  - user: Data for user login

### Response:
- Status Code 202: Authentication successfully
- Status Code 402: User is not exist
- Status Code 403: Incorrect email or password