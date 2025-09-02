#This code was used to balance the dataset by adding random images from underrepresented settings to reach a target count of 1869 images per setting.
#This is what was used to create the categories_settings_balanced.csv file and add images to the raw_images_organised_settings folder

#I will create a balance dataset for each thing i try and predict with the models

import os
import random
import shutil

import pandas as pd
df = pd.read_csv('categories.csv')
#How far each settings are from a count of 1800
setting_counts = df['setting'].value_counts() # Get counts of each unique value in the 'setting' column
setting_imbalance = 1869 - setting_counts # Calculate how far each setting is from a count of 1800

def add_random_images_to_dataset(df, setting, num_images_to_add):
    images_dir = 'new_data/' + setting + '/' # Path to the folder containing images for the specific setting
    image_files = os.listdir(images_dir) # List all files in the directory
    selected_images = random.sample(image_files, num_images_to_add) # Randomly select the specified number of images
    for image in selected_images:
        img_name = image.split('.')[0] # Extract the image name without the file extension
        shutil.copy2(images_dir + "/" + image,'raw_images_organised_settings') # Copy the image to the target directory
        df.loc[len(df)] = {'img_name': img_name, 'setting': setting} # Add a new row to the DataFrame
    return df

for setting, num_images_to_add in setting_imbalance.items(): # Iterate over each setting and the number of images to add to balance
    if num_images_to_add > 0:
        df = add_random_images_to_dataset(df, setting, num_images_to_add)

df.to_csv('categories_settings_balanced.csv', index=False) # Save the updated DataFrame to a new CSV file

