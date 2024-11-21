# **API Documentation**

This project mainly consists of 8 apps and 47 api endpoints.

1. User app - 11
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
    "role": "user",
    "subscription_plan": null,
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
    "role": "user",
    "subscription_plan": 4,
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

In the user app admin has some operations

## 1. List Users

* `URL`: http://127.0.0.1:8000/users/listusers/

* `Method` : GET

* `Description`: Retrieve user details.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
GET /listusers HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`

```
{
    "count": 5,
    "next": "http://127.0.0.1:8000/users/listusers/?page=2",
    "previous": null,
    "results": [
        {
            "user_id": 14,
            "username": "Isha",
            "email": "Isha@gmail.com",
            "phone_number": "+919023457890",
            "first_name": "Isha",
            "last_name": "S",
            "joined_date": "2024-11-15",
            "last_login": "2024-11-19",
            "subscription_plan": 3,
            "is_active": false,
            "role": "user"
        }
    ]
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

## 2. Deactivate Users

* `URL`: http://127.0.0.1:8000/users/deactivateuser/<int:user_id>

* `Method` : PATCH

* `Description`: Deactivate user.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
GET /deactivateuser/<int:user_id> HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`

```
{
    'message': User anagha deactivated successfully.'
}
```

### Other Responses


### 1. **Authentication Header Missing (400 Bad Request)**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

### 2. **Permission Denied (403 Forbidden)**  
```json
{
    "error": "You do not have permission to reset this password."
}
```

### 3. **User already deactivated (400 Bad Request)**  
```json
{
    "message": "User anagha is already deactivated."
}

```

### Messages

Here are the messages for deactivate user:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

2. **Permission Denied**  
```json
{
    "message":"You do not have permission to perform this action."
}

```
1. **User already deactivated**  
```json
{
    "message": "User anagha is already deactivated."
}

```
---

## 3. List of active Users

* `URL`: http://127.0.0.1:8000/users/activeusers/

* `Method` : GET

* `Description`: List of active users.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
GET /activeusers HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`

```
{
    "count": 3,
    "next": "http://127.0.0.1:8000/users/activeusers/?page=2",
    "previous": null,
    "results": [
        {
            "user_id": 15,
            "username": "Alen",
            "email": "Alen@gmail.com",
            "phone_number": "+919023459087",
            "first_name": "Alen",
            "last_name": "A",
            "joined_date": "2024-11-15",
            "last_login": "2024-11-15",
            "subscription_plan": null,
            "is_active": true,
            "role": "user"
        },
    ]
```

### Other Responses


### 1. **Authentication Header Missing (400 Bad Request)**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

### 2. **Permission Denied (403 Forbidden)**  
```json
{
    "error": "You do not have permission to reset this password."
}
```



### Messages

Here are the messages for listing the active users:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

2. **Permission Denied**  
```json
{
    "message":"You do not have permission to perform this action."
}

```

---

## 4. List of Inactive Users

* `URL`: http://127.0.0.1:8000/users/inactiveusers/

* `Method` : GET

* `Description`: List of inactive users.


* `Content-type`:
  
         Content-Type: application/json

### Example Request

```http
GET /inactiveusers HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`

```
[
    {
        "user_id": 14,
        "username": "Isha",
        "email": "Isha@gmail.com",
        "phone_number": "+919023457890",
        "first_name": "Isha",
        "last_name": "S",
        "joined_date": "2024-11-15",
        "last_login": "2024-11-19",
        "subscription_plan": 3,
        "is_active": false,
        "role": "user"
    },
    {
        "user_id": 32,
        "username": "anagha",
        "email": "anagha@gmail.com",
        "phone_number": "+919023459790",
        "first_name": "anagha",
        "last_name": "S",
        "joined_date": "2024-11-20",
        "last_login": "2024-11-20",
        "subscription_plan": null,
        "is_active": false,
        "role": "suspended"
    }
]
```

### Other Responses


### 1. **Authentication Header Missing (400 Bad Request)**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

### 2. **Permission Denied (403 Forbidden)**  
```json
{
    "error": "You do not have permission to reset this password."
}
```


### Messages

Here are the messages for listing the inactive users:
 

1. **Authentication Header Missing**  
```json
{
    "error": "Authentication credentials were not provided."
}
```

2. **Permission Denied**  
```json
{
    "message":"You do not have permission to perform this action."
}

```

---

# API Endpoints of userprofile app

## 1. Create User Profile

* `URL`:  http://127.0.0.1:8000/profile/

* `Method` : POST

* `Description`: Creates a  user profile with fields like user_id,gender,date_of_birth,Age, Height, Weight, Religion, Caste, Income, Profession, Education, Bio, Marital_status, Location,Language, profile_image.

* `Content-type`:
  
        Content-Type: multipart/form-data

* `Body Parameters`:


### `UserProfile` Model

| **Field Name**     | **Data Type**         | **Constraints**              | **Relationship**                              | **Description**                                                                 |
|---------------------|-----------------------|------------------------------|-----------------------------------------------|---------------------------------------------------------------------------------|
| `user_id`          | `ForeignKey`         | `null=True, blank=True`      | Foreign key to `CustomUser` (on `DO_NOTHING`) | Links profile to a specific user in the `CustomUser` model.                    |
| `Gender`           | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the user's gender.                                                      |
| `Date_of_Birth`    | `DateField`          | `null=True, blank=True`      | None                                        | Stores the user's date of birth.                                               |
| `Age`              | `IntegerField`       | `null=True, blank=True`      | None                                        | Stores the user's age.                                                         |
| `Height`           | `IntegerField`       | `null=True, blank=True`      | None                                        | Stores the user's height in centimeters.                                       |
| `Weight`           | `IntegerField`       | `null=True, blank=True`      | None                                        | Stores the user's weight in kilograms.                                         |
| `Religion`         | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the user's religion.                                                    |
| `Caste`            | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the user's caste.                                                       |
| `Income`           | `IntegerField`       | `null=True, blank=True`      | None                                        | Stores the user's annual income.                                               |
| `Profession`       | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the user's profession.                                                  |
| `Education`        | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the user's highest educational qualification.                           |
| `Bio`              | `CharField`          | `max_length=500, null=True, blank=True` | None                                        | Stores a brief bio or description of the user.                                 |
| `Marital_status`   | `CharField`          | `max_length=30, null=True, blank=True` | None                                        | Stores the user's marital status.                                              |
| `Location`         | `CharField`          | `max_length=200, null=True, blank=True` | None                                        | Stores the user's location address.                                            |
| `Language`         | `CharField`          | `max_length=50, null=True, blank=True` | None                                        | Stores the primary language(s) spoken by the user.                             |
| `Profile_img`      | `ImageField`         | `upload_to='profile_img'`    | None                                        | Stores the path to the user's profile image.                                   |
| `created_on`       | `DateTimeField`      | `auto_now_add=True`          | None                                        | Stores the timestamp when the profile was created.                             |
| `updated_on`       | `DateTimeField`      | `auto_now=True`              | None                                        | Stores the timestamp of the most recent update to the profile.                 |



### Example Request

```http
POST /profile HTTP/1.1
Host: api.example.com
Content-Type: multipart/form-data

---

### Form Data:
| **Key**           | **Value**               |
|--------------------|-------------------------|
| `user_id`         | 16                      |
| `Gender`          | Female                  |
| `Date_of_Birth`   | 2000-06-24              |
| `Age`             | 24                      |
| `Height`          | 168                     |
| `Weight`          | 50                      |
| `Religion`        | Hindu                   |
| `Caste`           | Brahmin                 |
| `Income`          | 40000                   |
| `Profession`      | Teacher                 |
| `Education`       | BCA                     |
| `Bio`             | Cricket lover           |
| `Marital_status`  | Single                  |
| `Location`        | Kozhikode               |
| `Language`        | Malayalam               |
| `Profile_img`     | (File) `pexels-steinportraits-1898555.jpg` |
```

---

### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "message": "Profile created successfully"
}
```

### Other Responses

Here are examples of possible responses for `UserProfile` creation:


### **1. Validation Error Response**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "message": "Validation failed",
    "errors": {
        "Gender": ["This field is required."],
        "Date_of_Birth": ["Invalid date format. Use YYYY-MM-DD."],
        "Profile_img": ["No file was submitted."]
    }
}
```

