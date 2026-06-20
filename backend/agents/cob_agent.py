from mock_api.insurer1 import PLAN_A
from mock_api.insurer2 import PLAN_B


def calculate_claim(
    total_cost,
    primary_plan,
    secondary_plan
):

    deductible = primary_plan["deductible"]

    remaining = total_cost - deductible

    primary_paid = remaining * primary_plan["coinsurance"]

    patient_balance = remaining - primary_paid

    secondary_paid = (
        patient_balance *
        secondary_plan["coinsurance"]
    )

    out_of_pocket = (
        patient_balance -
        secondary_paid
    )

    return {
        "total_cost": total_cost,
        "primary_paid": round(primary_paid),
        "secondary_paid": round(secondary_paid),
        "out_of_pocket": round(out_of_pocket)
    }


def coordinate_benefits():

    aarav = calculate_claim(
        450000,
        PLAN_B,
        PLAN_A
    )

    priya = calculate_claim(
        30000,
        PLAN_A,
        PLAN_B
    )

    return {
        "aarav": aarav,
        "priya": priya,
        "family_total_oop":
            aarav["out_of_pocket"] +
            priya["out_of_pocket"]
    }