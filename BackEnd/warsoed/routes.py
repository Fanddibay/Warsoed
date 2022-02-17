from warsoed import app
from warsoed.models import Village, Umkm
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/home')
def home():
    villages = Village.query.all()
    return render_template('home.html', title='Home', villages=villages)

@app.route('/location/<string:village>', methods=['GET'])
def location(village):
    umkms = Umkm.query.filter_by(id_village=Village.query.filter_by(name=village).first().id).all()
    return render_template('location.html', title=village, umkms=umkms, len=len)

@app.route('/detail/<int:umkm_id>')
def detail(umkm_id):
    umkm = Umkm.query.get_or_404(umkm_id)
    return render_template('detail.html', title=umkm.name, umkm=umkm)
