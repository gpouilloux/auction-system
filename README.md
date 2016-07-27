# Auction system

### How to use

**TODO**

### Specifications

Write a backend library for auction house for their online auction system.

The system supports the following operations:

1. Auctioneer adds an item that can be auctioned. An item has a unique
name and reserved price.

2. Auctioneer starts an auction on an item

3. Participants submit bids to an auction, a new bid has to have a
price higher than the current highest bid otherwise it's not allowed.

4. Auctioneer calls the auction (when s/he makes the judgement on her
own that there will be no more higher bids coming in). If the current
highest bid is higher than the reserved price of the item, the auction
is deemed as a success otherwise it's marked as failure. The item sold
should be no longer available for future auctions.

5. Participant/Auctioneer queries the latest action of an item by item
name. The library should return the status of the auction if there is
any, if the item is sold, it should return the information regarding
the price sold and to whom it was sold to.
