def calculate_tax(income, brackets=None):
    """
    Menghitung pajak penghasilan berdasarkan bracket progresif.
    
    Parameters:
    - income (float): Pendapatan tahunan dalam satuan mata uang (misalnya, rupiah atau USD).
    - brackets (list of tuples, optional): Daftar bracket dalam format [(batas_atas, tarif), ...].
      Default: Bracket sederhana mirip Indonesia (dalam rupiah).
    
    Returns:
    - float: Total pajak yang harus dibayar.
    
    Contoh brackets: [(50000000, 0.0), (250000000, 0.05), (500000000, 0.15), (float('inf'), 0.25)]
    """
    if brackets is None:
        # Bracket default (sesuaikan dengan negara Anda)
        brackets = [
            (50000000, 0.0),      # 0 - 50 juta: 0%
            (250000000, 0.05),    # 50 - 250 juta: 5%
            (500000000, 0.15),    # 250 - 500 juta: 15%
            (float('inf'), 0.25)  # > 500 juta: 25%
        ]
    
    tax = 0.0
    previous_limit = 0.0
    
    for limit, rate in brackets:
        if income > previous_limit:
            taxable = min(income, limit) - previous_limit
            tax += taxable * rate
            previous_limit = limit
        else:
            break
    
    return tax

# Fungsi helper untuk format output
def format_currency(amount, currency="IDR"):
    """Format angka sebagai mata uang."""
    return f"{currency} {amount:,.0f}".replace(",", ".")
