# Chat Service

## Description
The Chat Service handles messaging between users. It provides endpoints for sending and retrieving messages.

## Dependencies
- Flask=2.1.1
- pymongo=4.0.1
- Werkzeug==2.1.1

## Endpoints
- `POST /send`: Send a message.
- `GET /messages/<receiver>`: Retrieve messages for a specific receiver.

### Send Message
- **URL:** `/send`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "sender": "string",
    "receiver": "string",
    "message": "string"
  }

### Response:
 - 201 Created if the message is sent successfully.

### GET Message
- **URL:** `/message`
- **Method:** `GET`
- **Response:**
    - 200 OK with a list of messages.

## Running the Service

To run the service, use Docker Compose:

```bash docker-compose up --build chat-service ```
