"""

10. Smart Restaurant Order Processing System

A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

If order amount is at least 2000, then check customer type. If VIP, then check payment method. If online, give free dessert and 20 percent discount; otherwise only free dessert. If not VIP, then check if amount is at least 5000. If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; otherwise 5 percent discount. If below 1000, no offer.

Input:
Order Amount = 2500
Customer Type = VIP
Payment Method = online

Output:
Offer = Free Dessert + 20% Discount
"""

o=int(input("Order Amount ="))
c=input("Customer type =").lower()
p=input("Payment Method =").lower()

if o>=2000:
    if c=='vip':
        if p=='online':
            print("Offer = Free Dessert and 20% discount")
        else:
            print("Offer = only free dessert")
    else:
        if o>=5000:
            print("Offer = 15% discount")
        else:
            print("Offer = 10% discount")
else:
    if o>=1000:
        if c=='vip':
            print("Offer = 10% discount")
        else:
            print("Offer = 5% discount")

