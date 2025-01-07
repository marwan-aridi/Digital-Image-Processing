[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qAfTpIeA)
# Digital Image Processing 
Assignment #1

Due: 02/27/24 11:59 PM

1. (20 pts.) Distortion: Write code to perform barrel distortion on an image.
    - Starter code available in directory Tranform/
    - Transform/distortion.py: Edit the function distortion to implement this part.
    
2. (20 pts.) Correction Naive: Write code to perform correction on the input distorted image, by applying the inverse distortion function.
    - Starter code available in directory Tranform/
    - Transform/distortion.py: Edit the function correction_naive to implement this part.
    
2. (35 pts.) Correction with interpolation: Write code to correct the input distorted image, and use nearest neighbor and bilinear interpolation.
    - Starter code available in directory Tranform/
    - Transform/distortion.py: Edit the function correction to implement this part.
    - Transform/interpolation.py: Write code for linear and bilinear interpolation in their respective function definitions, you are welcome to write new functions and call them from these functions


  - The assignment can be run using dip_hw1_rotate.py (there is no need to edit this file)
  - Usage: `python dip_hw1_distortion.py -i image-name -k parameter_k -m method`                   
       - image-name: name of the image
       - k: Parameter k (eg. 0.005)
       - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt/Terminal
  - Any output images or files must be saved to "output/" folder

----------------------
One image is provided for testing: kenny.jpg
  
Notes: 

1. Files not to be changed: requirements.txt, dip.py, and Jenkinsfile 

2. the code has to run using one of the following commands

 - Usage: `./dip_hw1_distortion.py -i image-name -t parameter_k -m method`
 
   Example: `./dip_hw1_distortion.py -i kenny.jpg -k 0.0005 -m bilinear`

 - Usage: `python dip_hw1_distortion.py -i image-name -t parameter_k -m method`
 
   Example: `python dip_hw1_distortion.py -i kenny.jpg -k 0.0005 -m bilinear`
  
3. Any output file or image should be written to output/ folder

4. The code has to run on jenkins CI/CD

**Note:**
We are **restricted from importing cv2, numpy, stats, and other third-party libraries,** 
with the only exception of math, importing math library is allowed (import math).

While you can import it for testing purposes, the final submission should not contain the following statements.
- import cv2
- import numpy
- import numpy as np
- import stats
- etc...

The essential functions for the assignment are available in the dip module one can import using the following statement
```
import dip
from dip import *
```
The following functions are available

```commandline
from cv2 import namedWindow, imshow, waitKey, imwrite, imread

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max
from numpy import int, uint8, float, complex
from numpy import inf
from numpy.fft import fft2
```

*Assignments that contain any files that import these libraries will not be graded.* 
*Assignments that modify the dip.py file will not be graded.*


Part| Name                     | Pts
--------------|--------------------------|----------
1| Distortion               |- 20 Pts
2| Naive Correction         |- 20 Pts
3| Correction interpolation |- 35 Pts
-| **Total**                | - **75 Pts**

-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is the property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the digital image processing course offered at the University of Houston. The contents are not to be reproduced or shared with anyone without the author's permission. The contents are not to be posted on any online public hosting websites without the author's permission. The software is cloned and available to the students for the course duration. At the end of the semester, the GitHub organization is reset, and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>

