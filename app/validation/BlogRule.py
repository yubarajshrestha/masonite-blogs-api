""" BlogRule Validation Enclosure """

from masonite.validation import RuleEnclosure, required


class BlogRule(RuleEnclosure):
    """BlogRule Validation Enclosure Class."""

    def rules(self):
        """Used to return a list of rules in order to make validation
        more reusable.

        Returns:
            list -- List of rules
        """
        return [
            required(["title", "slug", "excerpt", "content", "categories", "status"])
        ]
