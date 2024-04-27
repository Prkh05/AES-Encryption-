from flask import Flask, request, jsonify
from Crypto.Cipher import AES


app = Flask(__name__)

class Encrypter:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def encrypt_image(self):
        aes = AES(self.key)
        cipher = aes.encrypt(self.text)
        return cipher

@app.route('/encrypt_image', methods=['POST'])
def encrypt_image():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')
    
    if text is None or key is None:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    encrypter = Encrypter(text, key)
    encrypted_text = encrypter.encrypt_image()
    
    return jsonify({'encrypted_text': encrypted_text}), 200

if __name__ == '__main__':
    app.run()
