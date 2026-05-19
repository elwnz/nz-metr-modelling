def metr_bank_deposit (td, REAL_RETURN, INFLATION):
     """
    Simple bank deposit model.

    
    REAL_RETURN: annual interest rate (e.g. 0.05 for 5%)
    td: personal tax rate on interest (e.g. 0.33 for 33%)
    INFLATION: inflation rate (e.g. 0.02 for 2%)

    Returns the final after-tax value of the deposit.
    """
    return td + ((td* INFLATION) / REAL_RETURN)
