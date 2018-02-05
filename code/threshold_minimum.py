# -*- coding: utf-8 -*-
# MODIFIED ALGORITHM USED BY CACO

'''
New BSD License

Copyright (c) 2007–2018 The scikit-learn developers.
All rights reserved.


Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of the Scikit-learn Developers  nor the names of
     its contributors may be used to endorse or promote products
     derived from this software without specific prior written
     permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
'''

# modified function from scikit
# https://github.com/scikit-image/scikit-image/blob/master/skimage/filters/thresholding.py

from skimage.exposure import histogram
from scipy.ndimage import filters as ndif
import numpy as np


# modifification is highlighted by "FIX begin -->>"
def threshold_minimum(image, nbins=1e4, max_iter=1000):
    """Return threshold value based on minimum method.
    The histogram of the input `image` is computed and smoothed until there are
    only two maxima. Then the minimum in between is the threshold value.
    Parameters
    ----------
    image : (M, N) ndarray
        Input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.
    max_iter: int, optional
        Maximum number of iterations to smooth the histogram.
    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.
    Raises
    ------
    RuntimeError
        If unable to find two local maxima in the histogram or if the
        smoothing takes more than 1e4 iterations.
    References
    ----------
    .. [1] C. A. Glasbey, "An analysis of histogram-based thresholding
           algorithms," CVGIP: Graphical Models and Image Processing,
           vol. 55, pp. 532-537, 1993.
    .. [2] Prewitt, JMS & Mendelsohn, ML (1966), "The analysis of cell
           images", Annals of the New York Academy of Sciences 128: 1035-1053
           DOI:10.1111/j.1749-6632.1965.tb11715.x
    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_minimum(image)
    >>> binary = image > thresh
    """

    def find_local_maxima_idx(hist):
        # We can't use scipy.signal.argrelmax
        # as it fails on plateaus
        maximum_idxs = list()
        direction = 1


        for i in range(hist.shape[0] - 1):
            if direction > 0:
                if hist[i + 1] < hist[i]:
                    direction = -1
                    maximum_idxs.append(i)
                # -->> FIX proposed
                elif i == hist.shape[0] - 2:
                    maximum_idxs.append(i)
                # <<-- FIX end
            else:
                if hist[i + 1] > hist[i]:
                    direction = 1
        return maximum_idxs

    hist, bin_centers = histogram(image.ravel(), nbins)
    smooth_hist = np.copy(hist).astype(np.float64)


    for counter in range(max_iter):
        smooth_hist = ndif.uniform_filter1d(smooth_hist, 3)

        maximum_idxs = find_local_maxima_idx(smooth_hist)
        if len(maximum_idxs) < 3:
            break

    if len(maximum_idxs) != 2:
        raise RuntimeError('Unable to find two maxima in histogram')
    elif counter == max_iter - 1:
        raise RuntimeError('Maximum iteration reached for histogram'
                           'smoothing')

    # Find lowest point between the maxima
    threshold_idx = np.argmin(smooth_hist[maximum_idxs[0]:maximum_idxs[1] + 1])
    threshold_lowest = bin_centers[maximum_idxs[0] + threshold_idx]
    return threshold_lowest

