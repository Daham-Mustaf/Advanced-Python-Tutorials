# Write a function that takes a JSON file and converts it into a Python dictionary. You can use the json module to accomplish this.
import json

def json_to_dict(file_path):
    with open(file_path, 'r') as f:
        json_string = f.read()
    return json.loads(json_string)
my_dict = json_to_dict('my_file.json')
print(my_dict)

# Write a function that takes a Python dictionary and writes it to a JSON file.import json


def write_to_json_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
my_dict = {'name': 'Alice', 'age': 25}
write_to_json_file(my_dict, 'my_data.json')
import json
import pathlib
import configparser
import os
import glob

def rename_files(directory_path):
    """
    This function renames image files in a given directory by removing a specific suffix, replacing characters, and adding a new suffix.

    Arguments:
    ------------

    directory_path: A string representing the path to the directory containing the image files.
    Returns:
    --------
    None

    Raises:

    """
    
    # Set the suffix for the new file names
    suffix = '.JPG'

    # Get a list of all image files in the directory
    image_files = glob.glob(directory_path + '360*.JPG')

    # Loop through each image file and rename it
    for image_file in image_files:
        try:
            # Get the original file name without the directory path or suffix
            original_filename = os.path.splitext(os.path.basename(image_file))[0]

            # Replace "_stitched_straightened_injected" with an empty string
            new_filename = original_filename.replace('_stitched_straightened_injected', '')

            # Replace all instances of "__" with "_"
            new_filename = new_filename.replace('__', '_')

            # Replace "360" with "ID_" in the file name
            new_filename = new_filename.replace('360', 'ID') + suffix

            # Rename the file
            os.rename(image_file, os.path.join(directory_path, new_filename))
            print(f'Renamed file {image_file} to {new_filename}')
            
        except Exception as e:
            print(f'Error renaming file: {image_file} ({e})')

def get_image_files(directory, extensions):
    """Get the image files in a directory with the given extensions."""
    files = []
    try:
        for file in directory.glob('*'):
            if file.suffix.lower() in extensions:
                files.append(file)
    except OSError as e:
        print(f"Error: {e.strerror}")
    return sorted(files)

def build_scene(file, next_file=None):
    """Build a scene dictionary for the given file."""
    file_name = os.path.splitext(file.name)[0].capitalize()
    scene = {
        "title": file_name.upper(),
        "hfov": 180,
        "pitch": -4,
        "yaw": 179,
        "type": "equirectangular",
        "panorama": f"/images/{file.name}"
    }
    if next_file:
        next_file_name = os.path.splitext(next_file.name)[0].capitalize()
        scene["hotSpots"] = [{
            "pitch": -2.1,
            "yaw": 132.9,
            "type": "scene",
            "text": next_file_name.upper(),
            "sceneId": next_file_name.upper()
        }]
    return scene


def build_json_config(directory, extensions):
    """Build a JSON configuration object for the given directory with the given extensions."""
    files = get_image_files(directory, extensions)
    if not files:
        print("No image files found.")
        return
    first_file = files[0]
    scenes = {}
    for i, file in enumerate(files):
        next_file = None
        if i < len(files) - 1:
            next_file = files[i+1]
        scene = build_scene(file, next_file)
        scene_name = file.stem.replace('Id_', 'ID_')
        scenes[scene_name] = scene
    json_object = {
        "default": {
            "firstScene":  os.path.splitext(first_file.name)[0].capitalize().upper(),
            # os.path.splitext(next_file.name)[0].capitalize()
            "author": "Daham Mustafa",
            "sceneFadeDuration": 1000
        },
        "scenes": scenes
    }
    return json_object


def write_json_config(json_object, output_file):
    """Write the JSON configuration object to a file."""
    output_dir = pathlib.Path(output_file).parent
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    with open(output_file, "w") as f:
        json.dump(json_object, f, indent=2)

# if __name__ == "__main__":
#     config = configparser.ConfigParser()
#     config.read('config.ini')
#     image_extensions = config.get('Settings', 'image_extensions').split(',')
#     images_dir = pathlib.Path(config.get('Settings', 'images_dir'))
#     output_file = config.get('Settings', 'output_file')
#     json_config = build_json_config(images_dir, image_extensions)
#     if json_config:
#         write_json_config(json_config, output_file)
#         print(f"JSON configuration file saved to {output_file}.") 

if __name__ == "__main__":
    # path to directory 
    directory_path = '/Users/m-store/Desktop/test/'
    rename_files(directory_path)

    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG')
    images_dir = pathlib.Path('/Users/m-store/Desktop/test')
    output_file = '/Users/m-store/Desktop/Data_thesis/OMS/Script/config.json'
    json_config = build_json_config(images_dir, image_extensions)
    if json_config:
        write_json_config(json_config, output_file)
        print(f"JSON configuration file saved to {output_file}.")
