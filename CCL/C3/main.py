import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i = 0
        while i < 10:
            self.response.write("Name: Shraddha Pawar<br>")
            self.response.write("Seat Number: 33260<br>")
            self.response.write("Department: IT<br>")
            self.response.write('<br>')
            i += 1

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
