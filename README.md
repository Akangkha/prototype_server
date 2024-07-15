# Trend-Centric Recommendation App Server

## Overview

This Flask server is a crucial component of the Trend-Centric Recommendation App. It handles user requests related to body measurements and color palette generation based on the user's skin color. The server is designed to integrate seamlessly with the machine learning models used in the app.

## API Endpoints

### 1. `/measurements`
- **Method:** POST
- **Description:** This endpoint receives user body measurements and processes them to provide size recommendations for different apparel.
- **Request Body:**
  ```json
  {
    "bust": "<value>",
    "upper_hip": "<value>",
    "hip": "<value>",
    "waist": "<value>"
  }
  ```
- **Response:**
  ```json
  {
    "upper_body_size": "<recommended size>",
    "lower_body_size": "<recommended size>"
  }
  ```

### 2. `/generate_palette`
- **Method:** POST
- **Description:** This endpoint takes the user's skin color and generates a complementary color palette using the Gemini-1.5-Flash model.
- **Request Body:**
  ```json
  {
    "skin_color": "<hex code or RGB value>"
  }
  ```
- **Response:**
  ```json
  {
    "color_palette": [
      "<color1>",
      "<color2>",
      "<color3>",
     
    ]
  }
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Akangkha/prototype_server]
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   flask run
   ```

## Usage

1. **Start the server:**
   Ensure the server is running by executing the start command in the terminal.
   ```bash
   flask run
   ```

2. **Send a POST request to `/measurements`:**
   - Use tools like Postman or curl to send a POST request with the required body measurements.
   
     ```bash
     curl -X POST http://localhost:5000/measurements \
     -H "Content-Type: application/json" \
     -d '{"bust": 34, "upper_hip": 36, "hip": 38, "waist": 30}'
     ```

3. **Send a POST request to `/generate_palette`:**
   - Use tools like Postman or curl to send a POST request with the user's skin color.