### **2. Duplicate Profile Error**

**HTTP Status:** `409 CONFLICT`

```json
{
    "message": "A profile already exists for this user.",
    "user_id": 16
}
```


### **4. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Validation Error**
```json
{
    "message": "Validation failed",
    "errors": {
        "Gender": ["This field is required."],
        "Date_of_Birth": ["Invalid date format. Use YYYY-MM-DD."],
        "Profile_img": ["No file was submitted."]
    }
}
```
2. **Profile already exists**
```json
{
    "message": "A profile already exists for this user.",
    "user_id": 16
}
```
---

## 2. Viewing Profile Details

* `URL`:  http://127.0.0.1:8000/profile/

* `Method` : GET

* `Description`: Retrieve profile details

* `Content-type`:
  
        Content-Type: application/json




### Example Request
```json
```http
GET /profile HTTP/1.1
Host: api.example.com
Content-Type:  application/json
{
    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 9,
            "Profile_img_url": "/media/profile_img/pexels-sulimansallehi-1704488_phFG3Tf.jpg",
            "Gender": "Female",
            "Date_of_Birth": "2000-06-24",
            "Age": 25,
            "Height": 167,
            "Weight": 52,
            "Religion": "Christian",
            "Caste": "Syrian Catholic",
            "Income": 30000,
            "Profession": "Teacher",
            "Education": "MCA",
            "Bio": "Dancer",
            "Marital_status": "Single",
            "Location": "Kochi",
            "Language": "Malayalam",
            "Profile_img": "/media/profile_img/pexels-sulimansallehi-1704488_phFG3Tf.jpg",
            "created_on": "2024-11-15T06:17:45.067790Z",
            "updated_on": "2024-11-15T08:31:16.052377Z",
            "user_id": 14
        },
    ]
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Authentication credentials not provided**
```json
{
    "message": "Authentication credentials were not provided."
}
```
2. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```


## 2. Viewing Profile Details by id

* `URL`:  http://127.0.0.1:8000/profile/byid/

* `Method` : GET

* `Description`: Retrieve profile details by id.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /profile/byid/ HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 0340b35216c3dcb68f0ebd023b32f2e98d389b66"
}

```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "id": 12,
    "Profile_img_url": "/media/profile_img/pexels-sulimansallehi-1704488_fc4Nudw.jpg",
    "Gender": "Female",
    "Date_of_Birth": "2000-06-24",
    "Age": 24,
    "Height": 168,
    "Weight": 50,
    "Religion": "Hindu",
    "Caste": "Brahmin",
    "Income": 40000,
    "Profession": "Teacher",
    "Education": "BCA",
    "Bio": "Cricket Lover",
    "Marital_status": "Single",
    "Location": "Kozhikode",
    "Language": "Malayalam",
    "Profile_img": "/media/profile_img/pexels-sulimansallehi-1704488_fc4Nudw.jpg",
    "created_on": "2024-11-20T15:59:16.305639Z",
    "updated_on": "2024-11-20T15:59:16.305639Z",
    "user_id": 33
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Invalid Token **

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "detail": "Invalid token."
}
```

### Messages

1. **Authentication credentials not provided**
```json
{
    "message": "Authentication credentials were not provided."
}
```
---

## 2. Update Profile Details by id

* `URL`:  http://127.0.0.1:8000/profile/byid/

* `Method` : PUT

* `Description`: Update profile details by id.

* `Content-type`:
  
        Content-Type: multipart/form-data



### Example Request
```json
```http
PUT /profile/byid/ HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 0340b35216c3dcb68f0ebd023b32f2e98d389b66"
}

```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "Location":"Kochi"
}
```

### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Validation Problem **

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "Location": [
        "Invalid location. Valid values are: Thiruvananthapuram, Kochi, Kozhikode, Kottayam, Alappuzha, Malappuram, Thrissur, Palakkad, Ernakulam, Idukki, Kannur, Wayanad, Pathanamthitta, Rajasthan India, Uttarakhand India, Himachal Pradhesh India, Andhra Pradhesh India, Arunachal Pradhesh India, Karnataka India, TamilNadu India, Punjab India, Assam India, Bihar India, Maharashtra India, Gujarat India, Chhattisgarh India, Goa India, Haryana India, Jammu and Kashmir India, Jharkhand India, Manipur India, Madhya Pradesh India, Meghalaya India, Mizoram India, Nagaland India, Odisha India, Sikkim India, Tripura India, Telangana India, West Bengal India, Uttar Pradesh India"
    ]
}
```

