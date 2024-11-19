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
    "password":"syam123",
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

