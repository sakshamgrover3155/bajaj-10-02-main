"""
MINIMAL TEST VERSION - Just Fibonacci
Use this to test if the basic structure works
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"is_success": True, "official_email": "saksham2200.be23@chitkara.edu.in"}), 200

@app.route('/bfhl', methods=['POST'])
def bfhl():
    print("\n=== REQUEST RECEIVED ===")
    print(f"Content-Type: {request.content_type}")
    print(f"Is JSON: {request.is_json}")
    print(f"Data: {request.data}")
    print(f"JSON: {request.get_json()}")
    print("========================\n")
    
    try:
        if not request.is_json:
            print("ERROR: Not JSON")
            return jsonify({"is_success": False}), 400
        
        data = request.get_json()
        
        if not data:
            print("ERROR: Empty data")
            return jsonify({"is_success": False}), 400
        
        if 'fibonacci' in data:
            n = data['fibonacci']
            print(f"Processing Fibonacci({n})")
            
            if not isinstance(n, int) or n < 0:
                print(f"ERROR: Invalid fibonacci value: {n}")
                return jsonify({"is_success": False}), 400
            
            # Generate fibonacci
            if n == 0:
                result = []
            elif n == 1:
                result = [0]
            else:
                result = [0, 1]
                for i in range(2, n):
                    result.append(result[-1] + result[-2])
            
            print(f"SUCCESS: Result = {result}")
            return jsonify({
                "is_success": True,
                "official_email": "test@chitkara.edu.in",
                "data": result
            }), 200
        
        print("ERROR: No fibonacci key found")
        return jsonify({"is_success": False}), 400
    
    except Exception as e:
        print(f"EXCEPTION: {e}")
        return jsonify({"is_success": False}), 500

if __name__ == '__main__':
    print("Starting minimal test server...")
    print("Test with: curl -X POST http://localhost:5000/bfhl -H 'Content-Type: application/json' -d '{\"fibonacci\": 5}'")
    app.run(host='0.0.0.0', port=5000, debug=True)
