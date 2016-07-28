import logging
import uuid

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)


# A participant can submit a bid if the auction is started
# and if the bid's price is higher than the current highest price
class Bid:
    def __init__(self, bidder, auction, amount):
        if not auction.is_started:
            logging.warning("Auction {} has not been started yet. "
                            "Bid is not allowed".format(auction.id))
        elif auction.highest_bid is not None \
                and auction.highest_bid.amount >= amount:
            logging.error("A new bid has to have a price higher than "
                          "the current highest bid.")
        else:
            self.id = uuid.uuid1()
            self.bidder = bidder
            self.amount = amount
            self.auction = auction
            self.auction.highest_bid = self
            logging.info("{} bids {} for auction {}".format(bidder.name,
                                                            amount,
                                                            auction.id))
