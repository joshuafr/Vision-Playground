# Vision-Playground
Where I mess around with various computer vision applications to knock off the 
rust.

The plan is to implement various vision related operations in Python. Once I
get those done, I'll use libraries to replicate the operations in the future.
For simplicity's sake I'll be using NumPy to do matrix operations; that's not
the skill-set I'm trying to exercise here.

Current progress:

Implementing Gaussian smoothing is under way. Currently the normalized kernel
is created. It's currently stored in a list of lists (2D array). The next 
steps are:

* Storing in a NumPy matrix instead of the 2D array. That will involve 
  installing NumPy of course.
* Loading the image specified and figuring out how to interact with it 
  programatically.
* Applying the convolution.