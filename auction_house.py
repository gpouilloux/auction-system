import uuid
import logging

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)


class AuctionHouse:
    def __init__(self):
        self.id = uuid.uuid1()
        self.auctions = []

    def add_auction(self, auction):
        existing_auctions = filter(lambda a: a.id == auction.id, self.auctions)
        if existing_auctions:
            logging.error("Auction {} has already been "
                          "added to the auction house".format(auction.id))
        else:
            self.auctions.append(auction)

    def latest_auction_by_item_name(self, name):
        auction = filter(lambda a: a.item.name == name, self.auctions)[-1]
        if auction is None:
            status = "The item {} has no auctions".format(name)
        else:
            status = "The latest auction for the item {} is \n".format(name)
            if auction.has_failed:
                status += "Auction for item {} did not " \
                          "reach the reserved price {}" \
                    .format(name, auction.item.reserved_price)
            else:
                if auction.is_started:
                    status += "{} leads the auction with " \
                              "the amount {}" \
                        .format(auction.highest_bid.bidder.name,
                                auction.highest_bid.amount)
                else:
                    status += "{} has been sold to {} " \
                              "for the amount {}" \
                        .format(name,
                                auction.highest_bid.bidder.name,
                                auction.highest_bid.amount)
        return status
