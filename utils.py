import math

'''Uses a Gaussian smoothing convolution to blur an input image.

Keyword arguments:
img_in -- the path to the image being blurred on the disk
img_out -- the path to write the blurred image to
sigma -- the desired standard deviation of the Gaussian (default 1)
size -- the size of the square kernel (default 5)
'''
def smooth_gauss(img_in, img_out, sigma=1.4, kernel_size=5) :
    const = 1/(2 * math.pi * (sigma**2)) #Constant before kernel
    k = round(kernel_size/2) # Constant used in exponentiation
    #initialize empty kernel
    kernel = [[0 for x in range(kernel_size)] for x in range(kernel_size)]
    normalize = 0 
    # Constructing the kernel
    for x in range(1, kernel_size+1):
        for y in range(1, kernel_size+1):
            numerator = ( (x-k-1) **2) + ( (y-k-1) **2)
            denominator = 2*(sigma**2)
            result = math.e ** -(numerator/denominator)
            if x == 1 and y == 1: #Set normalization constant
                normalize = result
            kernel[x-1][y-1] = int(round(result/normalize))
    #kernel is now a kernel_size * kernel_size 2D array whose members have
    #been normalized so that the corners are 1
    for x in range(kernel_size) :
        print kernel[x] #DEBUG

def main():
    smooth_gauss('filler', 'filler2')
    
if __name__ == '__main__':
    main()