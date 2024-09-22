from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to validate base64 string (placeholder)
def validate_base64(file_b64):
    # For now, assume any base64 string is valid. In real scenario, add validation logic here.
    return True

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Parse the JSON request body
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)

        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        # Validate file if provided
        file_valid = validate_base64(file_b64) if file_b64 else False
        file_mime_type = "image/png" if file_valid else None  # Dummy MIME type for the purpose of this challenge
        file_size_kb = len(file_b64) / 1024 if file_b64 else None  # Calculate size based on base64 string length

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic user_id logic
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
