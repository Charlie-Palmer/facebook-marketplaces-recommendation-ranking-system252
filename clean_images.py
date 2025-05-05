from PIL import Image
import os


def resize_image(final_size, im):
    
    """
    Resize and centre an image on a square of size 224 x 224.
    Args:
        final_size(int): The size of the output square image.
        im: Input image to be resized
    Returns:
        new_image: The resized square image.
    """
    
    size = im.size #Take the size of the original image.
    ratio = float(final_size) / max(size) #Calculate the ratio for resizing.
    new_image_size = tuple([int(x*ratio) for x in size]) #Calculate the new image size.
    im = im.resize(new_image_size, resample=Image.LANCZOS) #Resize the image.
    new_im = Image.new("RGB", (final_size, final_size)) #Create a new blank image of final size.
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2)) #Paste the resized image onto the centre of the blank image.
    return new_im

def clean_image_data(input_folder, output_folder='cleaned_images', size= 224):
    
    """
    Processes all images in the input folder using the resize_image function and saving them to the ouput folder.

    Args:
        input_folder (str): Path to the folder containing images to be cleaned.
        output_folder (str, optional): Path to the folder where cleaned images will be saved. Defaults to 'cleaned_images'.
        size (int, optional): Size of the output square images. Defaults to 224.
    """
    
    os.makedirs(output_folder, exist_ok=True) #Create output folder if it doesn't exist.
    
    for filename in os.listdir(input_folder): #Loop through each file in the input folder.
        #Only process files of common image file types.
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp")):
            input_path = os.path.join(input_folder, filename) #Full path to input image.
            output_path = os.path.join(output_folder, filename)  #Full path for saved cleaned image.
                    
            try:
                with Image.open(input_path) as img: #Open image file.
                    img = img.convert("RGB") #Convert image to RGB.
                    img = resize_image(size, img) #Resize and centre the image.
                    img.save(output_path) #Save to the output folder.
            except Exception as e:
                print(f'Failed to process {filename}: {e}') #Print error if an image fails to process.
    print(f"Image cleaning complete. Cleaned images saved to: {output_folder}") #Print success message with name of folder the images were saved to.

if __name__ == '__main__':
    clean_image_data("images_fb/images/", output_folder="cleaned_images", size=224)