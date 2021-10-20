import os, cv2
from imutils import paths
from itertools import product


def getBaseFolders(base_path):
  """ retorna uma lista com todos os arquivos do caminho informado com seus respectivos path"""
  return [os.path.join(base_path, folder) for folder in os.listdir(base_path) if os.path.isdir( os.path.join(base_path, folder))]


def resizeClassesImages(base_path, sizes):
  base_folders = getBaseFolders(base_path)
  sizes = list(sizes)
  for path, dimensions in list( product( base_folders, sizes ) ):
    print( "woking in", path, "with dimensions {}x{}".format(dimensions[0], dimensions[1]) )
    print("Get Images...")
    image_paths = list( paths.list_images( path ) )

    new_path = base_path + "{}x{}".format(dimensions[0], dimensions[1])
    new_path = os.path.join(new_path, os.path.basename(path))
    os.makedirs(new_path, exist_ok=True)
    new_image_paths = [os.path.join(new_path, os.path.basename(image_path)) for image_path in image_paths]

    print("Saving Images in '{}'... \n\n".format(new_path))
    for index in range(len(image_paths)):
      image = cv2.imread(image_paths[index])
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = cv2.resize(image, dimensions)
      cv2.imwrite(new_image_paths[index], image)



if __name__ == '__main__':
  base_path = '..{}imagens'.format(os.sep)
  mascara_base_path = base_path+"_mascara"
  aumentada_base_path = base_path+"_aumentada"
  mascara_aumentada_base_path = mascara_base_path+"_aumentada"
  sizes = [(200, 267)]

  resizeClassesImages(base_path=base_path, sizes=sizes)
  
  print("Run resizeClassesImages in", mascara_base_path)
  resizeClassesImages(base_path=mascara_base_path, sizes=sizes)
  
  print("Run resizeClassesImages in", aumentada_base_path)
  resizeClassesImages(base_path=aumentada_base_path, sizes=sizes)
  
  print("Run resizeClassesImages in", mascara_aumentada_base_path)
  resizeClassesImages(base_path=mascara_aumentada_base_path, sizes=sizes)