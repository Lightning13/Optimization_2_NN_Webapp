# %%
import anvil.server
import pandas as pd
from PIL import Image
import numpy as np
import tensorflow as tf
import io
from io import StringIO
from io import BytesIO
from PIL import Image
import numpy as np
import keras
from keras.models import load_model
import torchvision.transforms as transforms
import torch
from torch import nn




# %%
anvil.server.connect("YOUR-KEY-HERE")

# %%
@anvil.server.callable
def read_about(file_name):
    with open(file_name, 'r',encoding='utf-8') as file:
    # Read the entire contents of the file
        text = file.read()
        return text


# %%
import tensorflow as tf

class ClassToken(tf.keras.layers.Layer):
    def __init__(self, **kwargs):  
        super(ClassToken, self).__init__(**kwargs)

    def build(self, input_shape):
        w_init = tf.random_normal_initializer()
        self.w = self.add_weight(
            shape=(1, 1, input_shape[-1]), 
            initializer=w_init,
            trainable=True,
            name='cls_token'  
        )

    def call(self, inputs):
        batch_size = tf.shape(inputs)[0]
        hidden_dim = self.w.shape[-1]
        cls = tf.broadcast_to(self.w, [batch_size, 1, hidden_dim])
        return tf.cast(cls, dtype=inputs.dtype)

model_path = 'ViT_validationAcc9867.h5'  # Path to your model file
model_transformer = tf.keras.models.load_model(model_path, custom_objects={'ClassToken': ClassToken})

# %%
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv_layer = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        self.fc_layer = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(128 * 3 * 3, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 10)
        )
        
    def forward(self, x):
        x = self.conv_layer(x)
        x = x.view(x.size(0), -1)  # Flatten the layer
        x = self.fc_layer(x)
        return x
    
model_cnn_pytorch = CNN()
model_cnn_pytorch.load_state_dict(torch.load('mnist_cnn_model.pth', map_location=torch.device('cpu')))

# %%
# Load the model
model_cnn_tensorflow = load_model('model_cnn_tf_3')

# %%
def predict_class(np_data,id):
    if id == 1:

        if np.max(np_data) > 1:
                np_data = np_data / 255.0

        x_test_ravel = np.zeros((1,49,16))
        for img in range(1):
            ind = 0
            for row in range(7):
                for col in range(7):
                    x_test_ravel[img, ind, :] = np_data[(row * 4):((row + 1) * 4), (col * 4):((col + 1) * 4)].ravel()
                    ind += 1

        pos_feed = np.array([list(range(49))]*1)
        predicted_output = model_transformer.predict([x_test_ravel,pos_feed])
        predicted_class = np.argmax(predicted_output)
        # max_probability = np.max(predicted_output)
        return predicted_class,str(98.85)
    
    elif id ==2:
        # transform = transforms.Compose([
        #     transforms.ToTensor(),
        #     transforms.Normalize((0.5,), (0.5,))
        # ])

        if np.max(np_data) <= 1:
            np_data = np_data * 255.0
        
        image = torch.tensor(np_data, dtype=torch.float32).reshape(1, 1, 28, 28)  # Reshape to match input shape (batch_size, channels, height, width)

        # Perform inference
        model_cnn_pytorch.eval()
        with torch.no_grad():
            output = model_cnn_pytorch(image)

        # Interpret the prediction
        predicted_class = torch.argmax(output, dim=1).item()
        # prob = torch.max(output, dim=1)
        return predicted_class,str(99)
    
    elif id ==3:
        array_float = np_data.reshape(1,28,28,1)
        # array_float = np.expand_dims(np_data, axis=0)

        if np.max(np_data) > 1:
            array_float = array_float / 255.0
        
        output = model_cnn_tensorflow.predict(array_float)
        predicted_class = np.argmax(output)
        return predicted_class, str(99.39)

# %%
@anvil.server.callable
def validate_file(file):
    # Read CSV data into a DataFrame
    csv_content = file.get_bytes().decode('utf-8')
    df = pd.read_csv(StringIO(csv_content), header=None)

    df_np = np.array(df)
    
    # Check dimensions
    if df_np.shape != (28, 28):
        return 1 # Array dimensions are not 28x28

    # Check if all elements are numbers
    try:
        np.all(np.isfinite(df_np))
    except TypeError:
        return 2 # Array contains non-numeric values
    
    if not np.all((df_np >= 0) & (df_np <= 255)):
        return 3 # Array contains values outside the range [0, 255]

    return 4 # Array is 28x28 and contains only numbers"

# %%
@anvil.server.callable
def display_image(file):
    # Read CSV data into a DataFrame
    csv_content = file.get_bytes().decode('utf-8')
    df = pd.read_csv(StringIO(csv_content), header=None)

    df_np = np.array(df)

    if np.max(df_np) <= 1:
            df_np = df_np * 255.0
            
    img = Image.fromarray(df_np.astype('uint8'))

    # Convert image to bytes
    img_bytes = BytesIO()
    name = 'img'
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    return anvil.BlobMedia("image/png",img_bytes,name = name),df_np

# %%

@anvil.server.callable
def process_csv(df_np,id):
    
    df_np = np.array(df_np)
    predicted_class,probability = predict_class(df_np,id)


    return predicted_class,probability

# %%
anvil.server.wait_forever()


