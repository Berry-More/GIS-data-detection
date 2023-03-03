import numpy as np


def mean(array):
    return sum(array)/len(array)


def running_mean(x, N):
    out = np.zeros_like(x, dtype=np.float64)
    for i in range(len(x)):
        if N%2 == 0:
            a, b = i - (N-1)//2, i + (N-1)//2 + 2
        else:
            a, b = i - (N-1)//2, i + (N-1)//2 + 1
        a = max(0, a)
        b = min(len(x), b)
        out[i] = np.mean(x[a:b])
    return list(out)


def get_borders(data, step, diff, filter_value=1):
    
    data = running_mean(data, filter_value)
    all_mean = abs(mean(data))
    
    points = []
    interval = list(data[:step])
    for i in range((len(data) // step) - 1):

        current_interval = list(data[(i+1)*step:(i+2)*step])
        if (abs(mean(current_interval) - mean(interval))/all_mean)*100 < diff:
            interval += current_interval
        else:
            points.append((i+1)*step)
            interval = current_interval
            
    return points
