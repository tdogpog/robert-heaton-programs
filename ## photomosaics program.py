## photomosaics program

from PIL import Image 
import copy
import os
import math


img_initial=Image.open('dadsfamily.jpg')

width,height=img_initial.size


def generate_rgb_matrix():
    ##puts average color into a list of lists for each 640,480 pixel
    rgbmatrix=[]
    for row in range(height):
        innerlist=[]    
        for column in range(width):

            rgb=img_initial.getpixel((column,row))

            r,g,b=rgb

            innerlist.append((r,g,b))
        rgbmatrix.append(innerlist)
    
    return rgbmatrix


  
   
def calculate_average_for_chunks(rgbmatrix,chunksize):
    
    ##make a deep copy to edit
    avg_pixel_replacement=copy.deepcopy(rgbmatrix)

 
    ##extract chunks, 50x50 chunks AT A TIME
    ##this syntax for range grabs 50 rows and 50 columsn AT ONCE
    ##big lesson- we can use iterators like this FOR later iterators arguments
    ##to define how we want it to navigate the data in this instance,
    ##constraining it to chunks of 50 
    ##the first iteraton is going to print ZERO, NOTHING
    ##because the syntax is range(start,stop,step)
    ## example, range(3,10,2)
    ##outputs 3,5,7,9
    ##as you can see, 0 will go through first,
    ##and THEN you will get 50
    for row in range(0,height,chunksize):
        
        for column in range(0,width,chunksize):
            ##initialize the values to reset for each chunk
            total_pixel=0
            total_r=0   
            total_g=0
            total_b=0

            ##iterate over the chunk we just grabbed, really the function of that last 
            ##nested for loop was to set up the row/column argument that accurately
            ##examins the avg_pixel_replacement data structure, and resets 
            ##the counts for each chunk
            ##set a min argument on range for the chunks were in for boundary
            #concerns
            ##KEY NOTE. this is also a NEW range function syntax
            ##range(value,X) value is where it STARTS, X is where it ENDS
            ##typically range takes a value and then goes to zero
            ##then counts up to n-1 before it
            ##but this new syntax STARTS at value, and counts up to X
            ##o the second nested for loop structure will 
            #receive row/column as 0 for the first iteration, 
            #and the min will be row+chunksize, so 
            #it is effectively targeting the first 0-50 blocks. 
            #next iteration, row will be 0, column will be 50, 
            #so the second for loop structure will have row 0, 
            #stop point at 50, and the column 50, stop point at 100. 
            for i in range(row,min(row+chunksize-1,height)):
                for j in range(column,min(column+chunksize-1,width)):
                    r,g,b=avg_pixel_replacement[i][j]
                    total_r+=r
                    total_g+=g
                    total_b+=b
                    total_pixel+=1

            ##avg for each chunk
            avg_r=total_r//total_pixel
            avg_g=total_g//total_pixel
            avg_b=total_b//total_pixel

            ##should probably do the pythag matching here, match it 
            ##with the value in our dictionary,
            ##then remap it using a nested for loop structure 
            ##its going to be a 50x50 everytime... may need to adjust some 
            ##syntax

            
            distance_min=float('inf')

            img_replace=''

            ##goes through each value in our dictionary, which is a 2d matrix
            for key,avg_data in avg_source_color.items():
                source_r,source_g,source_b=avg_data
            
                distance=math.sqrt((source_r-avg_r)**2+(source_g-avg_g)**2+(source_b-avg_b)**2)
                if distance< distance_min:
                        distance_min=distance
                        file_name=key

            

            min_dist_img_data=source_images.get(file_name)


            ## use the same iterators that targed our chunks to replace it with average values
            ##go to the top and get our next chunk
            for i in range(row,min(row+chunksize,height)):
                for j in range(column,min(column+chunksize,width)):

                    ##BIG LESSON
                    ##PURPOSE OF MODULO: MAP COORDINATES FROM A 
                    ##SMALLER IMAGE TO A LARGER ONE, ENSURING SMALLER
                    ##ONE FITS WITHIN THE LARGER ONE
                    ## we had an issue here where we needed to map a 
                    ##50x50 coordinate system onto a BIG PICTURE 
                    ##640,480 coordinate system.
                    ##we fixed this by using MODULO. 
                    ##modulu for example if i was =347%chunksize=47
                    ##we effectively are on the 47th element of 6th chunk
                    ##and since ONLY CARE about the chunks coordinate restrictions
                    ##we chop off the larger picture with modulo 
                    ##and that will fit it to the smaller chunksizes
                    ##frames, and allow us to look at the datastrctureu
                    ##of the smaller image that is supposed to match the 
                    ##chunk size
                    smaller_img_pixel=min_dist_img_data[i%chunksize][j%chunksize]
                    avg_pixel_replacement[i][j]=smaller_img_pixel
                    # avg_pixel_replacement[i][j]=avg_r,avg_g,avg_b
    

    
    return avg_pixel_replacement


