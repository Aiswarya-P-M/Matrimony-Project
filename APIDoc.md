# **API Documentation**

This project mainly consists of 8 apps and 47 api endpoints.

1. User app - 
2. UserProfile app - 
3. Preference app - 
4. Matching app - 
5. Message app -
6. Notification app -
7. Subscription app -
8. Commonmatching app -


# API Endpoints of User app

## 1. Create New User

* `URL`: http://127.0.0.1:8000/users/

* `Method` : POST

* `Description`: Creates a new user with fields like username,password,email,first_name,last_name,phone_number and role.

* `Content-type`:
  
         Content-Type: application/json

* `Body Parameters`:

# CustomUser Model Fields

| Field Name          | Data Type              | Constraints                                   | Relationship                          | Description                                           |
|----------------------|------------------------|----------------------------------------------|---------------------------------------|-------------------------------------------------------|
| `user_id`           | `AutoField`           | Primary Key                                  | -                                     | Unique identifier for each user.                     |
| `username`          | `CharField`           | Max Length: 50, Unique                      | -                                     | The unique username for the user.                    |
| `password`          | `CharField`           | Max Length: 50                              | -                                     | Password for the user (hashed before saving).         |
| `email`             | `EmailField`          | Unique                                      | -                                     | Email address of the user, must be unique.            |
| `phone_number`      | `PhoneNumberField`    | Unique, Nullable, Blank                     | -                                     | Optional phone number, must be unique if provided.    |
| `first_name`        | `CharField`           | Max Length: 50                              | -                                     | The first name of the user.                           |
| `last_name`         | `CharField`           | Max Length: 50                              | -                                     | The last name of the user.                            |
| `joined_date`       | `DateField`           | Auto Now Add                                | -                                     | The date the user joined the platform.                |
| `last_login`        | `DateField`           | Auto Now                                    | -                                     | The date of the user's last login.                    |
| `created_on`        | `DateField`           | Auto Now Add                                | -                                     | The timestamp when the record was created.            |
| `updated_on`        | `DateField`           | Auto Now                                    | -                                     | The timestamp when the record was last updated.       |
| `is_active`         | `BooleanField`        | Default: True                               | -                                     | Indicates whether the user account is active.         |
| `subscription_plan` | `ForeignKey`          | Nullable, Blank                             | `Subscription` (DO_NOTHING)           | Links the user to a subscription plan, if any.                                      | -                             |
| `is_staff`          | `BooleanField`        | Default: False                              | -                                     | Indicates if the user is a staff member.              |
| `is_admin`          | `BooleanField`        | Default: False                              | -                                     | Indicates if the user is an admin.                    |
| `role`              | `CharField`           | Max Length: 50, Choices: [admin, user, suspended], Default: user | -               | The role of the user: Admin, Normal User, or Suspended. |




### Example Request

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "username":"syam",
    "password":"syam1234",
    "email":"syam@gmail.com",
    "first_name":"syam",
    "last_name":"S",
    "phone_number":"+919023459789",
    "is_active":true,
    "role":"user"
}
```
### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "message": "User Created Successfully"
}
```

### Other Responses
Here are the possible response messages that could occur while creating a user based on the constraints in your model:


### 1. **Duplicate Username**
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Username already exists."
}
```

### 2. **Duplicate Email**
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Email already exists."
}
```

### 3. **Duplicate Phone Number**
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Phone number already exists."
}
```

### 4. **Invalid Email Format**
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Enter a valid email address."
}
```

### 5. **Invalid Phone Number Format**
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Enter a valid phone number."
}
```

### 6. **Missing Required Fields**
If required fields like `username`, `password`, `email`, etc., are missing:
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "The following fields are required: [field_name]."
}
```

### 7. **Password Validation Failure**
If you have custom password validation rules and the password does not meet them:
**HTTP Status:** `400 BAD REQUEST`
```json
{
    "error": "Password must meet the required complexity."
}
```



### Messages

1. **Duplicate Username**
```json
{
    "username": [
        "A user with this username already exists."
    ]
}
```

