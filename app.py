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
    url = db.column(db.string(100), nullable=False)


class Killer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)


class survPerkSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "teachable")


class killPerkSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "teachable")


class survivorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "url")


class killerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "url")


surv_perk_schema = survPerkSchema()
surv_perks_schema = survPerkSchema(many=True)

kill_perk_schema = killPerkSchema()
kill_perks_schema = killPerkSchema(many=True)

survivor_schema = survivorSchema()
survivors_schema = survivorSchema(many=True)

killer_schema = killerSchema()
killers_schema = killerSchema(many=True)


# Survivor perk routes below
@app.route("/add-survivor-perk", methods=["POST"])
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


@app.route("/edit-survivor-perk/<id>", methods=["PUT"])
def update_surv_perk(id):
    surv_perk = SurvPerk.query.get(id)
    name = request.json['name']
    description = request.json['description']
    surv_perk.name = name
    surv_perk.description = description
    return jsonify(message="Successful edit")


@app.route("/delete-survivor-perk/<id>", methods=["DELETE"])
def delete_surv_perk(id):
    surv_perk = SurvPerk.query.get(id)
    db.session.delete(surv_perk)
    db.session.commit()
    return jsonify(message="Survivor perk deleted successfully")

# Survivor character routes


@app.route("/add-survivor", methods=["POST"])
def add_survivor():
    name = request.json["name"]
    url = request.json["url"]
    new_survivor = Survivor(
        name=name,
        url=url
    )
    db.session.add(new_survivor)
    db.session.commit()
    survivor = Survivor.query.get(new_survivor.id)
    return jsonify(message="Survivor successfully added")


@app.route("/survivors", methods=["GET"])
def get_survivors():
    all_survivors = Survivor.query.all()
    result = survivors_schema.dump(all_survivors)
    return jsonify(result)


@app.route("/edit-survivor/<id>", methods=["PUT"])
def update_survivor(id):
    survivor = survivor.query.get(id)
    name = request.json['name']
    url = request.json['url']
    survivor.name = name
    survivor.url = url
    return jsonify(message="Successful edit")


@app.route("/delete-survivor/<id>", methods=["DELETE"])
def delete_survivor(id):
    survivor = Survivor.query.get(id)
    db.session.delete(surivor)
    db.session.commit()
    return jsonify(message="Survivor deleted successfully")

# Killer character routes


@app.route("/add-killer", methods=["POST"])
def add_killer():
    name = request.json["name"]
    url = request.json["url"]
    new_killer = Killer(
        name=name
        url=url
    )
    db.session.add(new_killer)
    db.session.commit()
    killer = Killer.query.get(new_killer.id)
    return jsonify(message="Killer successfully added")


@app.route("/killers", methods=["GET"])
def get_killers():
    all_killers = Killer.query.all()
    result = survivors_schema.dump(all_killers)
    return jsonify(result)


@app.route("/edit-killer/<id>", method=["PUT"])
def update_killer(id):
    killer = killer.query.get(id)
    name = request.json["name"]
    url = request.json["url"]
    killer.name = name
    killer.url = url
    return jsonify("Successful edit")


if __name__ == "__main__":
    app.debug = True
    app.run()
