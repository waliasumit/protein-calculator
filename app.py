from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        if weight <= 0:
            return jsonify({'error': 'Weight must be positive'}), 400
        
        # Calculate protein needs (0.8-1.0g per kg)
        min_protein = weight * 0.8
        max_protein = weight * 1.0
        
        return jsonify({
            'min_protein': round(min_protein, 1),
            'max_protein': round(max_protein, 1)
        })
    except ValueError:
        return jsonify({'error': 'Please enter a valid weight in kilograms'}), 400

if __name__ == '__main__':
    app.run(debug=True) 