"""
Create a class that contains at least following methods:

It should have a method to take and store a 'buyer'
A buyer will have
    A name (str)
    A lower limit price (int)
    An upper limit price(int)
    A list of locations - being a US state (str) NY, PA, TX, etc that they wish to buy in.
    A list of Industries IDs (ints) that represent areas that they want to buy into

It should have a method to take and store a 'seller'
A seller will have:
    A name (str)
    A selling price (int)
    A location - a US state - where the seller is located
    A list of Industries IDs (ints) that represent areas that they operate in

It should have a method that examines the set of all buyers and will return a dictionary with the following key - values:
    {
        'low': Lowest seller price (int)
        'high': Highest seller price (int)
        'average': Average Seller Price (int)
        'media': Median Seller Price (int)
    }

It should have a method that examines the set of all buyers and returns a dictionary with the following key - values:
    {
        'low': Lowest buyer limit (int)
        'high': Highest buyer limit (int)
        'wide': Widest buyer range (int) EX: low of 100 and high of 500 would be range of 400
        'narrow': Most narrow buyer range (int)
    }

It should have a method that will, given a seller's name, return the names of all the compatible buyers.
A compatible buyer is one that:
    Has a matching geography in their geography list
    Has a lower limit lower than the seller's price
    Has an upper limit higher than the seller's
    Has at least one Industry that matches exactly, or is a parent of, any of the seller's industries

It should have a method that will, given a buyer's name, return hte names of all compatible sellers.
A compatible seller is one that:
    Has a geography matching one of the buyers locations
    Has a price higher than the buyer's lower limit
    Has a price lower than the buyer's upper limit
    Has an industry that matches exactly or is a child of any of the buyer's industries

A method that will execute a transaction. Given a sellers and buyers name,
it will remove both from the system.

Notes:
    Please use python3.
    This exercise is designed to be completed within 2-4 hours.
    This file requires `industries.csv` to load the industries.
    It is desirable to optimize requests for performance. Speed is important.
    Please include a basic set of tests.

    All names given will be unique and will not contain special characters.
    Only valid industry IDs will be given.

    You may use extra libraries. If you do, please include a requirements.txt file.
"""
import csv
import statistics

INDUSTRY_INDEX = {}


class IndustryNode:
    """
    Basic container object for industry nodes. Feel free to add to this object
    """
    def __init__(self, node_id: int, parent_id: int, tree_path: set, children_ids: set):
        # Unique ID for node
        self.node_id = node_id
        # The parent of the current node - If None, then it at the top of the tree
        self.parent_id = parent_id
        # The set of nodes that are parents of this node to the top of the tree, including self
        self.tree_path = tree_path
        # The set of nodes that are children of this node, including self
        # childen_ids set only containing self means the tail branch of the industry tree
        self.children_ids = children_ids


# Read in nodes and build industry index
with open('industries.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|')
    for row in csv_reader:
        new_node = {
            'node_id': int(row[0]),
            'parent_id': int(row[1]) if row[1] else None,  # If None, then it is a top of tree
            'tree_path': eval(row[2]),
            'children_ids': eval(row[3])
        }
        INDUSTRY_INDEX[new_node['node_id']] = IndustryNode(**new_node)


def get_industry_node(node_id: int):
    """ Use this function to get any industry by id """
    return INDUSTRY_INDEX.get(node_id)


