from flask import Flask, url_for, render_template, request, redirect, session
import os
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    return render_template('index.html')

#region ELEKTRIKSEL
@app.route("/akim", methods=["GET","POST"])
def akim():
    if request.method == "POST":
        gerilim = request.form["gerilim"]
        direnc = request.form["direnc"]
        if gerilim and direnc:
            gerilim = float(gerilim)
            direnc = float(direnc)
            result = gerilim/direnc
            values = {"gerilim":gerilim,"direnc":direnc}
            return render_template("pages/elektriksel/akim.html", result=result, values=values)
    return render_template("pages/elektriksel/akim.html")

@app.route("/direnc", methods=["GET","POST"])
def direnc():
    if request.method == "POST":
        gerilim = request.form["gerilim"]
        akim = request.form["akim"]
        if gerilim and akim:
            gerilim = float(gerilim)
            akim = float(akim)
            result = gerilim/akim
            values = {"gerilim":gerilim,"akim":akim}
            return render_template("pages/elektriksel/direnc.html", result=result, values=values)
    return render_template("pages/elektriksel/direnc.html")

@app.route("/gerilim", methods=["GET","POST"])
def gerilim():
    if request.method == "POST":
        direnc = request.form["direnc"]
        akim = request.form["akim"]
        if direnc and akim:
            direnc = float(direnc)
            akim = float(akim)
            result = direnc * akim
            values = {"direnc":direnc,"akim":akim}
            return render_template("pages/elektriksel/gerilim.html", result=result, values=values)
    return render_template("pages/elektriksel/gerilim.html")

@app.route("/siga", methods=["GET","POST"])
def siga():
    if request.method == "POST":
        yuk = request.form["yuk"]
        potansiyel = request.form["potansiyel"]
        if yuk and potansiyel:
            yuk = float(yuk)
            potansiyel = float(potansiyel)
            result = yuk / potansiyel
            values = {"yuk":yuk,"potansiyel":potansiyel}
            return render_template("pages/elektriksel/siga.html", result=result, values=values)
    return render_template("pages/elektriksel/siga.html")

@app.route("/siga2", methods=["GET","POST"])
def siga2():
    if request.method == "POST":
        katsayi = request.form["katsayi"]
        alan = request.form["alan"]
        mesafe = request.form["mesafe"]
        if katsayi and alan and mesafe:
            katsayi = float(katsayi)
            alan = float(alan)
            mesafe = float(mesafe)
            result = katsayi * alan / mesafe
            values = {"katsayi":katsayi,"alan":alan, "mesafe":mesafe}
            return render_template("pages/elektriksel/siga2.html", result=result, values=values)
    return render_template("pages/elektriksel/siga2.html")

@app.route("/kuvvet", methods=["GET","POST"])
def kuvvet():
    if request.method == "POST":
        yuk1= request.form["yuk1"]
        yuk2 = request.form["yuk2"]
        mesafe = request.form["mesafe"]
        if yuk1 and yuk2 and mesafe:
            yuk1 = float(yuk1)
            yuk2 = float(yuk2)
            mesafe = float(mesafe)
            result = yuk1 * yuk2 * 9 / (mesafe * mesafe)
            values = {"yuk1":yuk1,"yuk2":yuk2, "mesafe":mesafe}
            return render_template("pages/elektriksel/kuvvet.html", result=result, values=values)
    return render_template("pages/elektriksel/kuvvet.html")
#endregion


#region ENERJI
@app.route("/esneklik", methods=["GET","POST"])
def esneklik():
    if request.method == "POST":
        sabit= request.form["sabit"]
        yol = request.form["yol"]
        if sabit and yol:
            sabit = float(sabit)
            yol = float(yol)
            result = sabit * yol * yol / 2
            values = {"sabit":sabit,"yol":yol}
            return render_template("pages/enerji/esneklik.html", result=result, values=values)
    return render_template("pages/enerji/esneklik.html")

@app.route("/kinetik", methods=["GET","POST"])
def kinetik():
    if request.method == "POST":
        kutle= request.form["kutle"]
        hiz = request.form["hiz"]
        if kutle and hiz:
            kutle = float(kutle)
            hiz = float(hiz)
            result = kutle * hiz * hiz / 2
            values = {"kutle":kutle,"hiz":hiz}
            return render_template("pages/enerji/kinetik.html", result=result, values=values)
    return render_template("pages/enerji/kinetik.html")

@app.route("/potansiyel", methods=["GET","POST"])
def potansiyel():
    if request.method == "POST":
        kutle= request.form["kutle"]
        yercekimi= request.form["yercekimi"]
        yukseklik = request.form["yukseklik"]
        if kutle and yercekimi and yukseklik:
            kutle = float(kutle)
            yercekimi = float(yercekimi)
            yukseklik = float(yukseklik)
            result = kutle * yercekimi * yukseklik
            values = {"kutle":kutle,"yercekimi":yercekimi, "yukseklik":yukseklik}
            return render_template("pages/enerji/potansiyel.html", result=result, values=values)
    return render_template("pages/enerji/potansiyel.html")
#endregion

#region ENERJI
@app.route("/dusme", methods=["GET","POST"])
def dusme():
    if request.method == "POST":
        yukseklik= request.form["yukseklik"]
        hiz = request.form["hiz"]
        g = request.form["g"]
        if hiz and yukseklik and g:
            hiz = float(hiz)
            yukseklik = float(yukseklik)
            g = float(g)
            sonhiz = math.sqrt(hiz * hiz + 2 * g * yukseklik)
            sure = (sonhiz - hiz) / g 
            sonhiz = float("{:.2f}".format(sonhiz))
            sure = float("{:.2f}".format(sure))
            results = {"sonhiz":sonhiz, "sure":sure}
            values = {"hiz":hiz,"yukseklik":yukseklik, "g":g}
            return render_template("pages/diger/dusme.html", results=results, values=values)
    return render_template("pages/diger/dusme.html")
#endregion

@app.route("/hakkinda", methods=["GET", "POST"])
def hakkinda():
    return render_template("pages/hakkinda.html")

@app.errorhandler(404)
def page_not_found(error):
    return (render_template('404.html'), 404)
