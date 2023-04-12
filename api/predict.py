from theyyam.settings import MODEL as model
from theyyam.settings import LABEL_ENCODER as label_encoder
import cv2
import numpy as np

IMG_SIZE = 120

def predict(frame: np.ndarray) -> str:
  """
  Predicts the label of an input image.

  Args:
      frame: An OpenCV object containing the input image.

  Returns:
      The predicted label for the input image as a string.
  """
  print(type(frame))
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  # output = cv2.resize(frame, (512, 360)).copy()
  frame = cv2.resize(frame, (120, 120)).astype("float16")
  frame = frame.reshape(-1,IMG_SIZE, IMG_SIZE, 3) / 255

  preds = model([frame])
  print(preds)
  label = np.argmax(preds)
  print(label)
  print("Output: ",label_encoder.inverse_transform([label]))
  return label_encoder.inverse_transform([label])[0]