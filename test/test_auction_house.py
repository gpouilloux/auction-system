import unittest
import logging

from auction_system.participant import Participant

logging.getLogger().setLevel(logging.INFO)

from auction_system.auction import Auction
from auction_system.auction_house import AuctionHouse
from auction_system.item import Item


class TestAuctionHouse(unittest.TestCase):

    def setUp(self):
        self.auction_house = AuctionHouse()

    def tearDown(self):
        self.auction_house = None

    def testAddAuctionSuccess(self):
        auction = Auction(Item("Van Gogh's painting", 1000))
        self.auction_house.add_auction(auction)
        self.assertListEqual(self.auction_house.auctions, [auction])

    def testAddAuctionFailure(self):
        auction = Auction(Item("Van Gogh's painting", 1000))
        self.auction_house.add_auction(auction)
        self.auction_house.add_auction(auction)
        self.assertListEqual(self.auction_house.auctions, [auction])

    def testLatestAuctionStopped(self):
        auction = Auction(Item("Van Gogh's painting", 1000))
        self.auction_house.add_auction(auction)
        auction.start()
        auction.stop()
        logging.info(self.auction_house.latest_auction_by_item_name("Van Gogh's painting"))

    def testLatestAuctionStartedWithoutBidder(self):
        auction = Auction(Item("Van Gogh's painting", 1000))
        self.auction_house.add_auction(auction)
        auction.start()
        logging.info(self.auction_house.latest_auction_by_item_name("Van Gogh's painting"))

    def testLatestAuctionStartedWithBidder(self):
        auction = Auction(Item("Van Gogh's painting", 1000))
        self.auction_house.add_auction(auction)
        auction.start()
        guillaume = Participant("Guillaume")
        guillaume.bid(auction, 1001)
        logging.info(self.auction_house.latest_auction_by_item_name("Van Gogh's painting"))


if __name__ == '__main__':
    unittest.main()
