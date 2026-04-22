try:
    from enum import Enum
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from datetime import datetime
except ImportError as e:
    print(f"ERROR: {e}")


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if Rank.COMMANDER not in [i.rank for i in self.crew] \
                and Rank.CAPTAIN not in [i.rank for i in self.crew]:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365 and (len(self.crew)/2) >= \
                len([i.years_experience for i in self.crew
                    if i.years_experience >= 5]):
            raise ValueError(
                "Long missions (> 365 days) need 50% \
                    experienced crew (5+ years)")
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 35)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                ),
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for a in mission.crew:
            print(f"- {a.name} ({a.rank.value}) - {a.specialization}")
        print()
        print("=" * 35)

    except ValidationError as a:
        for err in a.errors():
            print("-", err["msg"])

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.LIEUTENANT,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                ),
            ],
            budget_millions=2500.0
        )
    except ValidationError as a:
        print("Expected validation error:")
        for err in a.errors():
            print("-", err["msg"].split(',')[-1].strip())


if __name__ == "__main__":
    main()
