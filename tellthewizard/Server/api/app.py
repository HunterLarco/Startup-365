"""
' DRIVERS
"""
import webapp2






class TwilioHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    
    sender = self.request.get('From')
    body = self.request.get('Body').strip()
    
    self.response.out.write('YOU SAID\n\n\n'+body)
  
  
  
  

  
app = webapp2.WSGIApplication([('/api/twilio/?', TwilioHandler)], debug=True)