##feed it the directory and the dimension you want to standardize
## all the images to 
def load_in_sourceimages(dir_path,dim):

    ## dictionary_name[key]=value 
    ##this will be our mode of storage
    ##were going to imgs[filename]=imgdata
    ##this will allow us to access source image data via filename
    imgs={}

    for filename in os.listdir(dir_path):
        if filename.endswith('.jpg'):
            ##go into specified dir_path and add filename at end to get
            ##the exact file we want
            full_path=os.path.join(dir_path,filename)
            ##open using dir and pil library
            img=Image.open(full_path)
            ##scale img with dim input
            ##thumbnail is used to fit size, preserve aspect ratio
            ##syntax is image.thumbnail(size, resample=Image.BICUBIC)
            ##2nd parameter is optional, first parameter is the tuple dim
            ##you want to resize the image to 
            ##2nd param is the resampling filter for pic quality 
            ##default is bicubic, best quality results
            img.thumbnail((dim,dim))

            ##stores the image as a 2d datastructure in our 
            ##dictionary.
            ##i did this to make replacing a 50x50 grid simple because
            ##this is being stored as the same type of data structure
            ## as our initial grid we fed in, making comparisons and replacements
            ## a 1-1 operation since we're doing 50x50 vs 50x50
            img_data=[]
            for row in range(img.height):
                source_inner=[]
                for column in range(img.width):
                    pixel=img.getpixel((column,row))
                    r,g,b=pixel
                    source_inner.append((r,g,b))

                img_data.append(source_inner)

            
            imgs[filename]=img_data
    
    return imgs

##feed it a source image, it will return the avg color of that entire image
def source_image_avgcolor(source_img):
    total_r=0
    total_g=0
    total_b=0
    total_pixel=0

    for row in range(len(source_img)):
        for column in range(len(source_img[row])):
            r,g,b=source_img[row][column]
            total_r+=r
            total_g+=g
            total_b+=b
            total_pixel+=1

            
    avg_r=total_r//total_pixel
    avg_g=total_g//total_pixel
    avg_b=total_b//total_pixel

    
    return(avg_r,avg_g,avg_b)

def create_image(finalmatrix):
    height=len(finalmatrix)
    ##allow us to print rectangular images
    ##if you dont have the [0] you're just getting the len of 
    ##final matrix, which is how many lists are in it, which is 
    ##how many rows are in it
    ##we want how many columns are in any given list
    ##so yeah index the first row directly and use len on it
    ##that will give us the amount of columns in that list 
    width=len(finalmatrix[0])
    final_image=Image.new('RGB',(width,height))
    pixels=final_image.load()
    for y in range(height):
        for x in range(width):
            pixels[x,y]= finalmatrix[y][x]

    return final_image

##chunk and dim should be same to ensure everything is in constraints
##the chunk is the pixelated size, goal is to replace pixels
## with the source images, dim arg sizes them to chunk for us 
chunk=5
dim=chunk

##go to ##imagecropping script, provide source images
##change source/destionation code, execute
##change top of the code for the large image
##change this for what folder of square images you want
##then run
source_images=load_in_sourceimages('./pokemon_square_images',dim)

avg_source_color={}
for filename,img in source_images.items():
    avg_color=source_image_avgcolor(img)
    avg_source_color[filename]=avg_color
    
print('source images loaded')


make_matrix=generate_rgb_matrix()
print('calculating larger image')

averaging=calculate_average_for_chunks(make_matrix,chunk)


averaging_image=create_image(averaging)

averaging_image.show()




