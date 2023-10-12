from fastapi import APIRouter, Path
from asyncio import gather
from converter import async_converter
from schamas import ConverterInput, ConverterOutput
router = APIRouter()

@router.get('/converter/{from_currency}', response_model=ConverterOutput)
async def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$')

):

    to_currencies = body.to_currencies
    price = body.price

    couroutines =  []

    for currency in to_currencies:
        coro =  async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        couroutines.append(coro)

    result = await gather(*couroutines)

    return ConverterOutput(
        message='sucess',
        data=result
    )