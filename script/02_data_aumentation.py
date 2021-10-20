from imutils import paths
from itertools import product
import numpy as np
import os, cv2

def getBaseFolders(base_path):
  """ retorna uma lista com todos os arquivos do caminho informado com seus respectivos path"""
  return [os.path.join(base_path, folder) for folder in os.listdir(base_path) if os.path.isdir( os.path.join(base_path, folder))]

def imageGenerator(image_path, out_path):
  from numpy import expand_dims
  # from keras.preprocessing.image import load_img
  from keras.preprocessing.image import img_to_array
  from keras.preprocessing.image import ImageDataGenerator
  
  image = cv2.imread(image_path)
  image = img_to_array(image)
  image = expand_dims(image, 0)

  datagen = ImageDataGenerator(brightness_range=[0.5,1.5], horizontal_flip=True, vertical_flip=True)
  it = datagen.flow(image, batch_size=1)
  batch = it.next()
  image = batch[0].astype('uint8')
  cv2.imwrite(out_path, image)


def classesImageGenerator(base_path, num_images=1):
  base_folders = getBaseFolders(base_path)
  for path in base_folders:
    print( "Trabalhando dentro de ", path )
    print("Pegando imagens...")
    image_paths = list( paths.list_images( path ) )
    
    print("Creating output list names...")
    new_path = base_path + "_aumentada"
    new_path = os.path.join(new_path, os.path.basename(path))
    os.makedirs(new_path, exist_ok=True)
    out_image_paths = [os.path.join(new_path, os.path.basename(image_path)) for image_path in image_paths]

    print("Generating Images in '{}'... \n\n".format(new_path))
    for index in range(len(image_paths)):
      for i in range(num_images):
        out_image_path = out_image_paths[index]
        dot_loc = out_image_path.rfind('.')
        out_image_path = out_image_path[:dot_loc] + " (0{}) ".format(i+1) + out_image_path[dot_loc:]
        imageGenerator(image_paths[index], out_image_path)

  print("Finish classesImageGenerator!!!")


if __name__ == '__main__':
  base_path = '..{}imagens'.format(os.sep)
  mascara_base_path = base_path+"_mascara"
  aumentada_base_path = base_path+"_aumentada"
  mascara_aumentada_base_path = mascara_base_path+"_aumentada"
  
  # print("Run classes de Images aumentadas")
  # classesImageGenerator(base_path=base_path, num_images=5)
  
  # print("Run classesImageGenerator")
  # classesImageGenerator(base_path=aumentada_base_path, num_images=5)

  print("FINISH ALL!!!")


  