### Messages

1. **Authentication credentials not provided**
```json
{
    "message": "Authentication credentials were not provided."
}
```
---

# API Endpoints of Preference app

## 1. Create preference

* `URL`:  http://127.0.0.1:8000/preference/

* `Method` : POST

* `Description`: Creates a  user preference with fields like Age,Gender, Height, Weight, Religion, Caste, Income, Profession, Education,  Marital_status, Location,Language.

* `Content-type`:
  
        Content-Type : application/json

* `Body Parameters`:


### `Preference` Model

Here’s the `Preference` model represented in Markdown table format:

| **Field Name**     | **Data Type**      | **Constraints**                     | **Relationship**                    | **Description**                                         |
|---------------------|--------------------|--------------------------------------|--------------------------------------|---------------------------------------------------------|
| `user_id`          | OneToOneField      | `null=True`, `blank=True`            | ForeignKey to `CustomUser`           | Links each preference to a single user.                 |
| `Age`              | JSONField          | `null=True`, `blank=True`            | None                                 | Stores a range [min, max] for the preferred age.         |
| `Height`           | JSONField          | `null=True`, `blank=True`            | None                                 | Stores a range [min, max] for the preferred height.      |
| `Weight`           | JSONField          | `null=True`, `blank=True`            | None                                 | Stores a range [min, max] for the preferred weight.      |
| `Income`           | JSONField          | `null=True`, `blank=True`            | None                                 | Stores a range [min, max] for the preferred income.      |
| `Profession`       | JSONField          | `null=True`, `blank=True`            | None                                 | List of preferred professions.                          |
| `Education`        | JSONField          | `null=True`, `blank=True`            | None                                 | List of preferred education levels.                     |
| `Location`         | JSONField          | `null=True`, `blank=True`            | None                                 | List of preferred locations.                            |
| `Language`         | JSONField          | `null=True`, `blank=True`            | None                                 | List of preferred languages.                            |
| `Caste`            | JSONField          | `null=True`, `blank=True`            | None                                 | Single-value preferred caste.                           |
| `Religion`         | JSONField          | `null=True`, `blank=True`            | None                                 | Single-value preferred religion.                        |
| `Gender`           | CharField          | `max_length=50`, `null=True`, `blank=True` | None                                 | Preferred gender of the user.                           |
| `Marital_status`   | CharField          | `max_length=50`, `null=True`, `blank=True` | None                                 | Preferred marital status of the user.                   |
| `created_on`       | DateTimeField      | Auto-generated                       | None                                 | Timestamp for when the preference was created.          |
| `updated_on`       | DateTimeField      | Auto-updated                         | None                                 | Timestamp for when the preference was last updated.     |



