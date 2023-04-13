import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_v=st.ks_2samp(x, y, alternative='two-sided')[1]
    p_value=2*np.min([norm.cdf(p_v)-
    if (p_value<0.09):
        return True
    else:
        return False
