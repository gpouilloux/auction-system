from auction import Auction
from auction_house import AuctionHouse
from item import Item
from participant import Participant
import logging

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)


# Main test - auction house scenario
def main():
    auction_house = AuctionHouse()

    guillaume = Participant("Guillaume")
    antonin = Participant("Antonin")

    painting_name = "Van Gogh's painting"
    painting = Item(painting_name, 1000)
    auction_painting = Auction(painting)

    auction_house.add_auction(auction_painting)
    # should fail - auction already added
    auction_house.add_auction(auction_painting)

    # auction has not been started yet
    guillaume.bid(auction_painting, 101)

    auction_painting.start()

    guillaume.bid(auction_painting, 101)
    antonin.bid(auction_painting, 999)
    # guillaume should bid more than 999
    guillaume.bid(auction_painting, 102)

    auction_painting.stop()

    logging.info(auction_house.latest_auction_by_item_name(painting_name))

if __name__ == '__main__':
    main()
