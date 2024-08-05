# ascii art 

from PIL import Image


img=Image.open(r'asc-car.jpg')

##checks we are in rgb mode and correct resolution
print(img.mode)
print(img.size)

#640,480
width,height=img.size

print(width)

#making 2d list that will contain lists 
outerlist=[]

print('Storing RGB values in list...')
#make a new list for each 640 rows
for row in range(height):
    innerlist=[]
    ##create tuple entries in each 480 columns
    for column in range(width):
        ##returns a tuple at specified XY (width height) location and appends to
        ##its respective row
        ## ( ( ) ) indicates you are feeding a tuple as an argument
        ## ( ) would feed two separate arguments 
        rgb=img.getpixel((column,row))
        print(rgb)
        
        innerlist.append(rgb)
    outerlist.append(innerlist)
print('Stored')

#With your pixel data in a 2-dimensional array, you will be able to access 
# pix_matrix[row][column
#the data at a given x, y co-ordinate as pixel_matrix[x][y], 
#and you will be able to iterate through it 

##asciimap list, 67 characters, 0-255 scale for brightness,
## calculates that character 1 corresponds to brigthness 3.8059
#were gonna need to make ranges to resolutions of our choice that round up before
# returning to index this string 
asciimap=r"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXUYJCLQ0OZmwqpdbkhao*#MW&8%B@$"

lenascii=len(asciimap)

final=255/lenascii

print('Data iterated through testing...')
##access each row 
for row in range(len(outerlist)):
    ## access each column outerlist[row] returns how many columsn in this row
    for column in range(len(outerlist[row])):
        pixel=outerlist[row][column]
        x,y,z=pixel
        ##avg brightness formula
        avgbrightness=0.21*x + 0.72*y + 0.07*z

        pixelconvert=int(round(avgbrightness/final))

        # pixelconvert = min(max(pixelconvert, 0), len(asciimap) - 1)

        asciiconverted=asciimap[pixelconvert-1]

        ##store it back into what was the rgb matrix
        outerlist[row][column]=asciiconverted
        
        
        #edit the data somehow?
    


with open('asccar.txt', 'w') as file:
    for row in outerlist:
        file.write(''.join(row) + '\n')




##asciimap list, 67 characters, 0-255 scale for brightness,
## calculates that character 1 corresponds to brigthness 3.8059
#were gonna need to make ranges to resolutions of our choice that round up before
# returning to index this string 
