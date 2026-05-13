class TableCalculator:
    """A calculator that generates multiplication tables."""
    async def calculate(self, number: int, limit: int = 10) -> list[int]:
        return [number * i for i in range(1, limit + 1)]