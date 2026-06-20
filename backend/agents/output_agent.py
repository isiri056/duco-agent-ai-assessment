def generate_summary(result):

    return f"""
    Total Cost: ₹{result['total_cost']}

    Primary Paid: ₹{result['primary_paid']}

    Secondary Paid: ₹{result['secondary_paid']}

    Out Of Pocket: ₹{result['out_of_pocket']}
    """