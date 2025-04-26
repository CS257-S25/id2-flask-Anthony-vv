from flask import Flask
from ProductionCode import covid_stats

app = Flask(__name__)
"""This is the main text for the Flask application, it wil provide the user information for formatting and an example"""
@app.route('/')
def homepage():
    return (
        "Welcome to my ID2 Application!\n\n"
        "Here you can compare COVID-19 stats for multiple countries using one date:\n"
        "Please use this format:\n"
        "/compare/date/ country1, country2.\n\n"
        "The date should be in the format YYYY-MM-DD.\n"
        "\nExample:\n"
        "/compare/2020-04-19/US,GB"
    )
    """"def compare_invalid_date(self):"""
@app.route('/compare/<date>/<countries>')
def compare(date, countries):
    """This function compares COVID-19 stats for multiple countries using one date"""
    try:
        output = f"COVID-19 data for {date}:\n"
        for country in countries.split(','):
            cases, deaths = covid_stats.stats(country, date, date)
            output += f"{country}: Cases={cases}, Deaths={deaths}\n"
        return output
    except (ValueError, KeyError) as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
