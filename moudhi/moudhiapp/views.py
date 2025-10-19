from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def myname_view (request):
    name = "moudhi"
    student_id = 2191121581
    return HttpResponse (f"""
    <html>
     <body>
      <h1> my name {name}!</h1>
      <h1> {student_id}</h1>
     </body>
    </html>
    <img src="https://camo.githubusercontent.com/c651b6c56785009595481d122b4432c670a0a0b832042cc1b66062638e57c6e3/68747470733a2f2f6f726465726f66707265616368657273696e646570656e64656e742e6f72672f77702d636f6e74656e742f75706c6f6164732f323031372f30392f6865792d796f752d6765742d746f2d776f726b2e6a7067">
    """)



def myclasses_view(request):
    myclasses = ()
    return HttpResponse (f"""
    <html>
     <ul>
     <li>math</li>
     <li>history</li>
     <li>english</li>
     </ul>
    </html>
    """)


