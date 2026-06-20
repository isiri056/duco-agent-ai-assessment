from mock_api.insurer1 import PLAN_A
from mock_api.insurer2 import PLAN_B

def calculate_acl_claim():

    total_cost = 450000

    deductible = PLAN_B["deductible"]

    remaining = total_cost - deductible

    primary_paid = remaining * PLAN_B["coinsurance"]

    patient_balance = remaining - primary_paid

    secondary_paid = patient_balance * PLAN_A["coinsurance"]

    oop = patient_balance - secondary_paid

    return {
        "total_cost": total_cost,
        "primary_paid": round(primary_paid),
        "secondary_paid": round(secondary_paid),
        "out_of_pocket": round(oop)
    }