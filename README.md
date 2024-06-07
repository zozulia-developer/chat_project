# Simple Chat Application

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd chat_project
    ```
   
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add the following configuration:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- `/api/chat/threads/` - Create or get a thread.
- `/api/chat/threads/<int:pk>/` - Delete a thread.
- `/api/chat/threads/user/` - Get user threads.
- `/api/chat/messages/` - Create a message.
- `/api/chat/messages/thread/<int:thread_id>/` - Get thread messages.
- `/api/chat/messages/<int:pk>/read/` - Mark message as read.
- `/api/chat/messages/unread/` - Get unread messages count.

## Authentication

Use JWT for authentication.

## API Documentation

Swagger and ReDoc documentation are available:
- Swagger: `/swagger/`
- ReDoc: `/redoc/`