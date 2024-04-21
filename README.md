# Daily Diet API

API made to control your diet and help you stay on track with your meals :)

## Functionalities

- Create a new meal
- Create and authenticate your account
- Search meals, edit or delete them

## Technologies Used

- Python
- SQLAlchemy
- Flask
- Flask-login
- Docker
- MySQL

## Installing the Project

```
git clone *projet-url*

cd *projects-directory*

pip3 install -r requirements.txt
```

## Load Docker Image (MySQL)

*Reminder: Docker software must be installed previously.

```
docker compose up -d
```

## Functional Requirements

- [x] It must be possible to register a meal.
- [x] It must be possible to list all meals for the user logged in.
- [x] It must be possible to view details of a specific meal.
- [x] It must be possible to edit and delete a meal created by your user.
- [x] It must be possible to register as a user.
- [x] It must be possible to log in and logout.

## Routes

### User Routes

#### Register User

```http
  POST /register
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Mandatory**. User's name |
| `password` | `string` | **Mandatory**. User's password. |

#### Authenticate User

```http
  POST /login
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Mandatory**. User's name. |
| `password` | `string` | **Mandatory**. User's password. |

#### Logout

```http
  GET /logout
```

### Meal Routes

#### Create Meal

```http
  POST /meal/register
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `meal_name` | `string` | **Mandatory**. Meal's name. |
| `description` | `string` | **Mandatory**. Meal's description. |
| `is_on_diet` | `boolean` | **Mandatory**. Tells wether the meal is on the diet track or not. |

#### Fetch Meals by User Logged In

```http
  GET /meal
```


#### Fetch Meal by ID

```http
  GET /meal/:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. Meal's ID. |
