##image cropping script
##makes all images square

from PIL import Image, ImageDraw
import os, errno

## ./ indicates where this script is located is where to look for this folder
source_dir = "./vegetable source images"
## ./ indicates the same thing as the former
dst_dir = "./veggie_square_images"

##this tries to make a directory with the former strings name
try:
	os.makedirs(dst_dir)
## OSError catches errors related to operating system
## as exc applies the OSError to that exc variable
## 
except OSError as exc:
	## checks if the directory exists, and if the path is indeed a directory
	## if so, pass, because that means the folder is already there, who cares
	if exc.errno == errno.EEXIST and os.path.isdir(dst_dir):
		pass
	##tells it to terminate with an error message
	else:
		raise


##loops over each file in the source directory 
for filename in os.listdir(source_dir):
	##checks if its a jpg, we need them all to be jpg
    if filename.endswith(".jpg"):
		##constructs the full directory path to the file we are on in the
		##for loop
        full_src_path = os.path.join(source_dir, filename)
		##loads the file from system into memeory, returns an Image
		##object, img, which we can do operations on 
        img = Image.open(full_src_path)
		##returns smallest dimension
        min_dim = min(img.size)
		
        ##img is the object we are doing an operation on we created
		##bounding box tuple. (0,0,..) is the top left and bottom right
		## is min_dim and min_dim 
		##creates a new object, cropped_img
        cropped_img = img.crop((0, 0, min_dim, min_dim))

        ##returns the full directoy to the directory we are creating
		##use same filename because we want filenames to be same
		##whether they are cropped or not
        full_dst_path = os.path.join(dst_dir, filename)
		##saves the cropped image inside the destination path
        cropped_img.save(full_dst_path)
		##prints to show its being done
        print("Squared " + filename)