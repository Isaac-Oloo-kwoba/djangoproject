def transfer_funds(db,sender_id: int, receiver_id: int, amount: float):
    sender = db.query(Account).filter_by(id=sender_id).with_for_update().one()
    receiver = db.query(Account).filter_by(id=receiver_id).with_for_update().one()

    if sender.balance < amount:
        raise ValueError("Insufficient funds")

    sender.balance -= amount
    receiver.balance += amount

    tx = Transaction(sender_id=sender_id, receiver_id=receiver_id, amount=amount)
    db.add(tx)
    db.commit()
    return tx


try:
    transaction = transfer_funds(session, 101, 202, 50.00)
    print(f"Transaction successful! ID: {transaction.id}")
except ValueError as e:
    print(f"Transfer failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")