from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmall import Marshmallow
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:///" + os.path.join(
    basedir, "app.sqlite"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SurvivorPerks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    teachable = db.Column(db.String(50), nullable=False)


class KillerPerks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    teachable = db.Column(db.String(50), nullable=False)


class Survivor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Killer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class survPerkSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "teachable")


class killPerkSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "teachable")


class survivorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


class killerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


surv_perk_schema = survPerkSchema()
surv_perks_schema = survPerkSchema(many=True)

kill_perk_schema = killPerkSchema()
kill_perks_schema = killPerkSchema(many=True)

survivor_schema = survivorSchema()
survivors_schema = survivorSchema(many=True)

killer_schema = killerSchema()
killers_schema = killerSchema(many=True)


# Survivor routes below
@app.route("/add-book", methods=["POST"])
def add_surv_perk():
    name = request.json["name"]
    description = request.json["description"]
    new_surv_perk = SurvPerk(
        name=name,
        description=description
    )
    db.session.add(new_book)
    db.session.commit()
    surv_perk = SurvPerk.query.get(new_surv_perk.id)
    return jsonify(message="Survivor perk added successfully")


@app.route("/survivor-perks", methods=["GET"])
def get_surv_perks():
    all_perks = SurvPerk.query.all()
    result = surv_perks_schema.dump(all_perks)
    return jsonify(result)


@app.route("/edit-survivor-perk/<id>", methods=["PATCH"])
def update_surv_perk(id):
    surv_perk = SurvPerk.query.get(id)
    name = request.json['name']
    description = request.json['description']


if __name__ == "__main__":
    app.debug = True
    app.run()
