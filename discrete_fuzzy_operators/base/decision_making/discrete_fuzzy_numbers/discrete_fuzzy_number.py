import collections
import plotly.express as plot_express
import plotly.graph_objects as go

from discrete_fuzzy_operators.base.exceptions.decision_making.discrete_fuzzy_numbers.dfn_bad_dimension import \
    DiscreteFuzzyNumberBadDimension
from discrete_fuzzy_operators.base.exceptions.decision_making.discrete_fuzzy_numbers.dfn_membership_out_bounds import \
    DiscreteFuzzyNumberMembershipOutOfBounds
from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteAggregationBinaryOperator
from numpy import linspace
from typing import Callable, Dict, List, Set, Tuple


class DiscreteFuzzyNumber:

    # region Main methods
    def __init__(self, fuzzy_number: Dict, n: int):
        self.n = n
        self.fuzzy_number = DiscreteFuzzyNumber.__clean_fuzzy_number(fuzzy_number)

    @staticmethod
    def __clean_fuzzy_number(fuzzy_number: Dict) -> Dict:
        """
        Remove all elements of the support that have membership function equal to zero. By convention, the discrete
        fuzzy number must represent only values that are strictly greater than zero.

        Args:
            fuzzy_number: A dictionary, representing the function that defines the discrete fuzzy number.

        Returns:
            A dictionary, representing the function that defines the initial discrete fuzzy number without the values
            which have null membership function.
        """
        new_fuzzy_number = {}
        for x in fuzzy_number.keys():
            if not 0 <= fuzzy_number[x] <= 1:
                raise DiscreteFuzzyNumberMembershipOutOfBounds()
            if fuzzy_number[x] != 0:
                new_fuzzy_number[x] = fuzzy_number[x]
        return collections.OrderedDict(sorted(new_fuzzy_number.items()))

    def __str__(self):
        return str(dict(self.fuzzy_number))

    @property
    def membership_values(self) -> List[float]:
        """
        Returns the membership values as a list of floats.
        """
        return list(self.fuzzy_number.values())
    # endregion

    # region Utils
    def cut(self, alpha: float) -> Set:
        """
        Computes the cuts of the discrete fuzzy number.

        Args:
            alpha: A float value between 0 and 1, which represents the membership function value to be cutted.

        Returns:
            A set, containing the vallues in the finite chain Ln such that its membership function is greather than
            the input threshold.
        """
        if not 0 <= alpha <= 1:
            raise DiscreteFuzzyNumberMembershipOutOfBounds()

        return set([x for x in self.fuzzy_number.keys() if self.fuzzy_number[x] >= alpha])

    def support(self) -> Set:
        """
        Computes the support of the discrete fuzzy number. Since by convention the values have been filtered to be
        strictly greater than zero, the keys of the dictionary is returned.

        Returns:
            A set, containing the values in the finite chain Ln such that its membership function is not null.
        """
        return self.cut(alpha=0)

    @staticmethod
    def plot_discrete_fuzzy_numbers(discrete_fuzzy_numbers: ["DiscreteFuzzyNumber"],
                                    discrete_fuzzy_numbers_titles: [str] = None,
                                    figure_size: Tuple[int, int] = (900, 600),
                                    figure_title: str = "Fuzzy discrete numbers"):
        """
        Given a list of discrete fuzzy numbers, plots them together in the same figure with different colours.

        Args:
            discrete_fuzzy_numbers: A list of DiscreteFuzzyNumber objects.
            discrete_fuzzy_numbers_titles: A list of strings, optional, representing the labels to be shown to each
                                           discrete fuzzy number.
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
            figure_title: A string, representing the title of the plot.
        """
        # Check if all discrete fuzzy numbers have the same dimension
        n = discrete_fuzzy_numbers[0].n
        for discrete_fuzzy_number in discrete_fuzzy_numbers:
            if n != discrete_fuzzy_number.n:
                raise DiscreteFuzzyNumberBadDimension()
        ############################################################

        labels = [i for i in range(0, n+1)]
        scatter_items = []
        for idx, discrete_fuzzy_number in enumerate(discrete_fuzzy_numbers):
            new_number = []
            for x in labels:
                if x in discrete_fuzzy_number.fuzzy_number:
                    new_number.append(discrete_fuzzy_number.fuzzy_number[x])
                else:
                    new_number.append(None)

            fuzzy_number_name = ""
            if discrete_fuzzy_numbers_titles is not None:
                fuzzy_number_name = discrete_fuzzy_numbers_titles[idx]

            scatter_items.append(go.Scatter(
                x=labels,
                y=new_number,
                mode="markers",
                name=fuzzy_number_name,
                marker=dict(size=12, color=plot_express.colors.qualitative.Plotly[idx], opacity=0.5)
            ))

        figure = go.Figure(data=scatter_items)
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1],
                             yaxis_range=[0, 1.1],
                             showlegend=True)
        figure.show()

    # endregion

    # region Interaction with other discrete fuzzy number

    # region Minimum
    @staticmethod
    def support_pseudointersection(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber") -> Set:
        """
        Computes the pseudo-intersection of the two supports, also known as wedge operation. The pseudo-intersection
        is defined as the set supp A ^ supp B = {min(x, y) | x in supp A, y in supp B}.

        References:
            Massanet S & Riera JV & Torrens J (2014)
            A new linguistic computational model based on discrete fuzzy numbers for computing with words.
            Information Sciences, Volume 258, Pages 277-290.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.

        Returns:
            A set, representing the pseudo-intersection of the supports of the two discrete fuzzy numbers.
        """
        pseudointersection = set([min(x, y) for x in dfn1.support() for y in dfn2.support()])
        return set(sorted(pseudointersection))

    @staticmethod
    def minimum_cut(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber", alpha: float) -> Set:
        """
        Computes the alpha-cuts of the minimum of two discrete fuzzy numbers.

        References:
            Massanet S & Riera JV & Torrens J (2014)
            A new linguistic computational model based on discrete fuzzy numbers for computing with words.
            Information Sciences, Volume 258, Pages 277-290.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.
            alpha: A float value between 0 and 1, which represents the membership function value to be cutted.

        Returns:
            A set, representing the cut of the minimum with the specified alpha.
        """
        alpha_cut_a = dfn1.cut(alpha)
        alpha_cut_b = dfn2.cut(alpha)

        final_minimum_cuts = []
        for z in DiscreteFuzzyNumber.support_pseudointersection(dfn1, dfn2):
            if min(min(alpha_cut_a), min(alpha_cut_b)) <= z <= min(max(alpha_cut_a), max(alpha_cut_b)):
                final_minimum_cuts.append(z)
        return set(final_minimum_cuts)

    @staticmethod
    def partial_minimum(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber",
                        number_trials: int = 100) -> "DiscreteFuzzyNumber":
        """
        Computes the minimum between two discrete fuzzy numbers. A range of possible alpha values is generated, and for
        each of them the corresponding cut is calculated. This minimum induces a partial order.

        References:
            Massanet S & Riera JV & Torrens J (2014)
            A new linguistic computational model based on discrete fuzzy numbers for computing with words.
            Information Sciences, Volume 258, Pages 277-290.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.
            number_trials: An integer, representing the number of steps to use to generate the range.

        Returns:
            A DiscreteFuzzyNumber object, representing the new discrete fuzzy number.
        """
        minimum_fuzzy_number = {}

        completed_labels = set()
        for alpha in linspace(1, 0, num=number_trials + 1):
            cuts = DiscreteFuzzyNumber.minimum_cut(dfn1, dfn2, alpha)
            new_labels = cuts.difference(completed_labels)

            for new_label in new_labels:
                minimum_fuzzy_number[new_label] = round(alpha, 5)

            completed_labels = completed_labels.union(cuts)

        return DiscreteFuzzyNumber(fuzzy_number=minimum_fuzzy_number, n=dfn1.n)
    # endregion

    # region Maximum
    @staticmethod
    def support_pseudounion(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber") -> Set:
        """
        Computes the pseudo-union of the two supports, also known as vee operation. The pseudo-union
        is defined as the set supp A v supp B = {max(x, y) | x in supp A, y in supp B}.

        References:
            Massanet S & Riera JV & Torrens J (2014)
            A new linguistic computational model based on discrete fuzzy numbers for computing with words.
            Information Sciences, Volume 258, Pages 277-290.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.

        Returns:
            A set, representing the pseudo-union of the supports of the two discrete fuzzy numbers.
        """
        pseudounion = set([max(x, y) for x in dfn1.support() for y in dfn2.support()])
        return set(sorted(pseudounion))

    @staticmethod
    def maximum_cut(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber", alpha: float) -> Set:
        """
        Computes the alpha-cuts of the maximum of two discrete fuzzy numbers.

        References:
            Massanet S & Riera JV & Torrens J (2014)
            A new linguistic computational model based on discrete fuzzy numbers for computing with words.
            Information Sciences, Volume 258, Pages 277-290.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.
            alpha: A float value between 0 and 1, which represents the membership function value to be cutted.

        Returns:
            A set, representing the cut of the maximum with the specified alpha.
        """
        alpha_cut_a = dfn1.cut(alpha)
        alpha_cut_b = dfn2.cut(alpha)

        final_maximum_cuts = []
        for z in DiscreteFuzzyNumber.support_pseudounion(dfn1, dfn2):
            if max(min(alpha_cut_a), min(alpha_cut_b)) <= z <= max(max(alpha_cut_a), max(alpha_cut_b)):
                final_maximum_cuts.append(z)
        return set(final_maximum_cuts)

    @staticmethod
    def partial_maximum(dfn1: "DiscreteFuzzyNumber", dfn2: "DiscreteFuzzyNumber",
                        number_trials: int = 100) -> "DiscreteFuzzyNumber":
        """
        Computes the maximum between two discrete fuzzy numbers. A range of possible alpha values is generated, and for
        each of them the corresponding cut is calculated. This maximum induces a partial order.

        Args:
            dfn1: A DiscreteFuzzyNumber object.
            dfn2: A DiscreteFuzzyNumber object.
            number_trials: An integer, representing the number of steps to use to generate the range.

        Returns:
            A DiscreteFuzzyNumber object, representing the new discrete fuzzy number.
        """
        maximum_fuzzy_number = {}

        completed_labels = set()

        for alpha in linspace(1, 0, num=number_trials + 1):
            cuts = DiscreteFuzzyNumber.maximum_cut(dfn1, dfn2, alpha)
            new_labels = cuts.difference(completed_labels)

            for new_label in new_labels:
                maximum_fuzzy_number[new_label] = round(alpha, 5)

            completed_labels = completed_labels.union(cuts)

        return DiscreteFuzzyNumber(fuzzy_number=maximum_fuzzy_number, n=dfn1.n)
    # endregion

    # region Aggregation with respect to a discrete fuzzy aggregation function
    def aggregate_cut(self,
                      other: "DiscreteFuzzyNumber",
                      discrete_aggregation_function: DiscreteAggregationBinaryOperator,
                      alpha: float) -> Set:
        """
        Computes the alpha-cuts of the aggregation of two discrete fuzzy numbers.

        Args:
            other: Another discrete fuzzy number.
            discrete_aggregation_function: A DiscreteFuzzyAggregationBinaryOperator, representing the discrete
                                           aggregation function to be used in the aggregation.
            alpha: A float value between 0 and 1, which represents the membership function value to be cutted.

        Returns:
            A set, representing the cut of the aggregation with the specified alpha.
        """
        if discrete_aggregation_function.n != self.n:
            raise DiscreteFuzzyNumberBadDimension()

        aggregation_cuts = [discrete_aggregation_function.evaluate_operator(x, y)
                            for x in self.cut(alpha) for y in other.cut(alpha)]

        final_aggregation_cuts = []
        for z in range(self.n+1):
            if min(aggregation_cuts) <= z <= max(aggregation_cuts):
                final_aggregation_cuts.append(z)
        return set(sorted(final_aggregation_cuts))

    def aggregate(self,
                  other: "DiscreteFuzzyNumber",
                  discrete_aggregation_function: DiscreteAggregationBinaryOperator,
                  number_trials: int = 100) -> "DiscreteFuzzyNumber":
        """
        Computes the discrete fuzzy number in the aggregation. A range of possible alpha values is generated, and for
        each of them the corresponding cut is calculated.

        Args:
            other: Another discrete fuzzy number.
            discrete_aggregation_function: A DiscreteFuzzyAggregationBinaryOperator, representing the discrete
                                           aggregation function to be used in the aggregation.
            number_trials: An integer, representing the number of steps to use to generate the range.

        Returns:
            A DiscreteFuzzyNumber object, representing the new discrete fuzzy number.
        """
        aggregation_fuzzy_number = {}

        completed_labels = set()
        for alpha in linspace(1, 0, num=number_trials+1):
            cuts = self.aggregate_cut(other, discrete_aggregation_function, alpha)
            new_labels = cuts.difference(completed_labels)

            for new_label in new_labels:
                aggregation_fuzzy_number[new_label] = round(alpha, 5)

            completed_labels = completed_labels.union(cuts)

        return DiscreteFuzzyNumber(fuzzy_number=aggregation_fuzzy_number, n=self.n)
    # endregion

    # region Total order
    def total_order_equal(self, other: "DiscreteFuzzyNumber") -> bool:
        """
        Computes if two discrete fuzzy numbers are equal following the criteria established in the Riera-Massanet
        total order. Two discrete fuzzy numbers are equal if, for each alpha, the alpha-cuts are equal.

        References:
            Riera JV & Massanet S & Bustince H & Fernandez J (2021).
            On Admissible Orders on the Set of Discrete Fuzzy Numbers for Application in Decision Making Problems.
            Mathematics, Volume 9, Number 1.

        Args:
            other: Another discrete fuzzy number.

        Returns:
            A boolean, indicating if the two discrete fuzzy numbers are equal.
        """
        memberships1 = set(self.membership_values)
        memberships2 = set(other.membership_values)

        for gamma in memberships1.union(memberships2):
            if not self.cut(gamma) == other.cut(gamma):
                return False
        return True

    def total_order_less(self, other: "DiscreteFuzzyNumber",
                         order: Callable[[Tuple[int, int], Tuple[int, int]], bool]) -> bool:
        """
        Computes if the first discrete fuzzy numbers is less strict than the second one following the criteria
        established in the Riera-Massanet total order.

        References:
            Riera JV & Massanet S & Bustince H & Fernandez J (2021).
            On Admissible Orders on the Set of Discrete Fuzzy Numbers for Application in Decision Making Problems.
            Mathematics, Volume 9, Number 1.

        Args:
            other: Another discrete fuzzy number.
            order: A callable method, representing the admissible order applied to two intervals. Returns a boolean
                   indicating if the first interval is less than the second interval.

        Returns:
            A boolean, indicating if the first discrete fuzzy number is less strict than the second one.
        """
        if self.total_order_equal(other):
            return False

        memberships = list(set(self.membership_values).union(set(other.membership_values)))
        memberships.sort()

        for j in range(len(memberships)):
            interval_1 = (min(self.cut(memberships[j])), max(self.cut(memberships[j])))
            interval_2 = (min(other.cut(memberships[j])), max(other.cut(memberships[j])))

            if order(interval_1, interval_2):

                flag = True
                for i in range(0, j):
                    interval_1 = (min(self.cut(memberships[i])), max(self.cut(memberships[i])))
                    interval_2 = (min(other.cut(memberships[i])), max(other.cut(memberships[i])))

                    if not order(interval_1, interval_2):
                        flag = False

                if flag:
                    return True
        return False

    def total_order_less_equal(self, other: "DiscreteFuzzyNumber",
                               order: Callable[[Tuple[int, int], Tuple[int, int]], bool]):
        """
        Computes if the first discrete fuzzy numbers is less than or equal to the second one following the criteria
        established in the Riera-Massanet total order.

        References:
            Riera JV & Massanet S & Bustince H & Fernandez J (2021).
            On Admissible Orders on the Set of Discrete Fuzzy Numbers for Application in Decision Making Problems.
            Mathematics, Volume 9, Number 1.

        Args:
            other: Another discrete fuzzy number.
            order: A callable method, representing the admissible order applied to two intervals. Returns a boolean
                   indicating if the first interval is less than the second interval.

        Returns:
            A boolean, indicating if the first discrete fuzzy number is less than or equal to the second one.
        """
        return self.total_order_equal(other) or self.total_order_less(other, order)

    # endregion

    # endregion


