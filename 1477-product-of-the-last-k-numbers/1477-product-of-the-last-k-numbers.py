class ProductOfNumbers:

    def __init__(self):
        # self.steam = []
        self.running_products = [0]
        # self.idx = 1
        self.zero_offset = 0

    def add(self, num: int) -> None:
        print(f"add {num=} with {self.zero_offset}")
        if num == 0:
            self.zero_offset = 0
            self.running_products.append(num)
            return
        
        self.zero_offset += 1 

        # self.idx += 1 
        if self.running_products[-1] == 0:
            self.running_products.append(num)
        else:
            self.running_products.append(num * self.running_products[-1])

        # self.steam.append(num)

    def getProduct(self, k: int) -> int:
        
        print(f"{k=} {self.zero_offset=} {(-k-1)=}, {len(self.running_products)}")

        if k == self.zero_offset:
            return self.running_products[-1]
        if k < self.zero_offset:
            return self.running_products[-1] // self.running_products[-k-1]

        return 0

        print(f"{self.running_products[-1] // self.running_products[-k-1]}")
        
        
        # return 


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
