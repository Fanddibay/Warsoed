from warsoed import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False, unique=True)
    def __repr__(self):
        return f'{self.id}, {self.name}'

class Users(db.Model):
    id = db.Column(db.String(22), primary_key=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable =False)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    umkm = db.relationship('Umkm', backref='users', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.username}, {self.email}, {self.id_role}'

class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    umkm = db.relationship('Umkm', backref='village', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.name}'

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    umkm = db.relationship('Umkm', backref='seller', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.phone_number}'

class Umkm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    open = db.Column(db.Time, nullable=False)
    close = db.Column(db.Time, nullable=False)
    shipping_free = db.Column(db.Boolean, nullable=False)
    shipping_price = db.Column(db.Float, nullable=False)
    location_link = db.Column(db.String(75), nullable=False, unique=True)
    location_desc = db.Column(db.String(150), nullable=False, unique=True)
    picture =  db.Column(db.String(20), nullable = False, default = 'default.jpg')
    id_village = db.Column(db.Integer, db.ForeignKey('village.id'), nullable=False)
    id_seller = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    menu = db.relationship('Menu', backref='umkm', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.open}, {self.close}'


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    id_type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    id_umkm = db.Column(db.Integer, db.ForeignKey('umkm.id'), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.id_type}'


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    menu = db.relationship('Menu', backref='type', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.type}'