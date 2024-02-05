from ._anvil_designer import Form3Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
# Add these imports to your form
from anvil.js.window import jQuery
from anvil.js import get_dom_node

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Set the latitude and longitude of the map to the desired location
    self.map_1.center = GoogleMap.LatLng(30.284215739792057, -97.73782819066138)
    self.map_1.zoom = 20
    marker = GoogleMap.Marker(
    animation=GoogleMap.Animation.DROP,
    position=GoogleMap.LatLng(30.284215739792057, -97.73782819066138)
    )
    self.map_1.add_component(marker)

   # Create an iframe element and set the src
    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src","https://news.utexas.edu/")
    # Append the iframe to a container in our form
    iframe.appendTo(get_dom_node(self.content_panel))
    js.call_js('window.open', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form2")
    pass

  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass

  def map_1_show(self, **event_args):
    """This method is called when the GoogleMap is shown on the screen"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    test = anvil.server.call('read_about')
    print(test)
    self.rich_text_1.content = anvil.server.call(str('read_about'))
    pass




