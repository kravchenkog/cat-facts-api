# Cat-Facts API Test

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