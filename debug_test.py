"""
Simple Debug Test for BFHL Endpoint
Run this after starting the Flask app to test what's failing
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoint(name, data):
    """Test an endpoint and print detailed results"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"{'='*60}")
    print(f"Request Data: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/bfhl", json=data)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"ERROR: {e}")
    print(f"{'='*60}")

# Test each operation
print("\n🔍 Starting Debug Tests...\n")

# Test 1: Fibonacci
test_endpoint("Fibonacci (5)", {"fibonacci": 5})

# Test 2: Prime
test_endpoint("Prime Numbers", {"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Test 3: LCM
test_endpoint("LCM", {"lcm": [12, 18, 24]})

# Test 4: HCF
test_endpoint("HCF", {"hcf": [48, 64, 80]})

# Test 5: AI (if you have API key set)
test_endpoint("AI Question", {"AI": "What is Python?"})

# Test 6: Invalid - Multiple keys (should fail)
test_endpoint("Invalid - Multiple Keys", {"fibonacci": 5, "prime": [1, 2, 3]})

# Test 7: Invalid - No keys (should fail)
test_endpoint("Invalid - Empty", {})

# Test 8: Invalid - Wrong type
test_endpoint("Invalid - Wrong Type", {"fibonacci": "not a number"})

print("\n✅ Debug tests complete!")
print("\nCheck the Flask server console for detailed logs.")
print("Look for any error messages printed there.\n")
