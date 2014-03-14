#
#    Simple GAE Database add/update example
#    Aurthor: Kevin Tu
#

import webapp2
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
        <form action="/" enctype="multipart/form-data" method="post">
            <div><label>keyname(*):</label></div>
            <div><input type="text" name="keyname" value=''></div>
            <div><label>name:</label></div>
            <div><input type="text" name="name" value=''></div>
            <div><label>value:</label></div>
            <div><input type="text" name="value" value=''></div>
            <div><input type="submit" value="submit" /></div>
        </form>
        </body>
        </html>""")

        success = self.request.get("success")
        if success :
            dbkeyname = self.request.get('keyname')
            dbname = self.request.get('name')
            dbvalue = self.request.get('value')
            self.response.out.write("<br/><b>Update DB success!</b><br/>")
            self.response.out.write("key_name=" + dbkeyname + "  name=" + dbname + "  value=" + dbvalue)

    def post(self):
        dbkeyname = self.request.get('keyname')
        dbname = self.request.get('name')
        dbvalue = self.request.get('value')

        getDB = testDB.get_by_key_name(dbkeyname)
        if getDB is not None :
            getDB.testDBname = dbname
            getDB.testDBvalue = dbvalue
            getDB.put()
        else:
            updateDb =  testDB (
                key_name = dbkeyname,
                testDBname = dbname,
                testDBvalue = dbvalue
            )
            updateDb.put()
        self.redirect("/?success=1&keyname=" + dbkeyname + "&name=" + dbname + "&value=" + dbvalue)

class testDB(db.Model):
	testDBname = db.StringProperty()
	testDBvalue = db.StringProperty()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
