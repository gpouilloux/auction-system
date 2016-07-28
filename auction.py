import uuid
import logging

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)


class Auction:
    def __init__(self, item):
        self.id = uuid.uuid1()
        self.item = item
        self.is_started = False
        self.has_failed = False
        self.highest_bid = None

    # An auction can be started if it has not already failed
    def start(self):
        if self.has_failed:
            logging.error("Auction {} has already failed and "
                          "can't be started.".format(self.id))
        else:
            self.is_started = True
            logging.info("Auction {} has been started".format(self.id))

    # An auction can be stopped if it's started
    # If the reserved price is not met, the auction is tagged as failed
    def stop(self):
        if self.is_started:
            if self.item.reserved_price > self.highest_bid.amount:
                self.has_failed = True
                logging.warning("Auction {} did not reach "
                                "the reserved price".format(self.id))
            self.is_started = False
            logging.info("Auction {} has been stopped".format(self.id))
        else:
            logging.error("Auction {} is not started. "
                          "You can't stop it.".format(self.id))
