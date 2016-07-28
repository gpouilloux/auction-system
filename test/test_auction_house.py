import unittest

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


if __name__ == '__main__':
    unittest.main()
