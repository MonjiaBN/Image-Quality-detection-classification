# Image-Quality-detection-classification
Sometimes, when I collect images for a dataset for a computer vision project, I take many blurred images that I didn't notice and it will take me time define them and delete them or maybe try to deblur . So I decide to develop a system that detects the quality of an image (clear or blur image) that help people to define the blurred ones.
Try the web application below


## Methods used :
To detect/classify the blurred images ,i use this two methods:

# 1- Variation of the Laplacian
a blurry image doesn't have a clearly edges ( an edge is a sharp change in intensity or color)
The laplacian isa type of edge detection filter that works with kernel convolution method (So laplacian convolves the image with the kernel and then return the variance)
- For clear images : a high variance between pixels
- For Blurry images : a small variance between pixels values ( not really a sharp change )
NB : we need to tune the value of the threshold : choose threshold basis by trial and error

### accuracy Score for NaturalBlurSet: 48.70%
### accuracy Score for DigitalBlurSet: 95.83%

# 2- Convolutional Neural Networks (CNN)
The accuracy of the model 58.18%

## About Dataset :
The dataset used in this repository is CERTH Image Blur Dataset.
You can download the dataset from this link  http://mklab.iti.gr/files/imageblur/CERTH_ImageBlurDataset.zip

# required packages in "requirements.txt" file

Some packages :
matplotlib 

numpy

pandas

requests

seaborn

scikit-learn

Flask (For Web Development)

# Link of the web application 

# References: 
https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/





