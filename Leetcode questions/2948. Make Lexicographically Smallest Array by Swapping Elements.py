from typing import List


class Solution:
    def lexicographicallySmallestArray(
            self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # Store every number along with its original index.
        #
        # Example:
        # nums = [60, 34, 56]
        #
        # pairs =
        # [(60, 0), (34, 1), (56, 2)]
        pairs = [(nums[i], i) for i in range(n)]

        # Sort according to VALUES.
        #
        # [(60, 0), (34, 1), (56, 2)]
        #
        # becomes:
        #
        # [(34, 1), (56, 2), (60, 0)]
        pairs.sort()

        # This will store our final answer.
        result = nums[:]

        # Start of the current swappable group.
        start = 0

        while start < n:

            # end will search for where the current
            # swappable group finishes.
            end = start + 1

            # Keep adding values to the same group
            # while consecutive sorted values differ
            # by at most 'limit'.
            #
            # Example:
            #
            # 56 -> 60 -> 62
            #
            # 60 - 56 <= limit
            # 62 - 60 <= limit
            #
            # Therefore all three belong to one group.
            while (
                    end < n
                    and pairs[end][0] - pairs[end - 1][0] <= limit
            ):
                end += 1

            # ------------------------------------------------
            # We have now found ONE complete swappable group.
            #
            # Group is:
            # pairs[start:end]
            # ------------------------------------------------

            # Extract the original indices belonging
            # to this group.
            indices = []

            for i in range(start, end):
                indices.append(pairs[i][1])

            # Sort the original indices.
            #
            # Example:
            #
            # values  = [56, 60, 62]
            # indices = [5, 1, 4]
            #
            # becomes:
            #
            # indices = [1, 4, 5]
            indices.sort()

            # The VALUES are already sorted because
            # the entire 'pairs' list was sorted earlier.
            #
            # So:
            #
            # smallest value -> smallest index
            # next value     -> next index
            # ...
            #
            # This produces the lexicographically
            # smallest arrangement for this group.
            for i in range(len(indices)):

                original_index = indices[i]

                value = pairs[start + i][0]

                result[original_index] = value

            # Move to the beginning of the next group.
            start = end

        return result