"""Основное приложение - REST API калькулятора."""
from flask import Flask, request, jsonify
import logging
from src.calculator import Calculator

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
calculator = Calculator()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "calculator-api"}), 200

@app.route('/api/v1/add', methods=['POST'])
def add():
    """Endpoint для сложения."""
    data = request.get_json()
    try:
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.add(a, b)
        return jsonify({"operation": "add", "result": result}), 200
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1/subtract', methods=['POST'])
def subtract():
    """Endpoint для вычитания."""
    data = request.get_json()
    try:
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.subtract(a, b)
        return jsonify({"operation": "subtract", "result": result}), 200
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1/multiply', methods=['POST'])
def multiply():
    """Endpoint для умножения."""
    data = request.get_json()
    try:
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.multiply(a, b)
        return jsonify({"operation": "multiply", "result": result}), 200
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1/divide', methods=['POST'])
def divide():
    """Endpoint для деления."""
    data = request.get_json()
    try:
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.divide(a, b)
        return jsonify({"operation": "divide", "result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