### Example Request

```http
POST /preference HTTP/1.1
Host: api.example.com
Content-Type: application/json


---
{
   "user_id":33,
  "Age": [27, 29],               
  "Height": [170, 185],          
  "Weight": [50, 70],            
  "Income": [50000, 100000],
  "Profession": ["Software Engineer","Teacher"], of preferred professions
  "Education": ["MCA","Master's Degree","Engineering Degree"],  
  "Location": ["Thiruvananthapuram","Kochi","Kozhikode"], 
  "Language": ["English","Malayalam"],    

  "Caste": ["Brahmin","Kshatriya"],
  "Religion": ["Hindu"],
  "Gender": "Male",
  "Marital_status": "Single"
}

```

---

### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "message": "Preference added successfully"
}
```

### Other Responses


### **1. Validation Error Response**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "Profession": [
        "Invalid profession(s). Valid values are: Software Engineer, Doctor, Teacher, Engineer, Lawyer, Architect, Nurse, Scientist, Artist, Chef, Mechanic, Accountant, Business Analyst, HR Manager, Marketing Manager, Consultant, Pharmacist, Writer, Photographer, Banker, Social Worker, Police Officer, Graphic Designer, Financial Analyst, Civil Engineer, IAS Officer, IPS Officer, Defense Personnel"
    ],
}
```

### **2. Preference with the user already exists.**

**HTTP Status:** `409 CONFLICT`

```json
{
    "user_id": [
        "preference with this user id already exists."
    ]
}
```


### **3. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **4. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Validation Error**
```json
{
    "Profession": [
        "Invalid profession(s). Valid values are: Software Engineer, Doctor, Teacher, Engineer, Lawyer, Architect, Nurse, Scientist, Artist, Chef, Mechanic, Accountant, Business Analyst, HR Manager, Marketing Manager, Consultant, Pharmacist, Writer, Photographer, Banker, Social Worker, Police Officer, Graphic Designer, Financial Analyst, Civil Engineer, IAS Officer, IPS Officer, Defense Personnel"
    ],
}
```
2. **Preference already exists**
```json
{
    "user_id": [
        "preference with this user id already exists."
    ]
}
```
---

## 2. Viewing Preference Details by Id

* `URL`:  http://127.0.0.1:8000/preference/preferencebyId/

* `Method` : GET

