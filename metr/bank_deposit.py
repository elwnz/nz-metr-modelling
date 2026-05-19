def metr_bank_deposit(td, REAL_RETURN, INFLATION):
    """
    Simple bank deposit METR model.

    td: personal tax rate on interest (e.g. 0.33)
    REAL_RETURN: real interest rate (e.g. 0.05)
    INFLATION: inflation rate (e.g. 0.02)

    Returns the METR for the deposit.
    """
    return td + ((td * INFLATION) / REAL_RETURN)

