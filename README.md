# Visual Bloom Filter - HD Version!

This is an update of my original Raspberry Pi / Pimoroni Unicorn Hat Visual Bloom Filter project.  Check out the [original article on my website](https://simonprickett.dev/visual-bloom-filter-with-raspberry-pi/), and the more complete README for the original [on GitHub](https://github.com/simonprickett/visual-bloom-filter-for-pi).

This version uses the [Pimoroni Unicorn Hat HD](https://shop.pimoroni.com/products/unicorn-hat-hd) in place of the original [Unicorn Hat](https://shop.pimoroni.com/products/unicorn-hat) from the previous project.  The primary difference between the two is that the original Unicorn Hat has 64 individually programmable LEDs (a grid of 8 x 8), while the HD version has 256 (in a 16 x 16 grid arrangement).  The HD version uses a different Python library than the regular Unicorn Hat but this has basically the same API.  As both products are the same size, this means that the LEDs are smaller / more densely packed in the HD version.

The code for this project (see `app.py`) is very similar to that of the original project.  The primary differences are as follows:

* Use of the `unicornhathd` ([documentation here](https://github.com/pimoroni/unicorn-hat-hd)) library rather than the original `unicornhat` one.
* As there are more LEDs, the bit array that forms the Bloom Filter is larger with the HD product (256 bits rather than 64).  I decided to use 6 hash functions with the HD version rather than 3 from the original.
* I set the brightness setting to a different value for the HD product vs the original.

Other than that, the project's the same as the original so for more detail and a description of what a Bloom Filter is and how it works, check out the [original project's article on my website](https://simonprickett.dev/visual-bloom-filter-with-raspberry-pi/).  I will add a new article and video specifically covering this version of the project at some point in the future...

