def inches_to_feet(inches: int | float) -> float:
    """
    Calculate how many feet are in the given inches

    Args:
        inches (int | float): Number of inches to convert

    Returns:
        (float) The equivalent number of feet
    """
    INCHES_PER_FOOT = 12
    inches_to_feet = inches / INCHES_PER_FOOT
    return inches_to_feet




def height_of_ball(height: float | int, velocity: float | int, t: float | int) -> float:
    """
        Computer height reached by ball
    
        Args: 
            height (int | float): Initial height of ball in inches
            velovity (int | float): Initial velocity of ball in feet/s
            t (int|float): time elapsed in seconds

        Returns:
            (float | int) The height (int feet) of the ball after t seconds
    """
    height_to_feet = inches_to_feet(height)
    height_reached = height_to_feet + (velocity * t) - (16 * t ** 2)
    return height_reached




def get_maximum_height(height: int | float, velocity: int | float) -> float:
    """ 
        Finding maximum height of a ball

        Args: 
            height (int | float): Initial height of the ball in inches
            velovity (int | float): Initial velocity of ball in feet/s
            t (int|float): time elapsed in seconds
        
        Returns:
            (float): the maximum height of the ball in inches
    """
    height_reached = height_of_ball(height, velocity, velocity/32)
    return height_reached



def get_root_sum(a: int | float, b: int | float, c: int | float) -> float:

    discriminant = (b ** 2 - 4 * a * c) ** 0.5
    positive_root = (-b + discriminant) / (2 * a)
    negative_root = (-b - discriminant) / (2 * a)
    print("Roots are: positive =", positive_root, "and negative =", negative_root)
    total_sum = positive_root + negative_root
    return total_sum
def nearest_whole(num):
    num += 0.5
    num = num // 1
    return num

def lbs_to_groups(lbs, fruit_per_lbs, fruit_per_group):
    total_fruit = fruit_per_lbs * lbs
    total_groups = total_fruit / fruit_per_group
    return nearest_whole(total_groups) 
LBS_PER_TON = 2000
APPLES_PER_LBS = 3
APPLES_PER_BUSHEL = 10
BANANAS_PER_LBS = 5.5
BANANAS_PER_BUNCH = 6
CANTALOPES_PER_LBS = 8
CANTALOPES_PER_BATCH = 14
def calculate_ingridients(tons):
    lbs = tons * LBS_PER_TON
    apples = lbs_to_groups(lbs, APPLES_PER_LBS, APPLES_PER_BUSHEL)
    bananas = lbs_to_groups(lbs, BANANAS_PER_LBS, BANANAS_PER_BUNCH)
    cantelopes = lbs_to_groups(lbs, CANTALOPES_PER_LBS, CANTALOPES_PER_BATCH)
    print("bushels:", apples)
    print("bunches:", bananas)
    print("batches:", cantelopes)


def main() -> None:
    # print("Testing inches_to_feet")
    # print(inches_to_feet(12)) # 1 foot

    # output = inches_to_feet(24) 
    # print(output) # 2 feet

    # output = inches_to_feet(37.5) 
    # print(output) # 3.125 feet
    # print("Testing height_of_ball")
    # output = height_of_ball(1200, 10, 2) 
    # print(output) # 56
    # output = get_maximum_height(60, 34)
    # print(output) # 23.0625
    # output = get_root_sum(1, -7, 10)
    # print(output)
    output = lbs_to_groups(10, 2, 1)
    print(output)
    calculate_ingridients(1)

if __name__ == "__main__":
    main()
