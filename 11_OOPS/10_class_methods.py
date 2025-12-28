class ChaiOrder:
    def __init__(self, tea_type,sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_details):
        return cls(order_details["tea_type"], order_details["sweetness"], order_details["size"])
    
    @classmethod
    def from_string(cls, order_details):
        tea_type, sweetness, size = order_details.split("-")
        return cls(tea_type, sweetness, size) 
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]

chai1 = ChaiOrder("masala", "1", "Small")
print(f"chai1 type: {chai1.tea_type}, chai1 sweetness: {chai1.sweetness}, chai1 size: {chai1.size}")

chai_dict = {"tea_type": "ginger", "sweetness":2, "size": "Large"}
chai2 = ChaiOrder.from_dict(chai_dict)
print(f"chai2 type: {chai2.tea_type}, chai2 sweetness: {chai2.sweetness}, chai2 size: {chai2.size}")

chai_string = "cardemom-3-Medium"
chai3 = ChaiOrder.from_string(chai_string)
print(f"chai3 type: {chai3.tea_type}, chai3 sweetness: {chai3.sweetness}, chai3 size: {chai3.size}")

print(ChaiUtils.is_valid_size("extra-large"))
print(ChaiUtils.is_valid_size("Large"))

print(chai1.__dict__)
print(chai2.__dict__)
print(chai3.__dict__)