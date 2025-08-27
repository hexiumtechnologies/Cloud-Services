from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

# sigma caching could be better
@app.after_request
def add_header(response):
    if 'static' in request.path:
        response.headers['Cache-Control'] = 'public, max-age=31536000'  # 1 year for static files
    return response

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/instances')
def instances():
    return render_template('instances.html', active_page='instances')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# serve static stuff correctly
@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)