class TakeHome:
    def __init__(self):
        """ Initializes a dictionary for sellers, their stats, and one
        each for buyers and their stats"""
        self.sellers = {}
        self.seller_stats = {}
        self.buyers = {}
        self.buyer_stats = {}

    def _calc_seller_stats(self) -> None:
        """ Updates self.sellers to reflect current lowest, highest, average,
        and median selling prices. """
        # create a list of just the price information
        selling_prices = [seller[0] for seller in self.sellers.values()]
        # update dictionary
        self.seller_stats = {
            'low': min(selling_prices),
            'high': max(selling_prices),
            'average': statistics.mean(selling_prices),
            'median': statistics.median(selling_prices)
        }

    def _calc_buyer_stats(self) -> None:
        """ Updates the buyer_stats dictionary to track current lowest
        of all lower limits, highest of all upper limits, and then calculate
        the difference between each buyer's individual upper and lower limit,
        storing the largest difference as widest spread, and the smallest
        difference as narrowest. """
        #  these are different lists so it seems more readable to assign
        #  then make the dictionary, it also assumes lowest lower limit is
        # lower than lowest upper limit, but I think this is safe.
        low = min([buyer[0] for buyer in self.buyers.values()])
        high = max([buyer[1] for buyer in self.buyers.values()])
        #  the next two will be acting upon the same list
        spread = [(buyer[1] - buyer[0]) for buyer in self.buyers.values()]
        wide = max(spread)
        narrow = min(spread)
        # update dictionary
        self.buyer_stats = {
            'low': low,
            'high': high,
            'wide': wide,
            'narrow': narrow
        }

    def add_seller(
        self,
        name: str,
        selling_price: int,
        geography: str,
        industries: [int]
    ) -> None:
        """ Adds a seller with their name, selling price, geography which is
        the US state they are located in, and list of industries.
        In addition, recalculates the overall seller stats."""
        self.sellers.setdefault(name, (selling_price, geography, industries))
        self._calc_seller_stats()

    def add_buyer(
        self, name: str,
        lower_limit: int,
        upper_limit: int,
        geographies: [str],
        industries: [int]
    ) -> None:
        """ Adds a buyer with the name, lower limit on price, upper limit on
        price, a list of US states they're willing to buy from, and the
        industries that are relevant to them. Once that's done, recalculate
        the stats based on this new version. """
        self.buyers.setdefault(
            name, (lower_limit, upper_limit, geographies, industries)
        )
        self._calc_buyer_stats()

    def get_seller_stats(self) -> {}:
        """ From the set of all sellers, gets the lowest, highest, average,
        and median selling prices. """
        return self.seller_stats

    def get_buyer_stats(self) -> {}:
        """ From the set of all buyers, gets the lowest lower limit on price,
        the highest upper limit on price, and then the widest (greatest
        difference) and narrowest (lowest difference) spread of each buyer's
        upper and lower price limits. """
        return self.buyer_stats

    def seller_recommendations(self, name: str) -> [str]:
        """ Given a seller's name, return the names of all the compatible
        buyers. A compatible buyer is one that:
        Has a matching geography in their geography list.
        Has a lower limit lower than the seller's price.
        Has an upper limit higher than the seller's
        Has at least one Industry that matches exactly, or is a parent of,
        any of the seller's industries. """
        compatible_buyers = []
        seller = self.sellers[name]
        # loop through the buyer dictionary
        for buyer in self.buyers:
            current_buyer = self.buyers[buyer]
            # check location
            if seller[1] in current_buyer[2]:
                # check limits
                if current_buyer[0] <= seller[0] <= current_buyer[1]:
                    # check industries
                    if seller[2] in current_buyer[3]:
                        # add name, note that this is buyer not current_buyer
                        compatible_buyers.append(buyer)
                    # check child industries only if no industry match
                    elif seller[2] in [
                        get_industry_node(industry)['children_ids']
                        for industry in current_buyer[3]
                    ]:
                        # add name, note that this is buyer not current_buyer
                        compatible_buyers.append(buyer)  # add name
        return compatible_buyers  # return the now-full list

    def buyer_recommendations(self, name: str) -> [str]:
        """ Given a buyer's name, return the names of all compatible sellers.
        A compatible seller is one that:
        Has a geography matching one of the buyers locations
        Has a price higher than the buyer's lower limit
        Has a price lower than the buyer's upper limit
        Has an industry that matches exactly or is a child of any of the
        buyer's industries. """
        buyer = self.buyers[name]
        compatible_sellers = []
        # loop through sellers dict
        for seller in self.sellers:
            current_seller = self.sellers[seller]
            # check location
            if current_seller[1] in buyer[2]:
                # check limits
                if buyer[0] <= current_seller[0] <= buyer[1]:
                    # check industries
                    if current_seller[2] in buyer[3]:
                        # add name, note this is seller not current_seller
                        compatible_sellers.append(seller)
                        # check child industries only if no industry match
                    elif current_seller[2] in [
                        get_industry_node(industry)['children_ids']
                        for industry in current_buyer[3]
                    ]:
                        # add name, note this is seller not current_seller
                        compatible_sellers.append(seller)
        return compatible_sellers  # return now-full list

    def transact(self, buyer_name: str, seller_name: str) -> None:
        """ Given a sellers and buyers name, it will remove both
        from the system. """
        # check to make sure both exist first
        if buyer_name in self.buyers and seller_name in self.sellers:
            del self.buyers[buyer_name]
            del self.sellers[seller_name]
            self._calc_seller_stats()
            self._calc_buyer_stats()
        else:
            print(
                'Either buyer or seller not found. No transaction performed.'
            )
