from flask import Flask, render_template
import selenium.webdriver as webdriver
import SearchResults2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/covidNews',  methods=['POST', 'GET'])
def newsApp():

    #return SearchResults2.get_results("Coronavirus Northern Ireland")
        return render_template('results-out.html', news = SearchResults2.get_results("Coronavirus Northern Ireland"),
                               description = SearchResults2.get_words("Coronavirus Northern Ireland"))



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