* `Description`: Retrieve preference details by id
* 
* `Content-type`:
  
        Content-Type: application/json




### Example Request
```json
```http
GET /preferencebyId HTTP/1.1
Host: api.example.com
Content-Type:  application/json
{
    {
    "Authorization": "Token 0340b35216c3dcb68f0ebd023b32f2e98d389b66"
}
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "id": 12,
    "Age": [
        27,
        29
    ],
    "Height": [
        170,
        185
    ],
    "Weight": [
        50,
        70
    ],
    "Income": [
        50000,
        100000
    ],
    "Profession": [
        "Software Engineer",
        "Teacher"
    ],
    "Education": [
        "MCA",
        "Master's Degree",
        "Engineering Degree"
    ],
    "Location": [
        "Thiruvananthapuram",
        "Kochi",
        "Kozhikode"
    ],
    "Language": [
        "English",
        "Malayalam"
    ],
    "Caste": [
        "Brahmin",
        "Kshatriya"
    ],
    "Religion": [
        "Hindu"
    ],
    "Gender": "Male",
    "Marital_status": "Single",
    "created_on": "2024-11-20T17:20:32.754519Z",
    "updated_on": "2024-11-20T17:20:55.411122Z",
    "user_id": 33
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Invalid Token**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "message":"Invalid Token"
}
```

### Messages

1. **Authentication credentials not provided**
```json
{
    "message": "Authentication credentials were not provided."
}
```
2. **Fo**
```json
{
    "message": "You do not have permission to perform this action."
}
```


## 3. Updating Preference Details by id

* `URL`:  http://127.0.0.1:8000/preference/preferencebyId/

* `Method` : PUT

* `Description`: Update profile details by id.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /profile/byid/ HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 0340b35216c3dcb68f0ebd023b32f2e98d389b66"
}

```
`Request Paylod`
```json
{
"Profession": ["Software Engineer","Teacher","Police Officer"], 
"Language": ["English","Malayalam"]
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "id": 12,
    "Age": [
        27,
        29
    ],
    "Height": [
        170,
        185
    ],
    "Weight": [
        50,
        70
    ],
    "Income": [
        50000,
        100000
    ],
    "Profession": [
        "Software Engineer",
        "Teacher",
        "Police Officer"
    ],
    "Education": [
        "MCA",
        "Master's Degree",
        "Engineering Degree"
    ],
    "Location": [
        "Thiruvananthapuram",
        "Kochi",
        "Kozhikode"
    ],
    "Language": [
        "English",
        "Malayalam"
    ],
    "Caste": [
        "Brahmin",
        "Kshatriya"
    ],
    "Religion": [
        "Hindu"
    ],
    "Gender": "Male",
    "Marital_status": "Single",
    "created_on": "2024-11-20T17:20:32.754519Z",
    "updated_on": "2024-11-20T17:36:57.620001Z",
    "user_id": 33
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Validation Error Response**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "Profession": [
        "Invalid profession(s). Valid values are: Software Engineer, Doctor, Teacher, Engineer, Lawyer, Architect, Nurse, Scientist, Artist, Chef, Mechanic, Accountant, Business Analyst, HR Manager, Marketing Manager, Consultant, Pharmacist, Writer, Photographer, Banker, Social Worker, Police Officer, Graphic Designer, Financial Analyst, Civil Engineer, IAS Officer, IPS Officer, Defense Personnel"
    ],
}
```

### Messages

1. **Validation Error**
```json
```json
{
    "Profession": [
        "Invalid profession(s). Valid values are: Software Engineer, Doctor, Teacher, Engineer, Lawyer, Architect, Nurse, Scientist, Artist, Chef, Mechanic, Accountant, Business Analyst, HR Manager, Marketing Manager, Consultant, Pharmacist, Writer, Photographer, Banker, Social Worker, Police Officer, Graphic Designer, Financial Analyst, Civil Engineer, IAS Officer, IPS Officer, Defense Personnel"
    ],
}
```

---



# API Endpoints of Matching app

## 1. Find matching between two users

* `URL`:  http://localhost:8000/matching/find-match/

* `Method` : GET

* `Description`: Finds the match between 2 users.
* `Content-type`:
  
        Content-Type : application/json

* `Body Parameters`:


### `Matching` Model



Here’s the `Matching` model represented in Markdown table format:

| **Field Name**   | **Data Type**   | **Constraints**                                    | **Relationship**                      | **Description**                                            |
|-------------------|-----------------|---------------------------------------------------|----------------------------------------|------------------------------------------------------------|
| `user1`          | ForeignKey      | `on_delete=models.DO_NOTHING`                     | ForeignKey to `CustomUser`             | Refers to the first user in the match.                     |
| `user2`          | ForeignKey      | `on_delete=models.DO_NOTHING`                     | ForeignKey to `CustomUser`             | Refers to the second user in the match.                    |
| `status`         | CharField       | `max_length=10`, choices: `accepted`, `pending`, `rejected`, default=`pending` | None | Indicates the current status of the match (accepted, pending, or rejected). |
| `match_score`    | FloatField      | `null=True`, `blank=True`                         | None                                   | Stores the percentage score of the match between users.    |
| `created_on`     | DateTimeField   | Auto-generated                                    | None                                   | Timestamp for when the match was created.                  |
| `updated_on`     | DateTimeField   | Auto-updated                                      | None                                   | Timestamp for when the match was last updated.             |


### Example Request

```http
GET /matching/find-match/ HTTP/1.1
Host: api.example.com
Content-Type: application/json


