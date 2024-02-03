from ._anvil_designer import Form3Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

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