2. **Duplicate Email**
```json
{
    "email": [
        "A user with this email already exists."
    ]
}
```

3. **Duplicate Phone Number**
```json
{
    "phone_number": [
        "A user with this phone number already exists."
    ]
}
```

4. **Invalid Email**
```json
{
    "email": [
        "Enter a valid email address."
    ]
}
```

5. **Invalid Phone Number**
```json
{
    "phone_number": [
        "Enter a valid phone number."
    ]
}
```

6. **Password Too Weak**
```json
{
    "password": [
        "This password is too short. It must contain at least 8 characters."
    ]
}
```

7. **Role Invalid**
```json
{
    "role": [
        "Select a valid choice. That choice is not one of the available options."
    ]
}
```

8. **Required Fields Missing**
```json
{
    "first_name": [
        "This field is required."
    ]
}
```

9. **Subscription Plan Not Found**
```json
{
    "subscription_plan": [
        "The selected subscription plan does not exist."
    ]
}
```

---

## 2. User Login

* `URL`: http://127.0.0.1:8000/users/login/

* `Method` : POST

* `Description`: It allows users to authenticate by providing their credentials (typically a username and password) and generates an authentication token for subsequent requests.

* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
POST /login HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "username":"syam",
    "password":"syam1234"
}

```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "token": "cc6d722db4dd95d7830957951bd8666153eba1c1"
}
```

### Other Responses
Here are the possible response messages that could occur while creating a user based on the constraints in your model:


Here are additional example responses that your login API could return:



### 1. `HTTP Status: 401 Unauthorized`  
**Description:** The provided credentials are invalid.  

**Response:**
```json
{
    "error": "Invalid credenials."
}
```



### 2. `HTTP Status: 403 Forbidden`  
**Description:** The user's account is inactive or suspended (e.g., `is_active` is set to `False`).  

**Response:**
```json
{
    "error": "Your account is inactive. Please contact support."
}
```



### 3. `HTTP Status: 400 Bad Request`  
**Description:** The request payload is incomplete, such as missing required fields like `username` or `password`.  

**Response:**
```json
{
    "error": "Username and password are required."
}
```

### 4. `HTTP Status: 500 Internal Server Error`  
**Description:** An unexpected error occurred on the server during the login process.  

**Response:**
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```


### Messages

Here are the messages related to login:

---

1. **Invalid Credentials**
     
```json
{
    "non_field_errors": [
        "Invalid credentials."
    ]
}
```

2. **Inactive Account**  
```json
{
    "is_active": [
        "Your account is inactive."
    ]
}
```



3. **Missing Username**  
```json
{
    "username": [
        "This field is required."
    ]
}
```

4. **Missing Password**  
```json
{
    "password": [
        "This field is required."
    ]
}
```

---
## 3. User Logout

* `URL`: http://127.0.0.1:8000/users/logout/

* `Method` : POST

* `Description`: Logs out the user by invalidating the provided token.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
POST /logout HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token cc6d722db4dd95d7830957951bd8666153eba1c1"
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "message": "Logout Successfully"
}
```

### Other Responses
Here are the possible response messages that could occur while creating a user based on the constraints in your model:


Here are additional possible responses for the logout API:

---

### 1. **HTTP Status: 400 Bad Request**  
**Description:** The `Authorization` header is missing in the request.  
```json
{
    "error": "Authentication credentials  is not provided."
}
```


### 2. **HTTP Status: 401 Unauthorized**  
**Description:** The token provided in the `Authorization` header is invalid or expired.  
```json
{
    "error": "Invalid or expired token."
}
```

### 4. **HTTP Status: 405 Method Not Allowed**  
**Description:** A request method other than `POST` was used for logout.  
```json
{
    "error": "Method not allowed. Use POST for logout."
}
```

