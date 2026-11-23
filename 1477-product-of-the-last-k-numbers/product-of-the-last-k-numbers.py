class ProductOfNumbers:

    def __init__(self):
        # Sentinel 1 allows clean division for the entire non-zero suffix
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset prefix products because any product spanning this 0 is 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k exceeds the count of numbers added since the last 0, the product is 0
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]