import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = st.cramervonmises_2samp(x, y)[1]
    if (p_value<0.09):
        return True
    else:
        return False
