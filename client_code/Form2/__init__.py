from ._anvil_designer import Form2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form3")
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_3.url = "https://www.linkedin.com/in/abhijit-anil-9a409b15a"
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_4.url = "https://github.com/Lightning13"
    pass

