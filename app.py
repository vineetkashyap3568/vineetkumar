from flask import Flask
import my_script  # Import your script

app = Flask(__name__)

@app.route("/run-script")
def run_script():
    result = my_script.run_script()  # Call the function from your script
    return f"<h1>{result}</h1>"  # Display the result in a simple HTML format

if __name__ == "__main__":
    app.run(debug=True)
