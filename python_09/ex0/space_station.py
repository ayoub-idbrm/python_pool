import sys
try:
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
    from typing import Optional
except ImportError as j:
    print(f"missing...{j}")
    sys.exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

    def __str__(self):
        status = 'operational' if self.is_operational else 'Non-operational'
        return (f"ID: {self.station_id}\n"
                f"Name: {self.name}\n"
                f"Crew: {self.crew_size} people\n"
                f"Power: {self.power_level}%\n"
                f"Oxygen: {self.oxygen_level}%\n"
                f"Status: {status}\n")


def main():
    print("Space Station Data Validation")
    print("=" * 35)
    try:
        result = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now())
        print("Valid station created:")
        print(result)
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print("-", err["msg"])
    print("=" * 35)
    try:
        _ = SpaceStation(
            station_id="IS002",
            name="second International space station",
            crew_size=35,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as a:
        print("Expected validation error:")
        for err in a.errors():
            print(err["msg"].split(".")[-1].strip())


if __name__ == "__main__":
    main()
