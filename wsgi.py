from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOCAL_PACKAGES = ROOT / ".deps"

if LOCAL_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_PACKAGES))

try:
    from flask import Flask, render_template
except ImportError as exc:  # pragma: no cover - user-facing bootstrap path
    raise SystemExit(
        "Flask is not installed. Run `python -m pip install --target .deps -r requirements.txt` "
        "and then rerun `python wsgi.py`."
    ) from exc


app = Flask(__name__, template_folder="pages", static_folder=".", static_url_path="")
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index() -> str:
    return render_template("index.html")


application = app


if __name__ == "__main__":
    print("Serving J-to-A Princeton at http://127.0.0.1:3000")
    print("Run: python wsgi.py")
    app.run(host="127.0.0.1", port=3000, debug=True)