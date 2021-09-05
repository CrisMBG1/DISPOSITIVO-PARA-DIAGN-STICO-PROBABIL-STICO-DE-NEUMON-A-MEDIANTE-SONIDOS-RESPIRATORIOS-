import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

longitud, altura = 150, 150
modelo = 'modelo.h5'
pesos_modelo = 'pesos.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):

  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)

  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)

  if answer == 0:
    print("predicción: Asma")
  elif answer == 1:
    print("predicción: Bronquiestasis")
  elif answer == 2:
    print("predicción: Bronquilitis")
  elif answer == 3:
      print("predicción: COPD (Enfermedad pulmonar obstructiva crónica) ")
  elif answer == 4:
      print("predicción: Saludable")
  elif answer == 5:
      print("predicción: LRTI (infección del tracto respiratorio inferior)")
  elif answer == 6:
      print("predicción: Neumonia")
  elif answer == 7:
      print("predicción: URTI (infección del tracto respiratorio superior)")



  return answer