from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.user import User

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            username=username,
            email=email
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth_bp.register"))

    return render_template("register.html")
