import faust as f

app=f.App('nuApp',broker='kafka://10.0.0.10')

class Order(f.Record):
    account_id: str
    amount: int

@app.agent(value_type=Order)
async def order(orders):
    async for order in orders:
        print(f'Order for {order.account_id}: {order.amount}')
