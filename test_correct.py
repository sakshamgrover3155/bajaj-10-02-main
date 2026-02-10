import requests

BASE_URL = "http://localhost:5000"

print("\n🧪 Testing BFHL API with correct format...\n")

# Test 1: Health
print("1. Health Check:")
try:
    r = requests.get(f"{BASE_URL}/health")
    print(f"   ✅ Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 2: Fibonacci
print("2. Fibonacci (n=5):")
try:
    r = requests.post(f"{BASE_URL}/bfhl", json={"fibonacci": 5})
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 3: Prime
print("3. Prime Numbers:")
try:
    r = requests.post(f"{BASE_URL}/bfhl", json={"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 4: LCM
print("4. LCM:")
try:
    r = requests.post(f"{BASE_URL}/bfhl", json={"lcm": [12, 18, 24]})
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 5: HCF
print("5. HCF:")
try:
    r = requests.post(f"{BASE_URL}/bfhl", json={"hcf": [48, 64, 80]})
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 6: AI
print("6. AI Question:")
try:
    r = requests.post(f"{BASE_URL}/bfhl", json={"AI": "What is Python?"})
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

print("=" * 60)
print("✅ All tests complete!")
print("=" * 60)
print("\nIf all tests show Status 200 and is_success: true, you're good!")
print("If you see errors, check the Flask console for details.")