### 5. **HTTP Status: 500 Internal Server Error**  
**Description:** An unexpected error occurred on the server during the logout process.  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```

### Messages

Here are the messages for the logout API:


1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

2. **Invalid or Expired Token**  
```json
{
    "error": "Invalid or expired token."
}
```


3. **Method Not Allowed**  
```json
{
    "error": "Method not allowed. Use POST for logout."
}
```

---

## 4. Get user details by id

* `URL`: http://127.0.0.1:8000/users/byId/

* `Method` : GET

* `Description`: Retrieve user details.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
POST /byId HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 94be0a7e284780b9ef4e65f38ebdcb77c375f826"
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "user_id": 28,
    "date_joined": "2024-11-19T16:02:30.840817Z",
    "username": "syam",
    "password": "pbkdf2_sha256$870000$neYWVgwtycqoHBrf45Oe5D$TrAVCo0036jm8q6DVJH/gmHAMgVzUHa5reG4BfkKv2g=",
    "email": "syam@gmail.com",
    "phone_number": "+919023459789",
    "first_name": "syam",
    "last_name": "S",
    "joined_date": "2024-11-19",
    "last_login": "2024-11-19",
    "created_on": "2024-11-19",
    "updated_on": "2024-11-19",
    "is_active": true,
    "is_superuser": false,
    "is_staff": false,
    "is_admin": false,
    "role": "user",
    "subscription_plan": null,
    "groups": [],
    "user_permissions": []
}
```

### Other Responses


### 1. **HTTP Status: 400 Bad Request**  
**Description:** The token is missing in the request.  
```json
{
    "error": "Authentication credentials were not provided."
}
```

---

### 2. **HTTP Status: 401 Unauthorized**  
**Description:** The token provided in the `Authorization` header is invalid or expired.  
```json
{
    "error": "Invalid or expired token."
}
```


### 3. **HTTP Status: 405 Method Not Allowed**  
**Description:** A request method other than `GET` was used for retrieval.  
```json
{
    "error": "Method not allowed. Use GET to retrieve user details."
}
```

---

### 4. **HTTP Status: 500 Internal Server Error**  
**Description:** An unexpected error occurred on the server while retrieving user details.  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```


### Messages

Here are the messages for the update details:


1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

2. **Invalid or Expired Token**  
```json
{
    "error": "Invalid or expired token."
}
```


3. **Method Not Allowed**  
```json
{
    "error": "Method not allowed. Use GET to retrieve user details."
}
```

4. **Internal Server Error**  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```
---

## 5. Update user Details

* `URL`: http://127.0.0.1:8000/users/byId/

* `Method` : PUT

* `Description`: Update user details.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
POST /byId HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 94be0a7e284780b9ef4e65f38ebdcb77c375f826"
}

```
`Request Paylod`
```
{
    "subscription_plan": 4
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "user_id": 28,
    "date_joined": "2024-11-19T16:02:30.840817Z",
    "username": "syam",
    "password": "pbkdf2_sha256$870000$neYWVgwtycqoHBrf45Oe5D$TrAVCo0036jm8q6DVJH/gmHAMgVzUHa5reG4BfkKv2g=",
    "email": "syam@gmail.com",
    "phone_number": "+919023459789",
    "first_name": "syam",
    "last_name": "S",
    "joined_date": "2024-11-19",
    "last_login": "2024-11-20",
    "created_on": "2024-11-19",
    "updated_on": "2024-11-20",
    "is_active": true,
    "is_superuser": false,
    "is_staff": false,
    "is_admin": false,
    "role": "user",
    "subscription_plan": 4,
    "groups": [],
    "user_permissions": []
}
```

### Other Responses


### 1. **HTTP Status: 400 Bad Request**  
**Description:** The token is missing in the request.  
```json
{
    "error": "Authentication credentials were not provided."
}
```

---

### 2. **HTTP Status: 401 Unauthorized**  
**Description:** The token provided in the `Authorization` header is invalid or expired.  
```json
{
    "error": "Invalid or expired token."
}
```


### 3. **HTTP Status: 405 Method Not Allowed**  
**Description:** A request method other than `PUT` was used for updation.  
```json
{
    "error": "Method not allowed. Use PUT to retrieve user details."
}
```

---

### 4. **HTTP Status: 500 Internal Server Error**  
**Description:** An unexpected error occurred on the server while updating user details.  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```


