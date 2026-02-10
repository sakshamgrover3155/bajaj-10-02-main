"""
Test Script for Flask API
Tests all endpoints with various inputs
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:5000"

def print_response(test_name, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print(f"{'='*60}")

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print_response("Health Check", response)

def test_fibonacci():
    """Test fibonacci endpoint"""
    test_cases = [
        {"fibonacci": 10},
        {"fibonacci": 5},
        {"fibonacci": 0},
        {"fibonacci": 1}
    ]
    
    for test_case in test_cases:
        response = requests.post(f"{BASE_URL}/bfhl", json=test_case)
        print_response(f"Fibonacci: {test_case}", response)

def test_prime():
    """Test prime endpoint"""
    test_cases = [
        {"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        {"prime": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]},
        {"prime": [2, 4, 6, 8, 10]}
    ]
    
    for test_case in test_cases:
        response = requests.post(f"{BASE_URL}/bfhl", json=test_case)
        print_response(f"Prime: {test_case}", response)

def test_lcm():
    """Test LCM endpoint"""
    test_cases = [
        {"lcm": [12, 18, 24]},
        {"lcm": [4, 6, 8]},
        {"lcm": [10, 15, 20]}
    ]
    
    for test_case in test_cases:
        response = requests.post(f"{BASE_URL}/bfhl", json=test_case)
        print_response(f"LCM: {test_case}", response)

def test_hcf():
    """Test HCF endpoint"""
    test_cases = [
        {"hcf": [12, 18, 24]},
        {"hcf": [48, 64, 80]},
        {"hcf": [100, 150, 200]}
    ]
    
    for test_case in test_cases:
        response = requests.post(f"{BASE_URL}/bfhl", json=test_case)
        print_response(f"HCF: {test_case}", response)

def test_ai():
    """Test AI endpoint"""
    test_cases = [
        {"AI": "What is the capital of France?"},
        {"AI": "What is the largest planet in our solar system?"},
        {"AI": "What is 2+2?"}
    ]
    
    for test_case in test_cases:
        response = requests.post(f"{BASE_URL}/bfhl", json=test_case)
        print_response(f"AI: {test_case}", response)

def test_error_cases():
    """Test error handling"""
    print("\n" + "="*60)
    print("TESTING ERROR CASES")
    print("="*60)
    
    # Multiple keys
    response = requests.post(f"{BASE_URL}/bfhl", json={"fibonacci": 5, "prime": [1, 2, 3]})
    print_response("Error: Multiple Keys", response)
    
    # Invalid type
    response = requests.post(f"{BASE_URL}/bfhl", json={"fibonacci": "not a number"})
    print_response("Error: Invalid Type", response)
    
    # Empty request
    response = requests.post(f"{BASE_URL}/bfhl", json={})
    print_response("Error: Empty Request", response)
    
    # Wrong HTTP method
    response = requests.get(f"{BASE_URL}/bfhl")
    print_response("Error: Wrong Method", response)

if __name__ == "__main__":
    print("\n🚀 Starting API Tests...\n")
    
    try:
        # Test all endpoints
        test_health()
        test_fibonacci()
        test_prime()
        test_lcm()
        test_hcf()
        test_ai()
        test_error_cases()
        
        print("\n✅ All tests completed!\n")
    
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the API")
        print("Make sure the Flask app is running on http://localhost:5000\n")
    
    except Exception as e:
        print(f"\n❌ Error during testing: {e}\n")
