# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.quality_change_per_day = {
            "Aged Brie": 1,
            "Backstage passes to a TAFKAL80ETC concert": {
                'ten_or_less': 2,
                'five_or_less': 3,
            },
            "Conjured Mana Cake": -2,
            "Sulfuras, Hand of Ragnaros": 0,
        }
        self.sell_in_change_per_day = {
            "Sulfuras, Hand of Ragnaros": 0,
        }

    def update_quality(self):
        for item in self.items:
            item.sell_in += self.sell_in_change_per_day.get(item.name, -1)
            self.incrementally_change_quality_of_item(item)
            if item.sell_in < 0:
                self.incrementally_change_quality_of_item(item)

    def incrementally_change_quality_of_item(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 0:
                item.quality = 0
            elif item.sell_in <= 5:
                item.quality += self.quality_change_per_day[item.name]['five_or_less']
            elif item.sell_in <= 10:
                item.quality += self.quality_change_per_day[item.name]['ten_or_less']
        else:
            item.quality += self.quality_change_per_day.get(item.name, -1)

        item.quality = max(item.quality, 0)
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = min(item.quality, 50)    


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
