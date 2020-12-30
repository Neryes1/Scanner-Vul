from app import app

# definindo rota
@app.route("/")
def index():
  return "Oi"