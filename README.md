# Cat-Facts API Test

## Test Case 1: Get Random Cat Fact

| Test Step | Description                                       | Expected Outcome                      |
|-----------|---------------------------------------------------|---------------------------------------|
| 1         | Send GET request to `/facts/random`               | The response status code is `200 OK`  |
| 2         | Validate the `text` field in the response         | The `text` field contains a cat fact  |

## Test Case 2: Get All Cat Facts

| Test Step | Description                                       | Expected Outcome                      |
|-----------|---------------------------------------------------|---------------------------------------|
| 1         | Send GET request to `/facts`                      | The response status code is `200 OK`  |
| 2         | Ensure the response returns a list of cat facts   | The response is a list                |

## Test Case 3: Invalid Route

| Test Step | Description                                       | Expected Outcome                      |
|-----------|---------------------------------------------------|---------------------------------------|
| 1         | Send GET request to an invalid route `/invalid_route` | The response status code is `404 Not Found` |
| 2         | Validate that the response contains 404           | Assert that the status code is `404`  |

## 1. Install Dependencies

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 2. Running Tests

To run the tests, use:
```bash
pytest ./test-cat-facts.py
```

## 3. Project Structure

```
.
├── test-cat-facts.py          # API tests
├── requirements.txt           # Project dependencies
└── venv/                      # Virtual environment
```