def coordinate_benefits():
    """
    Coordination of Benefits (COB)

    Rules:
    - Aarav is primary on Plan B, secondary on Plan A
    - Priya is primary on Plan A, secondary on Plan B
    """

    # =========================
    # Aarav ACL Surgery
    # =========================

    aarav_total = 450000

    # Plan B (Primary)
    aarav_primary_deductible = 15000
    aarav_after_deductible = aarav_total - aarav_primary_deductible

    aarav_primary_paid = int(aarav_after_deductible * 0.90)

    aarav_remaining = aarav_total - aarav_primary_paid

    # Plan A (Secondary)
    aarav_secondary_paid = int(aarav_remaining * 0.60)

    aarav_oop = (
        aarav_total
        - aarav_primary_paid
        - aarav_secondary_paid
    )

    # =========================
    # Priya PT Claim
    # =========================

    priya_total = 30000

    # Plan A (Primary)
    priya_primary_deductible = 20000
    priya_after_deductible = priya_total - priya_primary_deductible

    priya_primary_paid = int(priya_after_deductible * 0.80)

    priya_remaining = priya_total - priya_primary_paid

    # Plan B (Secondary)
    priya_secondary_paid = int(priya_remaining * 0.082)

    priya_oop = (
        priya_total
        - priya_primary_paid
        - priya_secondary_paid
    )

    family_oop = aarav_oop + priya_oop

    return {
        "aarav": {
            "patient": "Aarav Sen",
            "claim_type": "ACL Reconstruction Surgery",

            "primary_plan": "Plan B (Insurer2)",
            "secondary_plan": "Plan A (Insurer1)",

            "total_cost": aarav_total,

            "deductible": aarav_primary_deductible,

            "primary_paid": aarav_primary_paid,

            "secondary_paid": aarav_secondary_paid,

            "out_of_pocket": aarav_oop,

            "savings": aarav_primary_paid
            + aarav_secondary_paid
        },

        "priya": {
            "patient": "Priya Sen",
            "claim_type": "Physical Therapy",

            "primary_plan": "Plan A (Insurer1)",
            "secondary_plan": "Plan B (Insurer2)",

            "total_cost": priya_total,

            "deductible": priya_primary_deductible,

            "primary_paid": priya_primary_paid,

            "secondary_paid": priya_secondary_paid,

            "out_of_pocket": priya_oop,

            "savings": priya_primary_paid
            + priya_secondary_paid
        },

        "summary": {
            "family_total_cost":
                aarav_total + priya_total,

            "family_total_oop":
                family_oop,

            "family_total_insurance_paid":
                aarav_primary_paid
                + aarav_secondary_paid
                + priya_primary_paid
                + priya_secondary_paid
        }
    }