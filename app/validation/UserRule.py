""" UserRule Validation Enclosure """

from masonite.validation import RuleEnclosure, required


class UserRule(RuleEnclosure):
    """UserRule Validation Enclosure Class."""

    def rules(self):
        """Used to return a list of rules in order to make validation
        more reusable.

        Returns:
            list -- List of rules
        """
        return [
            required(['name', 'email', 'password'])
        ]
