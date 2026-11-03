from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# Satu rute untuk GET (buka halaman) dan POST (kirim formulir)
@app.route("/", methods=["GET", "POST"])
def beranda():
    nama = ""
    if request.method == "POST":
        # Ambil nama, buang spasi di tepi, batasi maksimal 50 karakter
        nama = request.form.get("nama", "").strip()[:50]

    # Tanggal dan jam server saat ini
    sekarang = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template("index.html", sekarang=sekarang, nama=nama)

if __name__ == "__main__":
    # Berjalan di localhost saja
    app.run(host="127.0.0.1", port=5000, debug=True)