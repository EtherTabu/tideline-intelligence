# =====================================================
# TIDE LINE — SYSTEM VALIDATOR
# =====================================================

import copy


# =====================================================
# VALIDATE CONTRACT
# =====================================================

def validate_contract(

    data,
    contract

):

    # =================================================
    # SAFETY
    # =================================================

    if not isinstance(data, dict):

        return copy.deepcopy(contract)

    # =================================================
    # START WITH REAL DATA
    # =================================================

    validated = copy.deepcopy(data)

    # =================================================
    # APPLY CONTRACT DEFAULTS
    # =================================================

    for key, default_value in contract.items():

        # =============================================
        # KEY MISSING
        # =============================================

        if key not in validated:

            validated[key] = copy.deepcopy(
                default_value
            )

            continue

        # =============================================
        # NESTED CONTRACTS
        # =============================================

        if (

            isinstance(default_value, dict)

            and

            isinstance(validated.get(key), dict)

        ):

            validated[key] = validate_contract(

                validated[key],
                default_value

            )

    # =================================================
    # RETURN VALIDATED STRUCTURE
    # =================================================

    return validated
