from ._anvil_designer import Anvil_AboutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Anvil_About(Anvil_AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.
    # file = 'test_html_text.txt'
    # self.rich_text_2.content = anvil.server.call('read_about',file)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4")
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
    pass
