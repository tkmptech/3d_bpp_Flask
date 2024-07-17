# Python Web Development Learning Project
IDE used: PyCharm
Python version: 3.6

Install dependencies before running: pip install -r requirement.txt

Start command: python manage.py runserver


##  Information Stored Passes as Input:
Here's a breakdown of the data with explanations of the key keywords:

1. **tradeId**: A unique identifier for the trade or transaction.

2. **orderList**: A list of orders included in the trade. Each order contains:
   - **orderCode**: A unique code identifying the order.
   - **unloadingSequence**: The sequence in which the order should be unloaded.
   - **goodList**: A list of goods included in the order. Each good contains:
     - **materialCode**: A unique code identifying the material or product.
     - **setCode**: An optional code for a set of goods (empty in this case).
     - **qty**: Quantity of the material.
     - **length, width, height**: Dimensions of the material.
     - **weight**: Weight of the material.
     - **restrictionList**: A list of restrictions for handling the material. Each restriction includes:
       - **flag**: A unique identifier for the restriction.
       - **isBear**: Indicates if the material can bear weight.
       - **bearLevel**: The level of weight the material can bear.
       - **isStack**: Indicates if the material can be stacked.
       - **stackLevel**: The level to which the material can be stacked.

3. **vehicleModelList**: A list of vehicle models available for transporting the goods. Each vehicle model contains:
   - **modelCode**: A unique code identifying the vehicle model.
   - **qty**: Quantity of vehicles of this model.
   - **cubic**: The cubic capacity of the vehicle (volume).
   - **weight**: The weight capacity of the vehicle.
   - **length, width, height**: Dimensions of the vehicle.

### Detailed Explanation of Each Section

1. **Trade ID**:
   - `tradeId`: `"312941678"` - Unique identifier for the entire trade transaction.

2. **Order List**:
   - `orderList`: Contains multiple orders with detailed information about each order.
     - `orderCode`: Unique identifier for the order (e.g., `"0"`, `"1"`).
     - `unloadingSequence`: Indicates the order in which this order should be unloaded (e.g., `0`, `1`).

3. **Goods in Each Order**:
   - `goodList`: Contains multiple goods for each order.
     - `materialCode`: Unique code for the material (e.g., `"CG0LLR009"`).
     - `setCode`: Code for the set of goods (empty in this case).
     - `qty`: Quantity of the material (e.g., `50`).
     - `length`, `width`, `height`: Dimensions of the material (e.g., `660.0`, `590.0`, `950.0`).
     - `weight`: Weight of the material (e.g., `0.45`).
     - `restrictionList`: Contains restrictions for handling the material.
       - `flag`: Identifier for the restriction (e.g., `"1"`, `"2"`).
       - `isBear`: Boolean indicating if the material can bear weight (e.g., `true`).
       - `bearLevel`: Level of weight the material can bear (e.g., `9`).
       - `isStack`: Boolean indicating if the material can be stacked (e.g., `true`).
       - `stackLevel`: Level to which the material can be stacked (e.g., `3`).

4. **Vehicle Model List**:
   - `vehicleModelList`: Contains multiple vehicle models available for transporting goods.
     - `modelCode`: Unique code for the vehicle model (e.g., `"B0002"`).
     - `qty`: Quantity of vehicles of this model (e.g., `4`).
     - `cubic`: Cubic capacity of the vehicle (e.g., `14.197008`).
     - `weight`: Weight capacity of the vehicle (e.g., `2500.0`).
     - `length`, `width`, `height`: Dimensions of the vehicle (e.g., `4340.0`, `1740.0`, `1880.0`).

##  Information Stored Passes as Output:
Here's an explanation of the data keywords in the provided JSON:

1. **tradeId**: A unique identifier for the trade or transaction.
2. **status**: Indicates the status of the transaction (0 might indicate success or completion).
3. **msg**: A message field that might contain additional information or error messages (empty in this case).
4. **carNum**: The number of cars or vehicles involved in the transaction (2 in this case).
5. **goodNum**: The total number of goods or items being transported (116 in this case).
6. **totalCapacity**: The total volume or capacity required for all the goods (40.456 cubic units).
7. **totalWeight**: The total weight of all the goods (0.044456 units).
8. **trainList**: A list containing details of each train or vehicle used in the transportation.

    - **train**: The train or vehicle identifier (1 in this case).
    - **modelCode**: The code representing the model of the vehicle (B0009 in this case).
    - **good_Num**: The number of goods or items in this particular vehicle (71 in this case).
    - **totalCapacity**: The total volume or capacity of goods in this vehicle (18.708 cubic units).
    - **totalWeight**: The total weight of goods in this vehicle (0.021348 units).
    - **packingRate**: The packing efficiency or rate, indicating how efficiently the space is used (0.283244258050841 in this case).
    - **stepList**: A list detailing the packing steps for each item in the vehicle.

        - **step**: The step number in the packing sequence (1 to 45 in this example).
        - **qty**: The quantity of goods packed in this step (usually 1 in this case).
        - **directionNum**: The orientation of the packed goods (e.g., "1*1*1" could indicate the dimensions or stacking direction).
        - **orderCode**: The order identifier related to the goods packed in this step (0 or 1 in this case).
        - **goodList**: A list of goods packed in this step.
            
            - **materialCode**: The code representing the material or goods being packed.
            - **restrictionFlag**: Indicates any restrictions on the goods (0 in this case, possibly indicating no restrictions).
            - **x**: The x-coordinate of the packed goods.
            - **y**: The y-coordinate of the packed goods.
            - **z**: The z-coordinate of the packed goods.
            - **trainIndex**: The index or identifier for the packing sequence of the goods.
