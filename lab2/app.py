from flask import Flask,render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)


#ROUTE HOME
@app.route("/")
def home():
    return render_template('index.html')

#ROUTE CASESAR
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar.html', inputPlainText = text, inputKeyPlain = key, outputCipherText = encrypted_text)

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template('caesar.html', inputCipherText = text, inputKeyCipher = key, outputPlainText = decrypted_text)

#ROUTE VIGENERE
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return render_template('vigenere.html', inputPlainText = text, inputKeyPlain = key, outputCipherText = encrypted_text)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return render_template('vigenere.html', inputCipherText = text, inputKeyCipher = key, outputPlainText = decrypted_text)

#ROUTE RAILFENCE
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailfenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return render_template('railfence.html', inputPlainText = text, inputKeyPlain = key, outputCipherText = encrypted_text)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailfenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return render_template('railfence.html', inputCipherText = text, inputKeyCipher = key, outputPlainText = decrypted_text)

#ROUTE TRANSPOSITION
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    return render_template('transposition.html', inputPlainText = text, inputKeyPlain = key, outputCipherText = encrypted_text)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    return render_template('transposition.html', inputCipherText = text, inputKeyCipher = key, outputPlainText = decrypted_text)

#ROUTE PLAYFAIR
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return render_template('playfair.html', inputPlainText = text, inputKeyPlain = key, outputCipherText = encrypted_text)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return render_template('playfair.html', inputCipherText = text, inputKeyCipher = key, outputPlainText = decrypted_text)

#MAIN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5050, debug=True)