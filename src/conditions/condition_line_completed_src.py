#  from parameters import PARAMETERS


class ConditionLineCompleted:
    def __init__(self):
        self.next_site = None
        self.site_changer = False

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        return bool(detailed_description["bulk"].get_complete_lines())

    @staticmethod
    def treat(tick, detailed_description, incoming):
        detailed_description["score"] += (
            detailed_description["bulk"].clean_complete_lines_and_return_score())

    def get_known_next_site(self):
        if self.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")

