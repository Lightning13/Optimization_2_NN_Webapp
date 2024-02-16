from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
  
    file = 'test_html_text_2.txt'
    self.rich_text_2.content = anvil.server.call('read_about',file)

    
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form2")
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form3")
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("CNN_About")
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Transformer_About")
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Anvil_About")
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_4.url = "https://medium.com/@abhijitanil.2/unleashing-the-power-of-convolutional-neural-networks-a-comparative-exploration-of-tensorflow-and-86a70879d3ad"
    pass
