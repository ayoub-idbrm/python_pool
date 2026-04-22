import sys
try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
    from typing import Optional
    from enum import Enum
    from datetime import datetime
except ImportError:
    print("missing ...")
    sys.exit(1)


class contact_type(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: contact_type
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("The Contact ID must start with 'AC'")
        if self.contact_type == contact_type.physical and not self.is_verified:
            raise ValueError("The Physical contact reports must be verified")
        if self.contact_type == contact_type.telepathic \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic Contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self

    def __str__(self):
        return (f"ID: {self.contact_id}\n"
                f"Type: {self.contact_type.value}\n"
                f"Location: {self.location}\n"
                f"Signal: {self.signal_strength}/10\n"
                f"Duration: {self.duration_minutes} minutes\n"
                f"Witnesses: {self.witness_count}\n"
                f"Message: '{self.message_received}'\n")


def main():
    print("Alien Contact Log Validation")
    print("=" * 35)

    try:
        res = AlienContact(
            contact_id="AC_2024_001",
            contact_type="radio",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(res)
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print("-", err["msg"])

    print("=" * 35)

    try:
        _ = AlienContact(
            contact_id="AC_2024_002",
            contact_type="telepathic",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as a:
        print("Expected validation error:")
        for err in a.errors():
            print(err["msg"].split(',')[-1].strip())


if __name__ == "__main__":
    main()
