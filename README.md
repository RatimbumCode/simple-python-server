# Simple Python Server

A lightweight Flask-based server that responds to GET requests with a JSON payload, secured with a token-based authentication system using environment variables.

## Features

- Responds to GET requests at the root endpoint (`/`) with a JSON message.
- Requires a valid verification token passed as a query parameter (`?token=`).
- Returns a success response (HTTP 200) with details if the token is valid.
- Returns an error response (HTTP 401) if the token is invalid or missing.
- Uses environment variables for secure token management.

## Installation

1. **Clone the Repository** (if applicable):

   ```bash
   git clone https://github.com/RatimbumCode/simple-python-server.git
   ```

   ```bash
   cd simple-python-server
   ```

2. **Install Required Packages**:
   Install the necessary Python packages using pip:

   ```bash
   pip install flask python-dotenv
   ```

   - `flask`: Web framework for building the server.
   - `python-dotenv`: Loads environment variables from a `.env` file.

3. **Set Up Environment Variables**:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` to set your own `API_TOKEN`:
     ```
     API_TOKEN=your-secure-token-here
     ```
   - **Note**: Keep `.env` secret and never commit it to version control (it’s already in `.gitignore`).

## Running the Server

1. **Start the Server**:
   Run the application:

   ```bash
   python app.py
   ```

   - The server will start in debug mode on `http://0.0.0.0:5000`.
   - Debug mode provides detailed error messages and auto-reloads on code changes.

2. **Test the Endpoint**:
   Use `curl` or a browser to test:
   - **Valid Request**:
     ```bash
     curl "http://localhost:5000/?token=your-secure-token-here"
     ```
     Example response:
     ```json
     {
       "message": "Hello! This is a JSON response from Flask.",
       "status": "success",
       "timestamp": "2025-03-11T12:34:56.789012",
       "method": "GET",
       "path": "/"
     }
     ```
   - **Invalid/Missing Token**:
     ```bash
     curl "http://localhost:5000/?token=wrong-token"
     ```
     Example response:
     ```json
     {
       "message": "Invalid or missing verification token.",
       "status": "error",
       "timestamp": "2025-03-11T12:34:56.789012"
     }
     ```

## Configuration

- **API_TOKEN**: Set this in `.env` to define the verification token. If not set, it falls back to `"default-token-fallback"`.
- **Host/Port**: Modify the `app.run()` parameters in `app.py` if you need a different host or port (e.g., `port=8080`).

## Development Notes

- **Debug Mode**: Enabled by default (`debug=True`). Disable it in production for security (`debug=False`).
- **Security**: For production, use HTTPS and a strong, unique token (e.g., generated with `secrets.token_urlsafe(32)` in Python).

## Generating a Secure Token

To create a strong token for your `.env`:

```python
import secrets
print(secrets.token_urlsafe(32))  # e.g., "oKj8yL9pQz8XvW2mK7tR4sN1uH5bG3dF"
```
