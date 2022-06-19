class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        return [[product for product in products if product.startswith(searchWord[:i + 1])][:3] for i in range(len(searchWord))]