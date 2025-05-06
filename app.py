<<<<<<< HEAD
=======
"""Flask application for comparing COVID-19 statistics for multiple countries on a given date."""

>>>>>>> f5cac13693667ac146363aafa85d9e7301bfef52
from flask import Flask
from ProductionCode import covid_stats

app = Flask(__name__)
<<<<<<< HEAD
"""This is the main text for the Flask application, it wil provide the user information for formatting and an example"""
@app.route('/')
def homepage():
=======

@app.route('/')
def homepage():
    """Display instructions for how to use the COVID-19 comparison endpoint."""
>>>>>>> f5cac13693667ac146363aafa85d9e7301bfef52
    return (
        "Welcome to my ID2 Application!\n\n"
        "Here you can compare COVID-19 stats for multiple countries using one date:\n"
        "Please use this format:\n"
<<<<<<< HEAD
        "/compare/date/ country1, country2.\n\n"
=======
        "/compare/date/country1,country2\n\n"
>>>>>>> f5cac13693667ac146363aafa85d9e7301bfef52
        "The date should be in the format YYYY-MM-DD.\n"
        "\nExample:\n"
        "/compare/2020-04-19/US,GB"
    )
<<<<<<< HEAD
    """"def compare_invalid_date(self):"""
@app.route('/compare/<date>/<countries>')
def compare(date, countries):
    """This function compares COVID-19 stats for multiple countries using one date"""
=======

@app.route('/compare/<date>/<countries>')
def compare(date, countries):
    """Compare COVID-19 stats for the given countries on the specified date."""
>>>>>>> f5cac13693667ac146363aafa85d9e7301bfef52
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
