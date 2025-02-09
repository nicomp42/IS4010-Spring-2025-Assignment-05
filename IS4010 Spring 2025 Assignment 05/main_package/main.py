# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu


from data_utilities_package.data_utilities import *
# ToDo: Add your import statement here 

if __name__ == "__main__":
    cars = read_car_price_dataset()
    print(len(cars), "rows read.")
    print("First:", cars[0])
    print("Last:", cars[-1])
    print("------------------------") 
    desired_model = "Camry"
    result = get_count_by_model(cars, desired_model)
    print(desired_model, "count:", result[0])
    print("------------------------")

    average_price_of_all_models = get_average_price_by_model(cars, None)
    print("Average price of all models:", average_price_of_all_models)
    print("------------------------")

    desired_models = ["Camry"]
    average_price_of_camry = get_average_price_by_model(cars, desired_models)
    print("Average price of ", desired_models, ":", average_price_of_camry)
    print("------------------------")
    
    desired_models = ["Camry", "RAV4"]
    average_price_of_camry = get_average_price_by_model(cars, desired_models)
    print("Average price of ", desired_models, ":", average_price_of_camry)
    print("------------------------")

    desired_make = "Toyota" 
    models_of_toyota = get_models_by_make(cars, desired_make)
    print("All models for", desired_make, ":", models_of_toyota)
    print("------------------------")
    
    desired_filters = ["Brand", "Model", "Price"]
    result = get_filtered_car_data(cars, desired_filters)
    # Just print the first and last row to be reasonably sure we are correct
    print("Car Data with reduced columns:", desired_filters)
    print("First:", result[0])
    print("Last:", result[-1])


    # ToDo: Contrive a test case for the most_frequent_letter function so there is a tie