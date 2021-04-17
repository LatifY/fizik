from flask import Flask, url_for, render_template, request, redirect, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    return render_template('index.html')

#region BASINC
@app.route("/kati-basinci", methods=["GET","POST"])
def kati():
    if request.method == "POST":
        kuvvet = request.form["kuvvet"]
        alan = request.form["alan"]
        if kuvvet and alan:
            kuvvet = float(kuvvet)
            alan = float(alan)
            result = kuvvet/alan
            values = {"kuvvet":kuvvet,"alan":alan}
            return render_template("pages/basinc/kati.html", result=result, values=values)
    return render_template("pages/basinc/kati.html")

@app.route("/sivi-basinci", methods=["GET","POST"])
def sivi():
    if request.method == "POST":
        derinlik = request.form["derinlik"]
        ozkutle = request.form["ozkutle"]
        ivme = request.form["ivme"]
        if derinlik and ozkutle and ivme:
            derinlik = float(derinlik)
            ozkutle = float(ozkutle)
            ivme = float(ivme)
            result = derinlik * ozkutle * ivme
            values = {"derinlik":derinlik,"ozkutle":ozkutle, "ivme":ivme}
            return render_template("pages/basinc/sivi.html", result=result, values=values)
    return render_template("pages/basinc/sivi.html")

@app.route("/gaz-basinci", methods=["GET","POST"])
def gaz():
    if request.method == "POST":
        hacim = request.form["hacim"]
        sicaklik = request.form["sicaklik"]
        tanecik = request.form["tanecik"]
        if hacim and sicaklik and tanecik:
            hacim = float(hacim)
            sicaklik = float(sicaklik)
            tanecik = float(tanecik)
            result = sicaklik / hacim * tanecik *8.3145
            values = {"hacim":hacim,"sicaklik":sicaklik, "tanecik":tanecik}
            return render_template("pages/basinc/gaz.html", result=result, values=values)
    return render_template("pages/basinc/gaz.html")
#endregion

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
#endregion

#region OPTIK
@app.route("/isik-akisi", methods=["GET","POST"])
def aki():
    if request.method == "POST":
        siddet = request.form["siddet"]
        if siddet:
            siddet = float(siddet)
            result = 4 * 3.14 * siddet
            values = {"siddet":siddet}
            return render_template("pages/optik/aki.html", result=result, values=values)
    return render_template("pages/optik/aki.html")

@app.route("/ortalama-aydinlanma-siddeti", methods=["GET","POST"])
def ortalama():
    if request.method == "POST":
        aki = request.form["aki"]
        alan = request.form["alan"]
        if aki and alan:
            aki = float(aki)
            alan = float(alan)
            result = aki/alan
            values = {"aki":aki,"alan":alan}
            return render_template("pages/optik/ortalama.html", result=result, values=values)
    return render_template("pages/optik/ortalama.html")

@app.route("/noktasal-aydinlanma-siddeti", methods=["GET","POST"])
def noktasal():
    if request.method == "POST":
        siddet = request.form["siddet"]
        mesafe = request.form["mesafe"]
        if siddet and mesafe:
            siddet = float(siddet)
            mesafe = float(mesafe)
            result = siddet / (mesafe**2)
            values = {"siddet":siddet,"mesafe":mesafe}
            return render_template("pages/optik/noktasal.html", result=result, values=values)
    return render_template("pages/optik/noktasal.html")
#endregion

@app.route("/gezegenlerde-agirlik", methods=["GET","POST"])
def agirlik():
    if request.method == "POST":
        kutle = request.form["kutle"]
        if kutle:
            kutle = float(kutle)
            dunya = round(kutle * 9.8,2)
            merkur = round(kutle * 3.7,2)
            mars = round(kutle * 3.72,2)
            saturn = round(kutle * 10.44,2)
            uranus = round(kutle * 8.87,2)
            venus = round(kutle * 8.87,2)
            neptun = round(kutle * 11.15,2)
            jupiter = round(kutle * 24.79,2)
            values = {"kutle":kutle}
            planets = {"Merkür":merkur, "Venüs":venus, "Dünya":dunya, "Mars":mars, "Jüpiter":jupiter, "Satürn":saturn, "Uranüs":uranus, "Neptün":neptun}
            return render_template("pages/uzay/agirlik.html", planets=planets, values=values)
    return render_template("pages/uzay/agirlik.html")



@app.errorhandler(404)
def page_not_found(error):
    return (render_template('404.html'), 404)
