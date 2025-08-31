from PIL import Image
from glob import glob
import shutil
import os

files = 'raw_photos/**/**/*.dng'

print(files)
for file in glob(files, recursive=True):
    filename = file.split('/')[-1] #get filename from path using final '/' to get last element
    organised_dng_file_path = f'raw_images_organised/{filename}'
    copy_image = shutil.copy(file, organised_dng_file_path) #copy image to new location
    rgb_img = Image.open(copy_image).convert('RGB') #convert object to RGB
    organised_jpg_path = organised_dng_file_path.replace('.dng', '.jpg') #change extension to .jpg
    rgb_img.save(organised_jpg_path) #save as jpg

    os.remove(organised_dng_file_path) #delete the copied dng file
    print(f'Converted {file} to {organised_jpg_path}')


