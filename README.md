# Chat Service

## Description
The Chat Service handles sending and receiving messages.

## Endpoints

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
