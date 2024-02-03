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
            self.df = anvil.server.call('import_csv_data', file)
            
            img_bytes = anvil.server.call('classify_image', file)
    
            # Check if img_bytes is already bytes-like
            if isinstance(img_bytes, bytes):
                # Display the image on the webpage
                image_source = 'data:image/png;base64,' + base64.b64encode(img_bytes).decode('utf-8')
                self.image_1.source = image_source  # Assuming 'image_1' is the name of your Image component
            else:
                self.text_test.text = "Error: Invalid image bytes"
        else:
            self.text_test.text = "Please upload a CSV file"
          
  pass      

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_test.text = anvil.server.call(str('sum_1'))
    pass
