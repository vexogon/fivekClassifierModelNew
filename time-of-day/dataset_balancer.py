#This code was used to balance the dataset by adding random images from underrepresented time_of_day to reach a target count of 3206 images per time_of_day.
#This is what was used to create the categories_settings_balanced.csv file and add images to

import os
import random
import shutil

import pandas as pd
df = pd.read_csv('time-of-day/time_of_day_dataset.csv')
time_of_day = df['time_of_day'].value_counts() # Get counts of each unique value in the 'time_of_day' column
time_of_day_imbalance = 3206 - time_of_day # Calculate how far each time_of_day is from a count of 3206 from day images count
print(time_of_day_imbalance)

def add_random_images_to_dataset(df, time_of_day, num_images_to_add):
    images_dir = "time-of-day/" + 'new_data/' + time_of_day + '/' # Path to the folder containing images for the specific time_of_day

    if len(os.listdir(images_dir)) <= num_images_to_add:
        print(f"Not enough images in {images_dir} to add {num_images_to_add} images.")
        num_images_to_add = len(os.listdir(images_dir))
        print(f"Adding only {num_images_to_add} images instead.")

    image_files = os.listdir(images_dir) # List all files in the directory
    selected_images = random.sample(image_files, num_images_to_add) # Randomly select the specified number of images
    print(f"Selected {len(selected_images)} images.")
    for image in selected_images:
        print(f"Adding image {image}.")
        shutil.copy2(images_dir + "/" + image,'time-of-day/raw_images_organised_time_of_day') # Copy the image to the target directory

        df.loc[len(df)] = {'img_name': image, 'time_of_day': time_of_day} # Add a new row to the DataFrame
    return df

for time_of_day, num_images_to_add in time_of_day_imbalance.items(): # Iterate over each time_of_day and the number of images to add to balance
    if num_images_to_add > 0:
        df = add_random_images_to_dataset(df, time_of_day, num_images_to_add)

df.to_csv('time-of-day/time-of-day-dataset_balanced.csv') # Save the updated DataFrame to a new CSV file

