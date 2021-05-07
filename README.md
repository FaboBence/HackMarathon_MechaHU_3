# HackMarathon_MechaHU_3 **Electron Microscope image processing**

## Team

**MechaHU**

### Team members

- Bence Fabó, Budapest University of Technology and Economics
- Mihály Makovsky, Budapest University of Technology and Economics
- Gellért Csapodi, Budapest University of Technology and Economics

## Our project 
The aim of our project is to find and fit ellipses on a given set of pictures taken by an electron microscope.

Our code opens a picture and starts processing it which consist of two phases. The prepocessing and the edge detection. After the edges are found, an ellipse fitting algorithm fits an ellipse onto them. As this first ellipse is usually not perfect due to noise in the edges, we do some noise filtering and have a second iteration of ellipse fitting to get better results.

On the left image, the green ellipse is the one fitted by us, the blue is provided by Thermo Fischer as ground truth. The right image depicts the found edges. 

![image](https://user-images.githubusercontent.com/65888378/117469002-8eee6080-af55-11eb-9ede-1125ffc07973.png)
![image](https://user-images.githubusercontent.com/65888378/117469018-9281e780-af55-11eb-9431-832543ec5b88.png)

## Detailed description
During the preprocess stage, we apply **Gaussian blur** and **thresholding** algorithm to reduce noise. The parameters of the algorithms have been carefully set to reach an optimum on the training data set. The tresholding is not hard-coded, the parameters adapt themselves dynamically to the brightest pixels of the image.

The **edge detection** is done by a **Canny algorithm**. At this stage of image procession the picture is usually still noisy, so the algorithm won't only find the edges of the ground truth ellipse, but also other edges which have to be removed in the further steps.

As we mentioned earlier, after edge detection the fitted ellipse won't fit well due the noisy edges.

![image](https://user-images.githubusercontent.com/65888378/117473256-0b833e00-af5a-11eb-933b-8d82f540f6c7.png)
![image](https://user-images.githubusercontent.com/65888378/117472302-08d41900-af59-11eb-94ae-75a2c34403d4.png)

We realised that the noise we are dealing with is mostly inside of the ground truth ellipse, so we came up with the idea of removing the edges found inside the generated ellipse. As you can see, if we iteratively repeat these steps the generated ellipse is going to get closer to the real edges of the ground truth ellipse.

![image](https://user-images.githubusercontent.com/65888378/117475170-07582000-af5c-11eb-95cd-2af90d69ef34.png)
![image](https://user-images.githubusercontent.com/65888378/117475206-0de69780-af5c-11eb-98f3-31ee71d99023.png)

We also compute the variance to every generated ellipse which gives a sense of how well it fits. If the variance is too high, we assume that no ellipse could be found on the picture.

## Further ideas
We've also come up with ideas that seemed to be beneficial in solving the problem, but turned out to be too hard to implement or not precise enough to improve the results.
One of these ideas was to find **continuous edges** and divide them into **smaller sections**. **We wanted to find an ellipse which fits a section almost perfectly** based on the theory, that if a ground truth ellipse exist, then there has to be at least a small edge section on the image which is part of it. Although this idea still seems to be great, we couldn't implement it precisely enough to make our results better. Here is the best fit we could achieve with it. (The red ellipse is fitted by this algorithm.)

![image](https://user-images.githubusercontent.com/65888378/117479437-a121cc00-af60-11eb-835d-26b5857f5ca7.png)

An other idea was to calculate the curvature of these edge sections and remove those with very high or low curvature. This way, we could have filtered out sharp corners and straight lines, and only fit an ellipse on the remaining edges.

Unfortunately we didn't have enough time to experiment with all of our ideas, but we are sure that we would be able to develop an algorithm with the required precision.
