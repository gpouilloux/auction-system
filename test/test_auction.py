import unittest

from auction_system.auction import Auction
from auction_system.item import Item
from auction_system.participant import Participant


class TestAuction(unittest.TestCase):

    def setUp(self):
        self.auction = Auction(Item("Van Gogh's painting", 1000))

    def tearDown(self):
        self.auction = None

    # Start an auction
    # OK Test
    def testStart(self):
        self.auction.start()
        self.assertTrue(self.auction.is_started)

    # Stop an auction which was not started
    # KO Test
    def testStopFail(self):
        self.auction.stop()
        self.assertFalse(self.auction.is_started)
        self.assertFalse(self.auction.has_failed)
        self.assertIsNone(self.auction.highest_bid)

    # Stop an auction without bids
    # KO Test
    def testStopAuctionFailed(self):
        self.auction.start()
        self.auction.stop()
        self.assertFalse(self.auction.is_started)
        self.assertTrue(self.auction.has_failed)
        self.assertIsNone(self.auction.highest_bid)

    # Stop an auction with a bid's price higher than
    # the reserved price.
    # OK Test
    def testStopAuctionSuccess(self):
        self.auction.start()
        guillaume = Participant("Guillaume")

        guillaume.bid(self.auction, 1001)

        self.auction.stop()
        self.assertFalse(self.auction.is_started)
        self.assertFalse(self.auction.has_failed)


if __name__ == '__main__':
    unittest.main()
