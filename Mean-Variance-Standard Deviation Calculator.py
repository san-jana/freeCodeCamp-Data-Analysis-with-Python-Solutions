# https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator
import numpy as np

def calculate(a_list):

    try:
    new_list = np.reshape(a_list,(3,3))
    calc = {'mean': [np.mean(new_list, axis = 0), np.mean(new_list, axis = 1), np.mean(new_list)],
            'variance': [np.var(new_list, axis = 0), np.var(new_list, axis = 1), np.var(new_list)],
            'standard deviation': [np.std(new_list, axis = 0), np.std(new_list, axis = 1), np.std(new_list)],
            'max': [np.max(new_list, axis = 0), np.max(new_list, axis = 1), np.max(new_list)],
            'min': [np.min(new_list, axis = 0), np.min(new_list, axis = 1), np.min(new_list)],
            'sum': [np.sum(new_list, axis = 0), np.sum(new_list, axis = 1), np.sum(new_list)] }
    return(calc)

    except ValueError:
    return print("List must contain nine numbers.")
