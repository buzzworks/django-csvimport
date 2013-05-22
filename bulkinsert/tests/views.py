from django.http import HttpResponse

def index(request, template='README.txt', **kwargs):
    return HttpResponse ('''<html><body><h1>django-bulkinsert Test app</h1>
                  <p>You have installed the test django-bulkinsert 
                  application. Click on the <a href="/admin/">admin</a> 
                  to try it</p>
                  <p>NB: you must run<br /> 
                     django-admin.py syncdb --settings=bulkinsert.tests.settings <br />
                  first to create the test models. 
                  <p>Click on bulkinsert in the admin</p>
                  <p>Try importing data via the test csv files in
                     django-bulkinsert/bulkinsert/tests/fixtures folder</p>
                  <p>Click on Add bulkinsert</p>
                  <p>For example select Models name: tests.Country and upload the countries.csv file</p>
                  </body></html>''')
