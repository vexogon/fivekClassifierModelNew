#Remame jpeg files to jpg files
import os
import shutil
source_folder = 'raw_images_organised_settings'
destination_folder = 'raw_images_organised_settings'
jpeg_count = 0
jpg_count = 0
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
for filename in os.listdir(source_folder):
    if filename.endswith('.jpeg'):
        jpeg_count += 1
        new_filename = filename[:-5] + '.jpg'  # Change the file extension to .jpg
        shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, new_filename))
    else:
        jpg_count += 1

print("JPEG", jpeg_count)
print("JPG", jpg_count)