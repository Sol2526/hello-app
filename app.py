from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a form and greeting logic
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Hello App</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="submit" value="Submit">
    </form>
    {% if name %}
        <h2>Hello {{ name }}. Congrats! You understand how to use Docker.</h2>
        <h2>Hello {{ name }}. This is V2</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
