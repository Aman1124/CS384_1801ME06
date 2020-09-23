# All decimal 3 places

import math

# Function to compute mean
def mean(first_list):
    # mean Logic 
    sum = summation(first_list)
    mean_value = sum/len(first_list)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    n = len(first_list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if first_list[j] > first_list[j+1]:
                first_list[j], first_list[j+1] = first_list[j+1], first_list[j]
    if n%2 == 1:
        median_value = first_list[(int(n/2))+1]
    else:
        median_value = (first_list[n/2] + first_list[n/2+1])/2
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    m = mean(first_list)
    a= 0
    for x in first_list:
        if isinstance(x, str):
            return 0
        a = a + ((x-m)*(x-m))
    standard_deviation_value = math.sqrt(a/len(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    variance_value = standard_deviation(first_list)*standard_deviation(first_list)
    return variance_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value = 0
    if len(first_list) != len(second_list):
        return 0
    else:
        for i in range(len(first_list)):
            if isinstance(first_list[i],str) or isinstance(second_list[i],str):
                return 0
            rmse_value = rmse_value + (first_list[i]-second_list[i])*(first_list[i]-second_list[i])
        rmse_value = math.sqrt(rmse_value/len(first_list))
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    mse_value = rmse(first_list, second_list)*rmse(first_list,second_list)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    mae_value = 0
    if len(first_list) != len(second_list):
        return 0
    else:
        for i in range(len(first_list)):
            if isinstance(first_list[i], str) or isinstance(second_list[i],str):
                return 0
            mae_value = mae_value + abs(first_list[i]-second_list[i])
        mae_value = mae_value/len(first_list)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    nse_value = 1 - mse(first_list, second_list)/variance(first_list)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    num = 0
    if len(first_list) != len(second_list):
        return 0
    else:
        mean_x = mean(first_list)
        mean_y = mean(second_list)
        for i in range(len(first_list)):
            if isinstance(first_list[i], str) or isinstance(second_list[i], str):
                return 0
            num = num + (first_list[i]-mean_x)*(second_list[i]-mean_y)
        pcc_value = num/(standard_deviation(first_list)*standard_deviation(second_list)*len(first_list))
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    m = mean(first_list)
    num = 0
    for x in first_list:
        if isinstance(x, str):
            return 0
        num = num + (x-m)*(x-m)*(x-m)
    sd = standard_deviation(first_list)
    skewness_value = num/(len(first_list)*sd*sd*sd)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    n = len(first_list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if first_list[j] > first_list[j+1]:
                first_list[j], first_list[j+1] = first_list[j+1], first_list[j]
    return first_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    m = mean(first_list)
    num = 0
    for x in first_list:
        if isinstance(x, str):
            return 0
        num = num + (x-m)*(x-m)*(x-m)*(x-m)
    sd = standard_deviation(first_list)
    kurtosis_value = num/(len(first_list)*sd*sd*sd*sd)
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for x in first_list:
        if isinstance(x, str):
            return 0
        summation_value =  summation_value + x
    return summation_value