{
    {
    "Authorization": "Token 03c41df36a2a5b92d4655c5fcfc53149ff56db46"
}
}
```
`Request Payload`
```json
{
    "user1_id":15,
    "user2_id":33
}
```

---

### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "user1": "Alen",
    "user2": "geetha",
    "match_score": 75.83333333333333,
    "status": "accepted"
}
```

### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```

---

## 2. Find all the matching for a specific user

* `URL`:  http://localhost:8000/matching/find-all-matches/

* `Method` : GET

* `Description`: Find all the matching for a specific user
* 
* `Content-type`:
  
        Content-Type: application/json




### Example Request
```json
```http
GET /preferencebyId HTTP/1.1
Host: api.example.com
Content-Type:  application/json
{
    {
    "Authorization": "Token 03c41df36a2a5b92d4655c5fcfc53149ff56db46"
}
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
[
    {
        "user1_id": 15,
        "user2_id": 14,
        "match_score": 88.33333333333333,
        "status": "accepted"
    },
    {
        "user1_id": 15,
        "user2_id": 33,
        "match_score": 75.83333333333333,
        "status": "accepted"
    },
    {
        "user1_id": 15,
        "user2_id": 16,
        "match_score": 57.49999999999999,
        "status": "pending"
    }
]
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **5. Invalid Token**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "message":"Invalid Token"
}
```

### Messages

1. **Authentication credentials not provided**
```json
{
    "message": "Authentication credentials were not provided."
}
```
---

# API Endpoints of Common Matching app

## 1. Create common matching table

* `URL`:  http://127.0.0.1:8000/commonmatch/

* `Method` : POST

* `Description`: Creates commonmatching table with fields with type_id and type.

* `Content-type`:
  
        Content-Type : application/json




### `CommonMatching` Model


# CommonMatchingTable

| **Field Name**   | **Data Type**      | **Constraints**                                 | **Relationship** | **Description**                                                                 |
|-------------------|--------------------|-------------------------------------------------|-------------------|---------------------------------------------------------------------------------|
| `type_id`         | `AutoField`       | Primary Key                                     | None              | A unique identifier for each type entry.                                        |
| `type`            | `CharField`       | Max length 20, unique, and restricted to predefined choices: 'gender', 'caste', 'religion', 'profession', 'education', 'location', 'language', 'marital_status'. | None | Represents the type of matching category (e.g., Gender, Caste, etc.).          |
| `created_on`      | `DateTimeField`   | Auto-generated at record creation              | None              | Timestamp indicating when the record was created.                               |
| `updated_on`      | `DateTimeField`   | Auto-updated at record modification            | None              | Timestamp indicating when the record was last updated.                          |

### Example Request

```http
POST /commonmatch HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}
}
```
`Request Payload`
```json
{
    "type":"marital_status"
}
```

### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "message": "Subscription added Successfully"
}
```

### Other Responses