### Messages

Here are the messages for the update API:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

1. **Invalid or Expired Token**  
```json
{
    "error": "Invalid or expired token."
}
```

1. **Invalid Field Value**  
```json
{
    "subscription_plan": [
        "Incorrect type. Expected pk value, received str."
    ]
}
```

1. **Method Not Allowed**  
```json
{
    "error": "Method not allowed. Use PUT or PATCH to update user details."
}
```

1. **Internal Server Error**  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```
---

## 5. Inactivate user 

* `URL`: http://127.0.0.1:8000/users/deactivate/

* `Method` : PUT

* `Description`: Inactivate user.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
PATCH /deactivate HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 94be0a7e284780b9ef4e65f38ebdcb77c375f826"
}

```


### Example Reponse

1.` HTTP Status: 200 OK`

```
{
   "message":"User Syam deactivated successfully" 
}
```

### Other Responses


### 1. **HTTP Status: 400 Bad Request**  
**Description:** The token is missing in the request.  
```json
{
    "error": "Authentication credentials were not provided."
}
```

---

### 2. **HTTP Status: 401 Unauthorized**  
**Description:** The token provided in the `Authorization` header is invalid or expired.  
```json
{
    "error": "Invalid or expired token."
}
```


### 3. **HTTP Status: 405 Method Not Allowed**  
**Description:** A request method other than `PATCH` was used for updation.  
```json
{
    "error": "Method not allowed. Use PATCH to update user details."
}
```

---

### 4. **HTTP Status: 400 BAD REQUEST**  
**Description:** It occurs when the user is already deactivated.
```json
{
    "detail": "User inactive or deleted."
}
```


### Messages

Here are the messages for the deactivate API:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

1. **Invalid or Expired Token**  
```json
{
    "error": "Invalid or expired token."
}
```

1. **Inactive user**  
```json
{
    "detail": "User inactive or deleted."
}
```

1. **Method Not Allowed**  
```json
{
    "error": "Method not allowed. Use PATCH  to deactivate user data."
}
```

1. **Internal Server Error**  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```

---
## 6. Reset Password 

* `URL`: http://127.0.0.1:8000/users/reset/

* `Method` : PUT

* `Description`: Reset user password.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
PUT /reset HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token a27c624aa1d8970ad484a06db06d14b8215627df"
}

```
`Request Paylod`
```
{
    "username":"syam",
    "old_password":"syam1234",
    "new_password":"shyam123"
}
```

### Example Reponse

1.` HTTP Status: 200 OK`

```
{
    "message": "Password reset successfully."
}
```

### Other Responses


### 1. **Authentication Header Missing (400 Bad Request)**  
```json
{
    "error": "Authentication credentials were not provided."
}
```
### 2. **Invalid or Expired Token (401 Unauthorized)**  
```json
{
    "error": "Invalid or expired token."
}
```

### 3. **Password Validation Error (400 Bad Request)**  
```json
{
    "error": "Password must contain at least 8 characters, including letters, numbers, and special characters."
}
```

### 4. **Password Mismatch (400 Bad Request)**  
```json
{
    "error": "Old password is not correct"
}
```

### 5. **Permission Denied (403 Forbidden)**  
```json
{
    "error": "You do not have permission to reset this password."
}
```

### 6. **Method Not Allowed (405 Method Not Allowed)**  
```json
{
    "error": "Method not allowed. Use PUT to reset the password."
}
```

### 7. **Internal Server Error (500 Internal Server Error)**  
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```

### Messages

Here are the messages for the reset password API:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

1. **Invalid or Expired Token**  
```json
{
    "error": "Invalid or expired token."
}
```

1. **Password Mismatch**  
```json
{
    "detail": "Old password is not correct."
}
```

1. **Method Not Allowed**  
```json
{
    "error": "Method not allowed. Use PUT  to reset password."
}
```

1. **Permission Denied**  
```json

{"message":"You do not have permission to perform this action."}

```
---