from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Folder with precomputed JSON plots
JSON_FOLDER = os.path.join(os.getcwd(), "data")

# Helper function to load all JSON files
def load_json_plot(filename):
    with open(os.path.join(JSON_FOLDER, filename), "r") as f:
        return json.load(f)

@app.route("/")
def index():
    # Load EDA plots
    eda_scatter = load_json_plot("eda_scatter.json")
    eda_hist = load_json_plot("eda_glucose_hist.json")
    eda_corr = load_json_plot("eda_correlation.json")
    eda_box = load_json_plot("eda_box_age.json")

    # Load model metrics
    metrics_bar = load_json_plot("metrics_bar.json")

    # Load confusion matrices
    cm_logreg = load_json_plot("cm_logreg.json")
    cm_xgb = load_json_plot("cm_xgb.json")
    cm_mlp = load_json_plot("cm_mlp.json")

    # Load feature importance
    fi_lr = load_json_plot("feature_importance_lr.json")
    fi_xgb = load_json_plot("feature_importance_xgb.json")

    return render_template(
        "index.html",
        eda_scatter=eda_scatter,
        eda_hist=eda_hist,
        eda_corr=eda_corr,
        eda_box=eda_box,
        metrics_bar=metrics_bar,
        cm_logreg=cm_logreg,
        cm_xgb=cm_xgb,
        cm_mlp=cm_mlp,
        fi_lr=fi_lr,
        fi_xgb=fi_xgb
    )

if __name__ == "__main__":
    app.run(debug=True)