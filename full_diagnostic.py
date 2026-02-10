"""
Complete Diagnostic Script
This will show us exactly what's happening
"""
import requests
import json
import sys

BASE_URL = "http://localhost:5000"

print("\n" + "="*70)
print("COMPLETE DIAGNOSTIC TEST")
print("="*70)

# Test 1: Health Check First
print("\n1. HEALTH CHECK TEST")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code != 200:
        print("❌ ERROR: Health check failed!")
        sys.exit(1)
    print("✅ Health check passed!")
except Exception as e:
    print(f"❌ ERROR connecting to server: {e}")
    print("\nMake sure Flask app is running with: python app.py")
    sys.exit(1)

# Test 2: Simple Fibonacci
print("\n2. FIBONACCI TEST (simplest case)")
print("-" * 70)
request_data = {"fibonacci": 5}
print(f"Sending: {json.dumps(request_data)}")

try:
    response = requests.post(
        f"{BASE_URL}/bfhl",
        json=request_data,
        headers={"Content-Type": "application/json"}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        print("✅ SUCCESS!")
    else:
        print("❌ FAILED!")
        
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 3: Check what the server actually receives
print("\n3. DETAILED REQUEST TEST")
print("-" * 70)
print("Testing with explicit headers and JSON encoding...")

import urllib.request
import json

data = {"fibonacci": 3}
json_data = json.dumps(data).encode('utf-8')

print(f"Data being sent: {data}")
print(f"JSON encoded: {json_data}")

try:
    req = urllib.request.Request(
        f"{BASE_URL}/bfhl",
        data=json_data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(f"Status: {response.status}")
        print(f"Response: {result}")
        
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}")
    print(f"Response: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")

# Test 4: All operations
print("\n4. TESTING ALL OPERATIONS")
print("-" * 70)

tests = [
    ("Fibonacci", {"fibonacci": 5}),
    ("Prime", {"prime": [2, 3, 4, 5]}),
    ("LCM", {"lcm": [12, 18]}),
    ("HCF", {"hcf": [12, 18]}),
    ("AI", {"AI": "What is 1+1?"})
]

for name, data in tests:
    print(f"\nTesting {name}...")
    print(f"Request: {json.dumps(data)}")
    
    try:
        response = requests.post(f"{BASE_URL}/bfhl", json=data)
        print(f"Status: {response.status_code} | Response: {response.text[:100]}")
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "="*70)
print("DIAGNOSTIC COMPLETE")
print("="*70)
print("\n⚠️  IMPORTANT: Check your Flask console for the server-side logs!")
print("Look for lines starting with 'Received data:', 'Provided keys:', etc.")
print("\nIf you see 'Error: Expected 1 key, got 2' or similar messages,")
print("please copy and paste the COMPLETE Flask console output.")
print("="*70 + "\n")
