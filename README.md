# TODO App API

This is a REST API for a simple todo app built with Django and Django REST Framework.

## Getting Started

To run the project, you'll need to have Python 3 and pip installed on your system. Then, follow these steps:

1. Clone the repository: `git clone https://github.com/tonyoseko99/todo-assessment.git`
2. `cd` into the project directory: `cd todo-assessment`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the migrations: `python3 manage.py migrate`
5. Start the development server: `python3 manage.py runserver`

You should now be able to access the API at http://localhost:8000/.

## API Endpoints

- `/todos/`: GET (list all todos), POST (create a new todo)
- `/todos/<id>/`: GET (retrieve a todo by id), PUT (update a todo), DELETE (delete a todo)
- `/signup/`: POST (create a new user)
- `/api-auth/login/`: POST (login with username and password)
- `/api-auth/logout/`: POST (logout)

## Authentication

- The API uses token-based authentication. To access protected endpoints, you'll need to include an `Authorization` header with a token in your request. You can obtain a token by sending a POST request to `/api-auth/login/` with your username and password in the request body.
- Signup using the `/signup/` endpoint using the `username`, `email`, and `password` fields

## Documentation

API documentation is available at `/swagger/` or `/redoc/`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
