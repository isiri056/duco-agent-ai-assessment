import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from agents.preauth_agent import (
    generate_preauth_letters
)

result = generate_preauth_letters()

print(result["aarav_letter"])

print("\n" + "=" * 80 + "\n")

print(result["priya_letter"])