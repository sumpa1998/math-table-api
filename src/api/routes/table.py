from fastapi import APIRouter
from src.core.table_calculator import TableCalculator


class ProcessTable:
    """API routes for processing math tables."""
    def __init__(self):
        super().__init__()
        self.table_calculator = TableCalculator()
        self.router = APIRouter(prefix="", tags=["Math Table"])

        self.router.add_api_route(
            path="/table",
            endpoint=self.process_table,   
            methods=["GET"],
            summary="Process a math table for a given number",
            response_description="Multiplication table as a list of integers"
        )

    async def process_table(self, number: int ):
        table_result = await self.table_calculator.calculate(number)
        return table_result