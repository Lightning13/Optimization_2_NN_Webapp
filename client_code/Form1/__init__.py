from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import base64


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.button_2.visible = False
    # Any code you write here will run before the form opens.

  def uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file is None:
        self.status_text.text = "No file uploaded"
    elif file.name.endswith('.csv'):
        self.status_text.text = "CSV file uploaded. Processing..."
        # pixel_intensities = anvil.server.call('process_csv', file)
        # # Convert the pixel intensities to base64-encoded image data
        # image_data = anvil.server.call('create_image_data',pixel_intensities)

        # # Set the source of the image component to the base64-encoded image data
        # # self.image_1.source = anvil.BlobMedia(content=bytes(image_data, 'utf-8'), content_type='image/png')

        # self.image_1.source = 'https://drive.google.com/file/d/1UkH_oeokSDxOd2D5Xx8rV2c5hpyLiKxt/view?usp=sharing'
        self.image_1.source = anvil.server.call('process_csv', file)
        self.uploader.visible = False
        self.status_text.text = "Processed"
        self.button_2.visible = True
    else:
        self.status_text.text = "Wrong file type. Please upload a CSV file"
        self.uploader.clear()
        self.uploader.text = "Re-Upload"

    pass      

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.status_text.text = anvil.server.call(str('sum_1'))
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form2")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form3")
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.uploader.clear()
    self.image_1.source = "_/theme/RNN_Tutorial.avif"
    self.uploader.visible = True
    self.button_2.visible = False
    self.status_text.text = "Ready for new file"
    pass
