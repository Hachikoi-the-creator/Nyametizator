from flask import Flask, render_template, url_for, request

app = Flask(__name__)


def word_changer(word):
    cast_list = word.split()
    vowels = ["a", "e", "i", "o", "u"]
    result = ""

    for word in cast_list:
        if len(word) < 3:
            result += word + "-h"
        else:
            if word[0].lower() in vowels:
                result += word + "-nya"
            else:
                result += word + "-nyo"
        # separate the words
        result += " "
    return result


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        original_text = request.form["original"]
        print(original_text)
        new_url = word_changer(original_text)
        return render_template(
            "index.html", original_text=original_text, output_text=new_url
        )

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
# debug is set to false which was true and also not hosting port was specified....all these are done just for hosting purposes so change it with change in needs.
