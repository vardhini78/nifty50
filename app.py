from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if 'year' in request.form:
        year = int(request.form['year'])
        january = float(request.form['january'])
        february = float(request.form['february'])
        march = float(request.form['march'])
        april = float(request.form['april'])
        may = float(request.form['may'])
        june = float(request.form['june'])
        july = float(request.form['july'])
        august = float(request.form['august'])
        september = float(request.form['september'])
        october = float(request.form['october'])
        november = float(request.form['november'])
        december = float(request.form['december'])
        
        annual_total = january + february + march + april + may + june + july + august + september + october + november + december
        
        return render_template('index.html', year=year, annual_total=annual_total)
    else:
        return jsonify({'error': 'Year not provided'})

if __name__ == '__main__':
    app.run(debug=True)
