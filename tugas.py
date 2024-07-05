from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def menu():
    return redirect(url_for('home'))

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        return redirect(url_for('login'))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = "tiara"
        password = "051103"
        input_username = request.form.get("username")
        input_password = request.form.get("password")

        if input_username == username and input_password == password:
            return redirect(url_for("daftarmobil"))
        else:
            return redirect(url_for("login"))
        
@app.route('/daftarmobil', methods=['GET', 'POST'])
def daftarmobil():
    mobil_list = [
         {'id': 1, 'nama': 'Daihatsu Xenia', 'tipe': 'MPV', 'Pajak': 'Hidup', 'Warna ': 'Merah','Harga Sewa' :'Rp 500.000', 'gambar': 'mobil.jpg'},
        {'id': 2, 'nama': 'Toyota Avanza', 'tipe': 'G13AT', 'gambar': 'mobil2.jpg','Pajak': 'Hidup', 'Warna ': 'Silver','Harga Sewa' :'Rp 400.000'},
    ]

    if request.method == "POST":
        mobil_id = request.form.get('mobil_id')
        return redirect(url_for('detail_mobil', mobil_id=mobil_id))
    return render_template('daftarmobil.html', mobil_list=mobil_list)

@app.route('/detail_mobil', methods=['GET', 'POST'])
def detail_mobil():
    mobil_id = request.args.get('mobil_id')
    print("Mobil ID:", mobil_id)

    if mobil_id is None:
        return "Mobil ID tidak diberikan"

    try:
        mobil_id = int(mobil_id)
    except ValueError:
        return "Mobil ID tidak valid"
    mobil_list = [
         {'id': 1, 'nama': 'Daihatsu Xenia', 'tipe': 'MPV', 'Pajak': 'Hidup', 'Warna': 'Merah','Harga Sewa' :'Rp 500.000', 'gambar': 'mobil.jpg'},
        {'id': 2, 'nama': 'Toyota Avanza', 'tipe': 'G13AT', 'gambar': 'mobil2.jpg', 'Pajak': 'Hidup', 'Warna': 'Silver', 'Harga Sewa': 'Rp 400.000'},
    ]
    mobil = next((m for m in mobil_list if m['id'] == mobil_id), None)
    print("Mobil:", mobil)
    if mobil is None:
        return "Mobil tidak ditemukan"

    if request.method == "POST":
        action = request.form.get('action')
        if action == "selanjutnya":
            return redirect(url_for('sewa'))
        elif action == "batal":
            return redirect(url_for('daftarmobil'))

    return render_template('detail_mobil.html', mobil=mobil)

@app.route("/sewa", methods=["POST", "GET"])
def sewa():
    if request.method == "GET":
        return render_template("sewa.html")
    
    elif request.method == "POST":
        action = request.form.get("action")
        
        if action == "selanjutnya":
            input_username = request.form.get("username")
            input_alamat_email = request.form.get("alamat_email")
            input_password = request.form.get("password")
            input_nomor_hp = request.form.get("nomor_hp")
            input_alamat = request.form.get("alamat")
            input_berapa_hari = request.form.get("berapa_hari")
            input_metode_pembayaran = request.form.get("metode_pembayaran")

            if input_username and input_alamat_email and input_password and input_nomor_hp and input_alamat and input_berapa_hari and input_metode_pembayaran:
                return redirect(url_for("transaksi", 
                                        username=input_username, 
                                        alamat_email=input_alamat_email, 
                                        nomor_hp=input_nomor_hp, 
                                        alamat=input_alamat,
                                        berapa_hari=input_berapa_hari,
                                        metode_pembayaran=input_metode_pembayaran))
        elif action == "batal":
            return redirect(url_for('daftarmobil'))
@app.route('/transaksi')
def transaksi():
    username = request.args.get('username')
    alamat_email = request.args.get('alamat_email')
    nomor_hp = request.args.get('nomor_hp')
    alamat = request.args.get('alamat')
    berapa_hari = request.args.get('berapa_hari')
    metode_pembayaran = request.args.get('metode_pembayaran')
    
    return render_template('transaksi.html', 
                           username=username, 
                           alamat_email=alamat_email, 
                           nomor_hp=nomor_hp, 
                           alamat=alamat, 
                           berapa_hari=berapa_hari,metode_pembayaran=metode_pembayaran)