### **1. Validation Error Response**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "plan_type": [
        "\"gold\" is not a valid choice."
    ]
}
```

### **2. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Validation Error**
```json
{
    "plan_type": [
        "\"gold\" is not a valid choice."
    ]
}
```


---

## 2. List Subscription

* `URL`:  http://127.0.0.1:8000/subscription/list

* `Method` : GET

* `Description`: Retrieve subscription details.
* 
* `Content-type`:
  
        Content-Type: application/json




### Example Request
```json
```http
GET /subscription/list HTTP/1.1
Host: api.example.com
Content-Type:  application/json
{
    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "subscription_id": 2,
            "plan_type": "basic",
            "start_date": "2024-06-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:12:55.650109Z",
            "updated_on": "2024-11-14T06:39:30.039128Z"
        },
        {
            "subscription_id": 3,
            "plan_type": "premium",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:13:25.451489Z",
            "updated_on": "2024-11-14T06:39:08.660198Z"
        },
        {
            "subscription_id": 4,
            "plan_type": "platinum",
            "start_date": "2024-01-01",
            "end_date": "2025-01-31",
            "status": "active",
            "created_on": "2024-11-14T05:14:36.041864Z",
            "updated_on": "2024-11-14T06:38:43.817882Z"
        }
    ]
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```


### Messages

1. **Forbidden action**
```json
{
    "message": "You do not have permission to perform this action."
}
```


## 3. Retrieve Subscription Details by id

* `URL`:  http://127.0.0.1:8000/subscription/list/<int:subscription_id>

* `Method` : GET

* `Description`: Retrieve Subscription Details by id.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /profile/byid/ HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "subscription_id": 4,
    "plan_type": "platinum",
    "start_date": "2024-01-01",
    "end_date": "2025-01-31",
    "status": "active",
    "created_on": "2024-11-14T05:14:36.041864Z",
    "updated_on": "2024-11-14T06:38:43.817882Z"
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```
## 3. Update Subscription Details 

* `URL`:  http://127.0.0.1:8000/subscription/update/<int:subscription_id>

* `Method` : PUT

* `Description`: Update Subscription Details.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /update/<int:subscription_id> HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```
```Request Payload```
```json
{
            "subscription_id": 2,
            "plan_type": "basic",
            "start_date": "2024-06-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:14:36.041864Z",
            "updated_on": "2024-11-14T05:14:36.041864Z"
        }
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "subscription_id": 2,
    "plan_type": "basic",
    "start_date": "2024-06-01",
    "end_date": "2024-12-31",
    "status": "active",
    "created_on": "2024-11-14T05:12:55.650109Z",
    "updated_on": "2024-11-20T18:21:03.517428Z"
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```

## 3. Delete Subscription Details 

* `URL`:  http://127.0.0.1:8000/subscription/delete/<int:subscription_id>

* `Method` : PUT

* `Description`: Delete Subscription Data.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /delete/<int:subscription_id> HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`
```
{
   "message":"Subscription plan deleted successfully"
}
```


### Other Responses

### **1. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```
### **1. No valid Subscription**

**HTTP Status:** `404 NOT FOUND`

```json
{
    "detail": "No Subscription matches the given query."
}
```


### Messages

1. **No valid Subscription**
```json
{
    "detail": "No Subscription matches the given query."
}
```
---


# API Endpoints of Subscription app

## 1. Create subscription

* `URL`:  http://127.0.0.1:8000/subscription/

* `Method` : POST

* `Description`: Creates subscription with fields plan_type,start_date,end_date and status.

* `Content-type`:
  
        Content-Type : application/json




### `Subscription` Model

Here’s the `Subscription` model represented in Markdown table format:

| **Field Name**       | **Data Type**  | **Constraints**                                    | **Relationship** | **Description**                                             |
|-----------------------|---------------|---------------------------------------------------|------------------|-------------------------------------------------------------|
| `subscription_id`    | AutoField      | Primary key                                       | None             | Unique identifier for each subscription.                   |
| `plan_type`          | CharField      | `max_length=10`, choices: `basic`, `premium`, `platinum` | None      | Specifies the type of subscription plan.                   |
| `start_date`         | DateField      | Required                                          | None             | The date when the subscription starts.                     |
| `end_date`           | DateField      | Required                                          | None             | The date when the subscription ends.                       |
| `status`             | CharField      | `max_length=10`, choices: `active`, `expired`     | None             | Indicates the current status of the subscription.          |
| `created_on`         | DateTimeField  | Auto-generated                                    | None             | Timestamp for when the subscription was created.           |
| `updated_on`         | DateTimeField  | Auto-updated                                      | None             | Timestamp for when the subscription was last updated.      |


### Example Request

