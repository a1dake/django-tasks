# Tasks API Documentation

## Endpoints:
1. List and Create Tasks
   - URL: /tasks/
   - Methods: POST (Create Task), GET (List Tasks)
   - Request Body (POST): TaskSerializer
   - Response (POST): TaskSerializer (201 Created), Error (400 Bad Request)
   - Response (GET): Paginated list of TaskSerializer

2. Retrieve, Update, and Delete Task
   - URL: /tasks/<int:task_id>/
   - Methods: GET (Retrieve Task), PUT (Update Task), DELETE (Delete Task)
   - Path Variable: task_id (int)
   - Response (GET): TaskSerializer (200 OK)
   - Request Body (PUT): TaskSerializer
   - Response (PUT): Updated TaskSerializer (200 OK), Error (400 Bad Request)
   - Response (DELETE): No content (204 No Content), Error (404 Not Found)

## Sample Usage:
### 1. Task List:
   - Endpoint: /tasks/
   - Method: GET
   - Response:
     ```json
     {
       "id": 1,
       "title": "New Task",
       "description": "Task description...",
       "status": false,
       "created_at": "2023-12-11T12:00:00Z"
     },
     {
       "id": 2,
       "title": "New Task 2",
       "description": "Task description 2...",
       "status": true,
       "created_at": "2023-12-11T12:00:00Z"
     }
     ```
     
### 2. Create Task:
   - Endpoint: /tasks/
   - Method: POST
   - Request Body:
     ```json
     {
       "title": "New Task",
       "description": "Task description...",
       "status": false
     }
     ```
   - Response:
     ```json
     {
       "id": 1,
       "title": "New Task",
       "description": "Task description...",
       "status": false
     }
     ```

### 3. Retrieve Task:
   - Endpoint: /tasks/1/
   - Method: GET
   - Response:
     ```json
     {
       "id": 1,
       "title": "New Task",
       "description": "Task description...",
       "status": false,
       "created_at": "2023-12-11T12:00:00Z"
     }
     ```

### 4. Update Task:
   - Endpoint: /tasks/1/
   - Method: PUT
   - Request Body:
     ```json
     {
       "title": "Updated Task",
       "description": "Updated description...",
       "status": true
     }
     ```
   - Response:
     ```json
     {
       "id": 1,
       "title": "Updated Task",
       "description": "Updated description...",
       "status": true,
       "created_at": "2023-12-11T12:00:00Z",
       "updated_at": "2023-12-11T13:00:00Z"
     }
     ```

### 5. Delete Task:
   - Endpoint: /tasks/1/
   - Method: DELETE
   - Response: No content (204 No Content)