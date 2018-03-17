import numpy as np
import math

def get_vectors_by_category(model, category_id) -> list:
    return model.docvecs[str(category_id)]

def preprocess_array(old_array):

   for x in np.nditer(old_array, op_flags=['readwrite']):
       x[...] = int(math.fabs(x))

   return old_array