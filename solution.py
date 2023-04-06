import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 539377624 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    df = pd.DataFrame(data=x)
    chi_l, chi_r = chi2.ppf([1-alpha/2, alpha/2], df = 1)
    return np.sqrt(df[0].var(ddof=0) / chi_l / 20) , \
           np.sqrt(df[0].var(ddof=0) / chi_r / 20)
