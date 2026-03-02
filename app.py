from flask import Flask, render_template, request
import random

app = Flask(__name__)

messages = [
    """
    <div class="ai-box">
        <h2>🤖 Niveau trop élevé !</h2>
        <p>Je suis encore en formation intensive...</p>
        <a href="https://chat.openai.com" target="_blank" class="btn">
            🚀 Aller vers ChatGPT
        </a>
    </div>
    """,
    """
    <div class="ai-box">
        <h2>🧠 Mon cerveau chauffe...</h2>
        <p>Cette question mérite un expert !</p>
        <a href="https://chat.openai.com" target="_blank" class="btn">
            👑 Parler au mentor suprême
        </a>
    </div>
    """,
    """
    <div class="ai-box">
        <h2>🎮 Boss final débloqué !</h2>
        <p>Je préfère laisser la main au champion.</p>
        <a href="https://chat.openai.com" target="_blank" class="btn">
            ✨ Accéder au boss final
        </a>
    </div>
    """
]

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        response = random.choice(messages)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
