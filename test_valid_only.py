"""
Test ONLY valid requests to verify API works
"""
import requests
import json

BASE_URL = "http://localhost:5000"

print("\n🧪 Testing VALID Requests Only\n")

# Test 1: Fibonacci
print("1. Testing Fibonacci...")
response = requests.post(f"{BASE_URL}/bfhl", json={"fibonacci": 5})
print(f"   Status: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}\n")

# Test 2: Prime
print("2. Testing Prime...")
response = requests.post(f"{BASE_URL}/bfhl", json={"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
print(f"   Status: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}\n")

# Test 3: LCM
print("3. Testing LCM...")
response = requests.post(f"{BASE_URL}/bfhl", json={"lcm": [12, 18, 24]})
print(f"   Status: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}\n")

# Test 4: HCF
print("4. Testing HCF...")
response = requests.post(f"{BASE_URL}/bfhl", json={"hcf": [48, 64, 80]})
print(f"   Status: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}\n")

# Test 5: AI (if API key is set)
print("5. Testing AI...")
response = requests.post(f"{BASE_URL}/bfhl", json={"AI": "What is Python?"})
print(f"   Status: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}\n")

print("✅ All tests completed!")
print("\nIf all status codes are 200 and is_success is True, your API is working perfectly!")
