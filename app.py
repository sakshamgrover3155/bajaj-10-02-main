"""
Flask Backend API - Production Ready (Fixed JSON Handling)
Handles health check and BFHL endpoints with multiple operations
"""

from flask import Flask, request, jsonify
from functools import reduce
import math
import os
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configuration
OFFICIAL_EMAIL = "saksham2200@chitkara.edu.in"

# Configure Google Gemini API
try:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Warning: Gemini API configuration failed - {e}")


# ==================== UTILITY FUNCTIONS ====================

def generate_fibonacci(n):
    """Generate first N fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    
    return True


def filter_primes(numbers):
    """Filter prime numbers from an array"""
    return [num for num in numbers if is_prime(num)]


def calculate_gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return abs(a)


def calculate_hcf(numbers):
    """Calculate HCF of multiple numbers"""
    if not numbers:
        return 0
    return reduce(calculate_gcd, numbers)


def calculate_lcm_two(a, b):
    """Calculate LCM of two numbers"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calculate_gcd(a, b)


def calculate_lcm(numbers):
    """Calculate LCM of multiple numbers"""
    if not numbers:
        return 0
    return reduce(calculate_lcm_two, numbers)


def get_ai_response(question):
    """Get single-word answer from Google Gemini API"""
    try:
        if not GEMINI_API_KEY:
            return "Error"
        
        model = genai.GenerativeModel('gemini-pro')
        enhanced_prompt = f"""Answer the following question with EXACTLY ONE WORD only. 
No explanations, no punctuation, no additional text. Just one single word.

Question: {question}

Answer (one word only):"""
        
        response = model.generate_content(enhanced_prompt)
        answer = response.text.strip()
        answer = answer.split()[0] if answer else "Unknown"
        answer = ''.join(char for char in answer if char.isalnum())
        
        return answer
    
    except Exception as e:
        print(f"AI Error: {e}")
        return "Error"


# ==================== API ENDPOINTS ====================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }), 200


@app.route('/bfhl', methods=['POST'])
def bfhl_handler():
    """Main BFHL endpoint handler"""
    try:
        # Debug logging
        print(f"\n{'='*60}")
        print(f"Content-Type: {request.content_type}")
        print(f"Raw Data: {request.get_data(as_text=True)}")
        
        # Check content type
        if not request.content_type or 'application/json' not in request.content_type:
            print("Error: Content-Type must be application/json")
            return jsonify({"is_success": False}), 400
        
        # Parse JSON
        try:
            data = request.get_json(force=True)
        except Exception as e:
            print(f"JSON Parse Error: {e}")
            return jsonify({"is_success": False}), 400
        
        print(f"Parsed Data: {data}")
        
        # Validate not empty
        if not data:
            print("Error: Empty data")
            return jsonify({"is_success": False}), 400
        
        # Check for exactly one valid key
        valid_keys = ['fibonacci', 'prime', 'lcm', 'hcf', 'AI']
        provided_keys = [key for key in valid_keys if key in data]
        
        if len(provided_keys) != 1:
            print(f"Error: Expected 1 key, got {len(provided_keys)}")
            return jsonify({"is_success": False}), 400
        
        operation = provided_keys[0]
        input_value = data[operation]
        
        print(f"Operation: {operation}, Input: {input_value}")
        
        # Process operation
        result = None
        
        if operation == 'fibonacci':
            if not isinstance(input_value, int) or input_value < 0:
                return jsonify({"is_success": False}), 400
            result = generate_fibonacci(input_value)
        
        elif operation == 'prime':
            if not isinstance(input_value, list):
                return jsonify({"is_success": False}), 400
            if not all(isinstance(x, int) for x in input_value):
                return jsonify({"is_success": False}), 400
            result = filter_primes(input_value)
        
        elif operation == 'lcm':
            if not isinstance(input_value, list) or len(input_value) == 0:
                return jsonify({"is_success": False}), 400
            if not all(isinstance(x, int) for x in input_value):
                return jsonify({"is_success": False}), 400
            result = calculate_lcm(input_value)
        
        elif operation == 'hcf':
            if not isinstance(input_value, list) or len(input_value) == 0:
                return jsonify({"is_success": False}), 400
            if not all(isinstance(x, int) for x in input_value):
                return jsonify({"is_success": False}), 400
            result = calculate_hcf(input_value)
        
        elif operation == 'AI':
            if not isinstance(input_value, str) or len(input_value.strip()) == 0:
                return jsonify({"is_success": False}), 400
            result = get_ai_response(input_value)
        
        # Success response
        print(f"✅ Success! Result: {result}")
        print(f"{'='*60}\n")
        return jsonify({
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": result
        }), 200
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"is_success": False}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({"is_success": False}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"is_success": False}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"is_success": False}), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*70)
    print("🚀 Flask BFHL API Server")
    print("="*70)
    print(f"Server: http://localhost:{port}")
    print(f"Health: http://localhost:{port}/health")
    print(f"BFHL:   http://localhost:{port}/bfhl")
    print("="*70)
    print("\n📝 Test command:")
    print("curl -X POST http://localhost:5000/bfhl \\")
    print("  -H 'Content-Type: application/json' \\")
    print("  -d '{\"fibonacci\": 5}'")
    print("\n" + "="*70 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)
