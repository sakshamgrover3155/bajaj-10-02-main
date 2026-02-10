# 🔧 TROUBLESHOOTING GUIDE - BFHL Endpoint Returns {"is_success": false}

## Quick Diagnostic Steps

### Step 1: Check What You're Sending
Make sure your request looks exactly like this:

**Correct Format:**
```json
{
  "fibonacci": 5
}
```

**Common Mistakes:**
```json
// ❌ WRONG - Typo in key name
{
  "fibonaci": 5
}

// ❌ WRONG - Multiple keys
{
  "fibonacci": 5,
  "prime": [1, 2, 3]
}

// ❌ WRONG - Wrong data type
{
  "fibonacci": "5"  // Should be integer, not string
}

// ❌ WRONG - Negative number
{
  "fibonacci": -5
}
```

### Step 2: Run Debug Test
```bash
# Start your Flask app in one terminal
python app.py

# In another terminal, run the debug test
python debug_test.py
```

This will show you exactly what's failing and print detailed logs.

### Step 3: Check Flask Console
When you run the app, you should see detailed logs like:
```
Received data: {'fibonacci': 5}
Provided keys: ['fibonacci']
Operation: fibonacci, Input: 5
Fibonacci result: [0, 1, 1, 2, 3]
Success response: {'is_success': True, 'official_email': '...', 'data': [...]}
```

If you see an error line, that tells you what's wrong.

## Common Issues & Solutions

### Issue 1: "Request is not JSON"
**Cause:** Missing `Content-Type: application/json` header

**Solution:**
```bash
# ✅ CORRECT
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'

# ❌ WRONG - Missing header
curl -X POST http://localhost:5000/bfhl \
  -d '{"fibonacci": 5}'
```

### Issue 2: "Expected 1 key, got 0"
**Cause:** Sending wrong key name or empty object

**Solution:** Check spelling - it's case-sensitive!
- ✅ `fibonacci` (lowercase)
- ✅ `prime` (lowercase)
- ✅ `lcm` (lowercase)
- ✅ `hcf` (lowercase)
- ✅ `AI` (uppercase!)
- ❌ `Fibonacci` (wrong case)
- ❌ `PRIME` (wrong case)

### Issue 3: "Expected 1 key, got 2"
**Cause:** Sending multiple keys

**Solution:** Send ONLY ONE operation per request
```json
// ❌ WRONG
{
  "fibonacci": 5,
  "prime": [1, 2, 3]
}

// ✅ CORRECT - Separate requests
Request 1: {"fibonacci": 5}
Request 2: {"prime": [1, 2, 3]}
```

### Issue 4: "Invalid fibonacci input"
**Cause:** Wrong data type or negative number

**Solution:**
```json
// ✅ CORRECT
{"fibonacci": 10}

// ❌ WRONG - String instead of integer
{"fibonacci": "10"}

// ❌ WRONG - Float instead of integer
{"fibonacci": 10.5}

// ❌ WRONG - Negative
{"fibonacci": -5}
```

### Issue 5: "Prime input is not a list"
**Cause:** Sending integer instead of array

**Solution:**
```json
// ✅ CORRECT
{"prime": [1, 2, 3, 4, 5]}

// ❌ WRONG - Not an array
{"prime": 5}

// ❌ WRONG - String
{"prime": "[1,2,3]"}
```

### Issue 6: "Array contains non-integers"
**Cause:** Array has strings or floats

**Solution:**
```json
// ✅ CORRECT
{"prime": [1, 2, 3, 4, 5]}

// ❌ WRONG - Contains strings
{"prime": ["1", "2", "3"]}

// ❌ WRONG - Contains floats
{"prime": [1.5, 2.3, 3.7]}
```

### Issue 7: AI endpoint not working
**Cause:** Missing or invalid Gemini API key

**Solution:**
```bash
# Check if API key is set
echo $GEMINI_API_KEY

# If empty, set it:
export GEMINI_API_KEY="your_actual_api_key_here"

# Restart Flask app
python app.py
```

## Testing Each Endpoint

### 1. Fibonacci
```bash
# Should return: [0, 1, 1, 2, 3]
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'
```

### 2. Prime
```bash
# Should return: [2, 3, 5, 7]
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}'
```

### 3. LCM
```bash
# Should return: 72
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12, 18, 24]}'
```

### 4. HCF
```bash
# Should return: 6
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [12, 18, 24]}'
```

### 5. AI
```bash
# Should return single word like: "Paris"
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the capital of France?"}'
```

## Using Postman

1. **Set Method:** POST
2. **Set URL:** `http://localhost:5000/bfhl`
3. **Headers:**
   - Key: `Content-Type`
   - Value: `application/json`
4. **Body:** Select "raw" and "JSON", then paste:
```json
{
  "fibonacci": 5
}
```

## Using Python Requests

```python
import requests

# Test fibonacci
response = requests.post(
    'http://localhost:5000/bfhl',
    json={"fibonacci": 5}  # Automatically sets Content-Type
)
print(response.json())
```

## Still Having Issues?

1. **Check Python Version:**
   ```bash
   python --version  # Should be 3.11+
   ```

2. **Reinstall Dependencies:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

3. **Check if Server is Running:**
   ```bash
   curl http://localhost:5000/health
   # Should return: {"is_success": true, "official_email": "..."}
   ```

4. **Look at Flask Logs:**
   The terminal running `python app.py` shows all errors

5. **Try a Simple Test:**
   ```python
   import requests
   
   # This should definitely work
   r = requests.post(
       'http://localhost:5000/bfhl',
       json={"fibonacci": 5}
   )
   print(r.status_code)  # Should be 200
   print(r.json())       # Should show success response
   ```

## Need More Help?

Run this command and share the output:
```bash
python debug_test.py > debug_output.txt 2>&1
```

This will create a file with all the test results and error messages.
