from imutils import paths
import numpy as np
import os, cv2

def getBaseFolders(base_path):
  return [os.path.join(base_path, folder) for folder in os.listdir(base_path) if os.path.isdir( os.path.join(base_path, folder))]

def maskImage(image_path, out_path):
  image = cv2.imread(image_path)
  image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  low_color = np.array([25, 52, 72])
  high_color = np.array([102, 255, 255])
  color_mask = cv2.inRange(image_hsv, low_color, high_color)
  masked_image = cv2.bitwise_and(image, image, mask=color_mask)
  cv2.imwrite(out_path, masked_image)


def maskClassesImages(base_path):
  base_folders = getBaseFolders(base_path)

  for path in base_folders:
    print( "trabalhando dentro de ", path )
    print("pegando Imagens...")
    image_paths = list( paths.list_images( path ) )
    
    print("Criando a lista de nomes de saida...")
    new_path = base_path + "_mascara"
    new_path = os.path.join(new_path, os.path.basename(path))
    os.makedirs(new_path, exist_ok=True)
    out_image_paths = [os.path.join(new_path, os.path.basename(image_path)) for image_path in image_paths]
    
    print("Conveting Images in '{}'... \n\n".format(new_path))
    for index in range(len(image_paths)):
      maskImage(image_paths[index], out_image_paths[index])
  print("Segmentacao terminada!!!")


if __name__ == '__main__':
  base_path = '..{}imagens'.format(os.sep)

  print("Rodando Segmentacao")
  maskClassesImages(base_path=base_path)