```http
POST /subscription HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    {
    "Authorization": "Token 03c41df36a2a5b92d4655c5fcfc53149ff56db46"
}
}

`Request Payload`
```json
{
    "plan_type": "platinum",
    "start_date": "2024-01-01",
    "end_date": "2025-01-31",
    "status": "active"
}
```

### Example Reponse

1.` HTTP Status: 201 CREATED`
```
{
    "message": "Subscription added Successfully"
}
```

### Other Responses


### **1. Validation Error Response**

**HTTP Status:** `400 BAD REQUEST`

```json
{
    "plan_type": [
        "\"gold\" is not a valid choice."
    ]
}
```

### **2. Forbidden Action (No Permissions)**

**HTTP Status:** `403 FORBIDDEN`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Validation Error**
```json
{
    "plan_type": [
        "\"gold\" is not a valid choice."
    ]
}
```


---

## 2. List Subscription

* `URL`:  http://127.0.0.1:8000/subscription/list

* `Method` : GET

* `Description`: Retrieve subscription details.
* 
* `Content-type`:
  
        Content-Type: application/json




### Example Request
```json
```http
GET /subscription/list HTTP/1.1
Host: api.example.com
Content-Type:  application/json
{
    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}
}
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "subscription_id": 2,
            "plan_type": "basic",
            "start_date": "2024-06-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:12:55.650109Z",
            "updated_on": "2024-11-14T06:39:30.039128Z"
        },
        {
            "subscription_id": 3,
            "plan_type": "premium",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:13:25.451489Z",
            "updated_on": "2024-11-14T06:39:08.660198Z"
        },
        {
            "subscription_id": 4,
            "plan_type": "platinum",
            "start_date": "2024-01-01",
            "end_date": "2025-01-31",
            "status": "active",
            "created_on": "2024-11-14T05:14:36.041864Z",
            "updated_on": "2024-11-14T06:38:43.817882Z"
        }
    ]
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```


### Messages

1. **Forbidden action**
```json
{
    "message": "You do not have permission to perform this action."
}
```


## 3. Retrieve Subscription Details by id

* `URL`:  http://127.0.0.1:8000/subscription/list/<int:subscription_id>

* `Method` : GET

* `Description`: Retrieve Subscription Details by id.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /profile/byid/ HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "subscription_id": 4,
    "plan_type": "platinum",
    "start_date": "2024-01-01",
    "end_date": "2025-01-31",
    "status": "active",
    "created_on": "2024-11-14T05:14:36.041864Z",
    "updated_on": "2024-11-14T06:38:43.817882Z"
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```
## 3. Update Subscription Details 

* `URL`:  http://127.0.0.1:8000/subscription/update/<int:subscription_id>

* `Method` : PUT

* `Description`: Update Subscription Details.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /update/<int:subscription_id> HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```
```Request Payload```
```json
{
            "subscription_id": 2,
            "plan_type": "basic",
            "start_date": "2024-06-01",
            "end_date": "2024-12-31",
            "status": "active",
            "created_on": "2024-11-14T05:14:36.041864Z",
            "updated_on": "2024-11-14T05:14:36.041864Z"
        }
```
### Example Reponse

1.` HTTP Status: 200 OK`
```
{
    "subscription_id": 2,
    "plan_type": "basic",
    "start_date": "2024-06-01",
    "end_date": "2024-12-31",
    "status": "active",
    "created_on": "2024-11-14T05:12:55.650109Z",
    "updated_on": "2024-11-20T18:21:03.517428Z"
}
```


### Other Responses

### **1. Unauthorized Request**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "Authentication credentials were not provided."
}
```

### **2. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```

### Messages

1. **Forbidden Action**
```json
{
    "message": "You do not have permission to perform this action."
}
```

## 3. Delete Subscription Details 

* `URL`:  http://127.0.0.1:8000/subscription/delete/<int:subscription_id>

* `Method` : PUT

* `Description`: Delete Subscription Data.

* `Content-type`:
  
        Content-Type: application/json


### Example Request
```json
```http
GET /delete/<int:subscription_id> HTTP/1.1
Host: api.example.com
Content-Type:  application/json

    {
    "Authorization": "Token 371a77d488199b7dc3be15c9424b96b555322086"
}

```

### Example Reponse

1.` HTTP Status: 200 OK`
```
{
   "message":"Subscription plan deleted successfully"
}
```


### Other Responses

### **1. Forbidden action**

**HTTP Status:** `401 UNAUTHORIZED`

```json
{
    "message": "You do not have permission to perform this action."
}
```
### **1. No valid Subscription**

**HTTP Status:** `404 NOT FOUND`

```json
{
    "detail": "No Subscription matches the given query."
}
```


### Messages

1. **No valid Subscription**
```json
{
    "detail": "No Subscription matches the given query."
}
```
---

