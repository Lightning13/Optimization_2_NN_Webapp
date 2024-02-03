from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import base64


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file is None:
        self.text_test.text = "No file uploaded"
    elif file.name.endswith('.csv'):
        self.text_test.text = "CSV file uploaded. Processing..."

        # pixel_intensities = anvil.server.call('process_csv', file)
        # # Convert the pixel intensities to base64-encoded image data
        # image_data = anvil.server.call('create_image_data',pixel_intensities)

        # # Set the source of the image component to the base64-encoded image data
        # # self.image_1.source = anvil.BlobMedia(content=bytes(image_data, 'utf-8'), content_type='image/png')

        # self.image_1.source = 'https://drive.google.com/file/d/1UkH_oeokSDxOd2D5Xx8rV2c5hpyLiKxt/view?usp=sharing'
        self.image_1.source = anvil.server.call('process_csv', file)
        self.text_test.text = "Processed"
    else:
        self.text_test.text = "Please upload a CSV file"

   
  pass      

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_test.text = anvil.server.call(str('sum_1'))
    pass
