from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# -----------------------------
# LAB STATE
# -----------------------------
message = "Welcome to RITP College!"
defaced = False

# -----------------------------
# WEBSITE HTML
# -----------------------------
PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>RITP Security Lab</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #111;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* NORMAL WEBSITE */
        .normal-page {
            min-height: 100vh;
            text-align: center;
            padding-top: 80px;
        }

        .normal-page h1 {
            font-size: 42px;
        }

        .panel {
            width: min(700px, 90%);
            margin: 40px auto;
            padding: 30px;
            border: 1px solid #444;
            border-radius: 15px;
            background: #1b1b1b;
        }

        input {
            width: 70%;
            padding: 14px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
        }

        button {
            padding: 13px 20px;
            margin: 8px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
        }

        .publish {
            background: #2196f3;
            color: white;
        }

        .simulate {
            background: #b00020;
            color: white;
        }

        .restore {
            background: #2e7d32;
            color: white;
        }

        .notice {
            margin-top: 25px;
            padding: 20px;
            background: #222;
            border-radius: 10px;
        }

        /* DEFACEMENT SIMULATION */
        .hacked-page {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;

            background:
                radial-gradient(circle at center,
                #3a0000 0%,
                #120000 45%,
                #050000 100%);
        }

        .warning {
            font-size: 70px;
            margin: 0;
            font-weight: 900;
            letter-spacing: 3px;
            color: #ff2020;
            text-shadow:
                0 0 10px #ff0000,
                0 0 25px #ff0000;
        }

        .subtitle {
            font-size: 25px;
            color: #fff;
            margin: 20px;
        }

        .simulation {
            color: #ff7070;
            font-size: 16px;
            letter-spacing: 2px;
        }
    </style>
</head>

<body>

{% if defaced %}

    <!-- ================================= -->
    <!-- DEFACEMENT SIMULATION SCREEN -->
    <!-- ================================= -->

    <div class="hacked-page">

        <h1 class="warning">
            ⚠ THIS WEBSITE IS HACKED ⚠
        </h1>

        <p class="subtitle">
            RITP
        </p>

        <p class="simulation">
            SECURITY LAB — DEFACEMENT SIMULATION
        </p>

        <form method="POST">
            <button
                class="restore"
                name="action"
                value="restore">
                RESTORE WEBSITE
            </button>
        </form>

    </div>

{% else %}

    <!-- ================================= -->
    <!-- NORMAL WEBSITE -->
    <!-- ================================= -->

    <div class="normal-page">

        <h1>
            RITP College Portal
        </h1>

        <p>
            Cybersecurity Training Laboratory
        </p>

        <div class="panel">

            <h2>College Notice</h2>

            <form method="POST">

                <input
                    type="text"
                    name="message"
                    placeholder="Enter notice"
                    required
                >

                <br>

                <button
                    class="publish"
                    name="action"
                    value="notice">
                    PUBLISH NOTICE
                </button>

            </form>

            <div class="notice">

                <h3>Current Notice</h3>

                <div>
                    {{ message }}
                </div>

            </div>

            <hr>

            <h3>
                Security Testing
            </h3>

            <p>
                This button only performs a local
                defacement simulation.
            </p>

            <form method="POST">

                <button
                    class="simulate"
                    name="action"
                    value="deface">

                    RUN DEFACEMENT SIMULATION

                </button>

            </form>

        </div>

    </div>

{% endif %}

</body>
</html>
"""


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    global message
    global defaced

    if request.method == "POST":

        action = request.form.get("action")

        # Publish normal notice
        if action == "notice":

            message = request.form.get(
                "message",
                ""
            )

        # Start simulation
        elif action == "deface":

            defaced = True

        # Restore website
        elif action == "restore":

            defaced = False
            message = "Welcome to RITP College!"

    return render_template_string(
        PAGE,
        message=message,
        defaced=defaced
    )


# -----------------------------
# START SERVER
# -----------------------------
if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )