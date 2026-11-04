# Salon and spa bookkeeping kit

Bookkeeping for a salon or spa keeps card tips as money owed to staff, books
booth rent as income, separates retail product sales from services, holds gift
cards as a liability until they are used, and grosses each card deposit back
up before processor fees. This kit has the accounts, a checklist and a
worked month that ties.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart of accounts for a salon or spa: service, retail and booth rent income, tips payable, gift cards outstanding, backbar supplies apart from retail cost. Columns: Number, Name, Type, Detail, Notes. |
| `month-end-checklist.md` | Ten steps for closing a salon's month, from pulling card deposits apart to locking the period. |
| `card-deposits.csv` | A fictional month of card deposits, one row per week, each grossed up into services, retail and tips with the processor fee on its own column. |
| `october-2026-month.csv` | The same fictional salon's October 2026 on cash basis: every line, the account it goes to, and whether it counts in profit. |
| `check_salon_month.py` | Checks that every deposit reads across, that tips payable nets to zero, that deposits agree with the month, and prints revenue, expenses and profit. Python 3, standard library only. |

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or use it as
   a list to compare with the accounts you already have. Delete booth rent if
   you have no renters and the gift card lines if you don't sell them.
2. Each month, export the booking system's sales and tips summary and fill in
   a copy of `card-deposits.csv` from your processor statement.
3. Run the check:

   ```
   python3 check_salon_month.py card-deposits.csv october-2026-month.csv
   ```

4. Work through `month-end-checklist.md` before you lock the month.

## The worked month

Juniper Hair Studio is a fictional salon with commission stylists and three
booth renters. October 2026, cash basis:

| | Amount |
|---|---|
| Card services | 28,400.00 |
| Card retail | 3,600.00 |
| Cash services | 1,850.00 |
| Booth rent, 3 renters at 900.00 | 2,700.00 |
| **Revenue** | **36,550.00** |
| Processor fees, 2.8% of 36,200.00 card volume | 1,013.60 |
| Retail restock | 1,450.00 |
| Backbar color and supplies | 960.00 |
| Stylist wages and commissions, gross | 14,300.00 |
| Employer payroll taxes | 1,093.95 |
| Rent | 4,500.00 |
| **Expenses** | **23,317.55** |
| **Profit** | **13,232.45** |

Card tips of 4,200.00 came in with the card sales and went out through
payroll, so they sit in tips payable and never touch profit. The card volume
the processor charges on (36,200.00) includes those tips, which is why the fee
is worked out on more than the card sales.

All figures are fictional.

## FAQ

### Are card tips salon revenue?

No. Tips added on a card belong to the staff member. They land in your account
with the sale, sit in tips payable, and go out to staff through payroll. Booked
as revenue, the month looks better than it was and payroll looks worse.

### Is booth rent income for the salon?

Yes. Renters pay you to use a chair or room, and that rent is salon income,
recorded apart from service sales. Whether a stylist is a renter or an
employee depends on how the arrangement actually works; that is a question for
your accountant.

### When does a gift card become revenue?

When it is redeemed. A gift card sold in December is a service you owe later,
so it sits in gift cards outstanding until the client uses it. Prepaid
packages and memberships work the same way.

## Learn more

Full guide: [Bookkeeping for salons and spas](https://www.zerabooks.com/bookkeeping-for-salons-and-spas). Related: [ZeraBooks bookkeeping services](https://www.zerabooks.com/bookkeeping-services).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
