import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
def buy():
    """Buy shares of stock"""
    # User reached route via POST (submitting form)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares")

        # Get symbol and shares
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))

        # Get stock price
        price = lookup(symbol)
        if not price:
            return apology("symbol not found")

        # Get user ID
        user_id = session["user_id"]

        # Calculate total cost
        total_cost = price * shares

        # Ensure user has enough cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        if cash < total_cost:
            return apology("not enough cash")

        # Update user's cash
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Add transaction to history
        db.execute("INSERT INTO transactions (user_id, type, symbol, price, shares, time) VALUES (?, ?, ?, ?, ?, ?)",
                    user_id, "BUY", symbol, price, shares, datetime.datetime.utcnow())

        # Redirect user to portfolio page
        return redirect("/portfolio")

    # User reached route via GET (showing form)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please enter a symbol!")
        item = lookup(symbol)

        if not item:
            return apology("Invalid Symbol!")
        return render_template("quoted.html", item=item, usd_function=usd)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("username is required!")
        elif not password:
            return apology("password is required!")
        elif not confirmation:
            return apology("confirmation is required!")

        if password != confirmation:
            return apology("passwords do not match")

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO USERS (username, hash) values (?, ?)", username, hash)
            return redirect("/")
        except:
            return apology("Username has already been registered!")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
def sell():
    """Sell shares of stock"""
    # User reached route via POST (submitting form)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares")

        # Get symbol and shares
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))

        # Get stock price
        price = lookup(symbol)
        if not price:
            return apology("symbol not found")

        # Get user ID
        user_id = session["user_id"]

        # Get number of shares owned
        owned_shares = db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", user_id, symbol)[0]["shares"]

        # Ensure user owns enough shares
        if shares > owned_shares:
            return apology("not enough shares")

        # Calculate total proceeds
        total_proceeds = price * shares

        # Update user's cash
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_proceeds, user_id)

        # Update portfolio
        db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, user_id, symbol)

        # Add transaction to history
        db.execute("INSERT INTO transactions (user_id, type, symbol, price, shares, time) VALUES (?, ?, ?, ?, ?, ?)",
                    user_id, "SELL", symbol, price, -shares, datetime.datetime.utcnow())

        # Redirect user to portfolio page
        return redirect("/portfolio")@app.route("/buy", methods=["GET", "POST"])
