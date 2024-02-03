import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import io
import base64
@anvil.server.callable
def create_image_data(pixel_intensities):
    # Convert pixel intensities to grayscale image data
    max_intensity = max(max(row) for row in pixel_intensities)
    image_data = bytearray()

    for row in pixel_intensities:
        for intensity in row:
            # Scale intensity to 0-255 range
            scaled_intensity = int(intensity * 255 / max_intensity)
            image_data.extend((scaled_intensity,))

    # Encode the image data as base64
    return base64.b64encode(bytes(image_data)).decode()
  