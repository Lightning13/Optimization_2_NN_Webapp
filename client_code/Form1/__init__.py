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
  gv_data = []
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_2.visible = False
    self.button_3.visible = False
    self.button_4.visible = False
    self.button_5.visible = False
    self.button_1.visible = False
    self.label_4.text ='Please upload a 28 x 28 csv file'
    # Any code you write here will run before the form opens.

  def uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file is None:
        self.status_text.text = "No file uploaded"
    elif file.name.endswith('.csv'):
        validate = anvil.server.call('validate_file', file)
        if validate == 4:
          self.status_text.text = "CSV file uploaded. Awaiting Model Selection"
          #Process the image
          self.image_1.source, self.gv_data = anvil.server.call('display_image', file)
          self.label_4.text ='File converted to image'
          self.uploader.visible = False
          self.rich_text_2.visible = False
          self.button_3.visible = True
          self.button_4.visible = True
          self.button_5.visible = True
          self.button_1.visible = True
          self.rich_text_1.content = 'Which Model would you like to try?'
        elif validate == 1:
          self.status_text.text = "File is not 28 x 28. Please upload a valid file"
          alert("File is not 28 x 28. Please upload a valid file")
          self.uploader.clear()
          self.uploader.text = "Re-Upload"
        elif validate == 2:
          self.status_text.text = "File contains non-numeric values"
          alert("File contains non-numeric values")
          self.uploader.clear()
          self.uploader.text = "Re-Upload"
        elif validate == 3:
          self.status_text.text = "File contains values outside the range [0, 255]"
          alert("File contains values outside the range [0, 255]")
          self.uploader.clear()
          self.uploader.text = "Re-Upload"
    else:
        self.status_text.text = "Wrong file type. Please upload a CSV file"
        alert("Wrong file type. Please upload a CSV file")
        self.uploader.clear()
        self.uploader.text = "Re-Upload"

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
    self.label_3.text = ''
    self.label_5.text = ''
    self.label_6.text = ''
    # self.label_2.text = ''
    self.image_1.source = "_/theme/SvckSy7fFviqrq8ClF.gif"
    self.uploader.visible = True
    self.rich_text_2.visible = True
    self.label_4.visible = True
    self.button_2.visible = False
    self.status_text.text = "Ready for new file"
    self.label_4.text ='Please upload a 28 x 28 csv file'
    self.rich_text_1.content = ''

    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form4")
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.status_text.text = "CNN (PyTorch) model running"
    predicted_class,class_probability = anvil.server.call('process_csv', self.gv_data,2)
    #Hide/Unhide buttons
    self.uploader.visible = False
    self.rich_text_2.visible = False
    self.label_4.visible = False
    self.status_text.text = "Processed"
    self.label_3.text = 'Class: '+str(predicted_class)
    # self.label_2.text = 'Model Accuracy: '+str(class_probability)
    self.button_2.visible = True

    self.rich_text_1.content = 'CNN (PyTorch) Model Performance'
    self.button_3.visible = False
    self.button_4.visible = False
    self.button_5.visible = False
    self.button_1.visible = False
  
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.status_text.text = "Transformer model running"
    predicted_class,class_probability = anvil.server.call('process_csv', self.gv_data,1)
    #Hide/Unhide buttons
    self.uploader.visible = False
    self.rich_text_2.visible = False
    self.label_4.visible = False
    self.status_text.text = "Processed"
    self.label_3.text = 'Class: '+str(predicted_class)
    # self.label_2.text = 'Model Accuracy: '+str(class_probability)
    self.button_2.visible = True

    self.rich_text_1.content = 'Transformer Model Performance'
    self.button_3.visible = False
    self.button_4.visible = False
    self.button_5.visible = False
    self.button_1.visible = False
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.status_text.text = "CNN (TensorFlow) model running"
    predicted_class,class_probability = anvil.server.call('process_csv', self.gv_data,3)
    #Hide/Unhide buttons
    self.uploader.visible = False
    self.rich_text_2.visible = False
    self.label_4.visible = False
    self.status_text.text = "Processed"
    self.label_3.text = 'Class: '+str(predicted_class)
    # self.label_2.text = 'Model Accuracy: '+str(class_probability)
    self.button_2.visible = True

    self.rich_text_1.content = 'CNN (Tensorflow) Model Performance'
    self.button_3.visible = False
    self.button_4.visible = False
    self.button_5.visible = False
    self.button_1.visible = False
    gv_data = []
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_4.url = 'https://github.com/Lightning13/Optimization_2_NN_Webapp/tree/c76500fd0910e93eafdc8ac3880fde30c6d767fb/test_files'
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.status_text.text = "All models running"
    predicted_class_2,class_probability = anvil.server.call('process_csv', self.gv_data,2)
    predicted_class_1,class_probability = anvil.server.call('process_csv', self.gv_data,1)
    predicted_class_3,class_probability = anvil.server.call('process_csv', self.gv_data,3)
    #Hide/Unhide buttons
    self.uploader.visible = False
    self.rich_text_2.visible = False
    self.label_4.visible = False
    self.status_text.text = "Processed"
    self.label_3.text = 'CNN (PyTorch) Class: '+str(predicted_class_2)
    self.label_5.text = 'Transformer Class: '+str(predicted_class_1)
    self.label_6.text = 'CNN (TensorFlow) Class: '+str(predicted_class_3)
    # self.label_2.text = 'Model Accuracy: '+str(class_probability)
    self.button_2.visible = True

    self.rich_text_1.content = 'All Models Performance'
    self.button_3.visible = False
    self.button_4.visible = False
    self.button_5.visible = False
    self.button_1.visible = False
    pass



