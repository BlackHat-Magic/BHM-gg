from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def home():
	return(render_template("home/index.html"))

@app.route("/twitch")
def twitch():
	return(redirect("https://www.twitch.tv/blackhat_magic", 301))

@app.route("/ttv")
def ttv():
	return(redirect("https://www.twitch.tv/blackhat_magic", 301))

@app.route("/youtube")
def youtube():
	return(redirect("https://www.youtube.com/c/BlackHatMagic", 301))

@app.route("/yt")
def yt():
	return(redirect("https://www.youtube.com/c/BlackHatMagic", 301))

@app.route("/twitter")
def twitter():
	return(redirect("https://www.twitter.com/Black_HatMagic", 301))

@app.route("/twt")
def twt():
	return(redirect("https://www.twitter.com/Black_HatMagic", 301))

@app.route("/t")
def t():
	return(redirect("https://www.twitter.com/Black_HatMagic", 301))

@app.route("/github")
def github():
	return(redirect("https://www.github.com/BlackHat-Magic", 301))

@app.route("/gitlab")
def gitlab():
	return("Well aren't you a nosy one? Gitlab coming soon (tm).")

@app.route("/git")
def git():
	return(redirect("https://www.github.com/BlackHat-Magic", 301))

@app.route("/reddit")
def reddit():
	return(redirect("https://www.reddit.com/u/BlackHatMagic1545", 301))

@app.route("/email")
def email():
	return(redirect("mailto:BlackHatMagic@gmail.com", 301))

@app.route("/mail")
def mail():
        return(redirect("mailto:BlackHatMagic@gmail.com", 301))

@app.route("/discord")
def discord():
	return(redirect("https://discord.gg/dqSusZqenq", 301))

@app.route("/discord-profile")
def discordProfile():
	return(redirect("https://discord.com/users/272197511769227264", 301))

@app.route("/steam")
def steam():
	return(redirect("https://steamcommunity.com/id/Black_Hat_Magic/", 301))

if(__name__ == "__main__"):
	app.run(debug=True)
