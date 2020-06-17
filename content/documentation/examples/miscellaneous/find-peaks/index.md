+++
title = "Finding Intensity Peaks"
weight = 10
+++

### Finding Intensity Peaks

To find the intensity peaks from a GISAXS simulation, the result must be casted in the form of a `histogram2d`. This must then be passed to the method `FindPeaks` to get the (x,y) coordinates of each peak:

```python
    result = run_simulation().histogram2d()
    peaks = ba.FindPeaks(result, 2, "nomarkov", 0.001)
    peaks_x = [peak[0] for peak in peaks]
    ypeak_y = [peak[1] for peak in peaks]
```

{{< galleryscg >}}
{{< figscg src="Figure.png" width="670px" caption="Intensity images">}}
{{< /galleryscg >}}

The following script offers a complete example in which the peaks are found after carrying on a GISAXS simulation. This particular example uses as a sample a grating of long boxes distributed along a 1D lattice.

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/FindPeaks.py" language="python" >}}
