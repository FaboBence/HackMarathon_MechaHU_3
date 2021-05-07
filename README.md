## HackMarathon_MechaHU_3
# Our project 
The aim of our project is to find and fit ellipses on a given set of pictures taken by an electromicroscope. 

Our code takes a picture and starts preprocessing it. After preprocession is done, the altered picture is passed to the edge detection algorithm which provides the edges to be found on the picture. After the edges are found, an ellipse fitting algorithm fits an ellipse on the points of the edges. As this usually isn't the perfect ellipse due to the noisy edges, we do some noise filtering and iterate over the picture in order to smoothen the found ellipse. 
# Detailed description
During the preprocess stage, we apply Gaussian blur and two thresholding algorithms to make the noise and disturbing pixels disappear.  The parameters of the algorithms have been carefuly set to reach an optimum. The tresholding is not hard-coded, instead, the parameters adapt themselves dynamically to the lightest pixels of the image.

The edge detection is done by a Canny agorithm. At this stage of image procession, the picture is usually still noisy, so the algorithm won't only find the edges of the possible ellipse, but also other edges which have to be removed in the further steps to avoid wrong ellipse fits.

At the next stage, we fit an ellipse onto the found edges. Due to the noise, this ellipse won't fit the ellipse to be found well, so we came up with an idea to remove noise. After this first ellipse is fit, we fill up the ellipse with black pixels, and fit an ellipse again to the picture with the blackened middle part. As we removed the noise from the middle of the picture this way, the new ellipse is going to get closer to the real edges of the ellipse to be found. Iterating with this algortihm over the picture provides an ellipse which mostly mathces the ellipse provided by the challenge organizers. The algortihm works fine, as the noise is always inside of the ellipse to be found, outside of it the picture is usually black.

As there are still ellipses which have been fit onto points without any real connection to each other, we also compute an R^2 value to every ellipse which gives a sense of how well the fitted ellipse matches the points onto which it was fit. If R^2 is too high, we say that no ellipse could be found on the picture.
# Further ideas
We've also come up with ideas which seemed to be beneficial in solving the problem, but turned out to be too hard to implement or not precise enough to improve the results.
One of these ideas was to sort edges, and fit ellipses on every small edge-section and choose the ellipse with the lowest R^2 value. Although this idea still seems to be great, we couldn't implement it precise enough to make our results better.

An other idea was to calculate the curvature of the edges found and remove edges with very high or low curvature. This way, we could have filtered out sharp corners or straight lines which are obviously not ellipses, only noise. This could have been done by the calculation of the derivatives of every small eedge section, but we didn't have enough time to make this work. In the future, this idea could boost the performance of our algorithm. 
