from flask import Flask, render_template, request, jsonify, send_file
import qrcode
from io import BytesIO

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

@app.route('/qr')
def generate_qr():
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the data
    qr.add_data('https://protein-calculator-1.onrender.com/')
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a bytes buffer
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True) 