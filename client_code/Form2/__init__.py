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

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_7.url = "https://www.linkedin.com/in/abhijit-anil-9a409b15a"
    pass

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_6.url = "https://www.linkedin.com/in/biyunyuan/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app"
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_3.url = "https://www.linkedin.com/in/rahull-borana/"
    pass

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form4")
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_4.url = "https://linkedin.com/in/kkarthick12"
    pass

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_5.url = "https://www.linkedin.com/in/hayoung-kim-840682b5/"
    pass

