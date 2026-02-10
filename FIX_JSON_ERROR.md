# 🔧 FIX: "Failed to decode JSON object" Error

## The Problem
You're getting: `Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)`

This means the server is receiving **empty or invalid data**.

## ✅ SOLUTION: Correct Ways to Send Requests

### Method 1: Using curl (CORRECT FORMAT)

```bash
# ✅ CORRECT - Note the single quotes around JSON and double quotes inside
curl -X POST http://localhost:5000/bfhl \
  -H 'Content-Type: application/json' \
  -d '{"fibonacci": 5}'
```

**Common curl Mistakes:**

```bash
# ❌ WRONG - Missing Content-Type header
curl -X POST http://localhost:5000/bfhl -d '{"fibonacci": 5}'

# ❌ WRONG - Using double quotes outside (doesn't work in bash)
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d "{"fibonacci": 5}"

# ❌ WRONG - Not escaping quotes properly
curl -X POST http://localhost:5000/bfhl \
  -H 'Content-Type: application/json' \
  -d {"fibonacci": 5}
```

### Method 2: Using Python requests (RECOMMENDED)

```python
import requests

# ✅ CORRECT - Using json parameter (automatically sets Content-Type)
response = requests.post(
    'http://localhost:5000/bfhl',
    json={"fibonacci": 5}
)
print(response.json())

# ❌ WRONG - Using data parameter without headers
response = requests.post(
    'http://localhost:5000/bfhl',
    data='{"fibonacci": 5}'
)
```

### Method 3: Using Postman

1. **Method:** POST
2. **URL:** `http://localhost:5000/bfhl`
3. **Headers Tab:**
   - Key: `Content-Type`
   - Value: `application/json`
4. **Body Tab:**
   - Select: **raw**
   - Select: **JSON** (from dropdown)
   - Enter:
   ```json
   {
     "fibonacci": 5
   }
   ```
5. Click **Send**

### Method 4: Using JavaScript/fetch

```javascript
// ✅ CORRECT
fetch('http://localhost:5000/bfhl', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({fibonacci: 5})
})
.then(r => r.json())
.then(data => console.log(data));

// ❌ WRONG - Missing Content-Type
fetch('http://localhost:5000/bfhl', {
  method: 'POST',
  body: JSON.stringify({fibonacci: 5})
})
```

## 🧪 Test All Endpoints

Save this as `test_correct.py`:

```python
import requests

BASE_URL = "http://localhost:5000"

print("Testing all endpoints with CORRECT format...\n")

# Test 1: Health
print("1. Health Check:")
r = requests.get(f"{BASE_URL}/health")
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

# Test 2: Fibonacci
print("2. Fibonacci:")
r = requests.post(f"{BASE_URL}/bfhl", json={"fibonacci": 5})
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

# Test 3: Prime
print("3. Prime:")
r = requests.post(f"{BASE_URL}/bfhl", json={"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

# Test 4: LCM
print("4. LCM:")
r = requests.post(f"{BASE_URL}/bfhl", json={"lcm": [12, 18, 24]})
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

# Test 5: HCF
print("5. HCF:")
r = requests.post(f"{BASE_URL}/bfhl", json={"hcf": [48, 64, 80]})
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

# Test 6: AI
print("6. AI:")
r = requests.post(f"{BASE_URL}/bfhl", json={"AI": "What is Python?"})
print(f"   Status: {r.status_code}")
print(f"   Response: {r.json()}\n")

print("✅ All tests complete!")
```

Run it:
```bash
python test_correct.py
```

## 🔍 Debugging Steps

### Step 1: Restart Flask
```bash
# Stop current server (Ctrl+C)
# Start fresh
python app.py
```

### Step 2: Test with the simplest possible request
```bash
curl -X POST http://localhost:5000/bfhl \
  -H 'Content-Type: application/json' \
  -d '{"fibonacci": 5}'
```

### Step 3: Check Flask console output
You should see:
```
============================================================
Content-Type: application/json
Raw Data: {"fibonacci": 5}
Parsed Data: {'fibonacci': 5}
Operation: fibonacci, Input: 5
✅ Success! Result: [0, 1, 1, 2, 3]
============================================================
```

If you see this, it's working!

## 📋 Quick Reference

| Operation | Request Body | Expected Response |
|-----------|-------------|-------------------|
| Fibonacci | `{"fibonacci": 5}` | `{"is_success": true, "data": [0,1,1,2,3]}` |
| Prime | `{"prime": [1,2,3,4,5]}` | `{"is_success": true, "data": [2,3,5]}` |
| LCM | `{"lcm": [12, 18]}` | `{"is_success": true, "data": 36}` |
| HCF | `{"hcf": [12, 18]}` | `{"is_success": true, "data": 6}` |
| AI | `{"AI": "What is 1+1?"}` | `{"is_success": true, "data": "Two"}` |

## ⚠️ Important Notes

1. **Content-Type header is MANDATORY** - Without it, Flask won't parse JSON
2. **Use single quotes** around JSON in curl, **double quotes** inside
3. **Python requests** with `json=` parameter is the easiest method
4. **Check your quotes** - This is the #1 cause of JSON errors

## Still Not Working?

Try this minimal test:
```python
import requests
r = requests.post('http://localhost:5000/bfhl', json={"fibonacci": 1})
print(f"Status: {r.status_code}")
print(f"Text: {r.text}")
```

If this doesn't return `{"is_success": true, ...}`, share:
1. The exact output
2. The Flask console logs
3. What command you're using
