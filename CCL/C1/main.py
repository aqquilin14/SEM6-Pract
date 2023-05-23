import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('hello')

app = webapp2.WSGIApplication([('/',MainPage)], debug=True)


#python <path_to_sdk>/bin/devappserver.py <path_to_application_directory>
