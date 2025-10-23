## How to Run the Project Locally

1. Clone the repository
```bash
git clone https://github.com/Afnan112/notification-service.git
cd notification-service
```
2. Install dependencies
```
pip install pipenv
pipenv install
pipenv shell
```
3. Apply database migrations
 ```
   python manage.py migrate
```
4. Run the server
```
python manage.py runserver
```
5. Access the API or admin panel
   Create notification: POST /api/notifications
   Check status and details of the notification: GET /api/notifications/:id
   Django admin (for viewing notifications): http://127.0.0.1:8000/admin/
