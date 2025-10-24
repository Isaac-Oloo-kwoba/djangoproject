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