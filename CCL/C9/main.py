import webapp2
import requests

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome to the University Search App')

class SearchUniversitiesHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name', '')  # Get the university name from the query parameter

        # Make a GET request to the API with the provided university name
        response = requests.get(f"http://universities.hipolabs.com/search?name={name}")
        universities = response.json()  # Get the JSON response

        # Process the response and display the university information
        if universities:
            result = f"Found {len(universities)} universities matching '{name}':<br><br>"
            for university in universities:
                result += f"Name: {university['name']}<br>"
                result += f"Country: {university['country']}<br>"
                result += f"Website: {university['web_pages'][0]}<br><br>"
        else:
            result = f"No universities found matching '{name}'"

        self.response.write(result)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/search', SearchUniversitiesHandler)
], debug=True)
