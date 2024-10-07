restaurants_listDict = [
                          {"ID" : "1", "Name" : "Viking Luxury Buffet", "Location" : "Pasay City", "Cuisine Type" : "Buffet", "Established Year" : "2011", "Website or Contact" : "www.vikings.ph"},
                          {"ID" : "2", "Name" : "Antonio's Restaurant", "Location" : "Tagaytay", "Cuisine Type" : "Fine Dining", "Established Year" : "2002", "Website or Contact" : "www.antoniosrestaurant.ph"},
                          {"ID" : "3", "Name" : "Mesa Filipino Moderne", "Location" : "Makati City", "Cuisine Type" : "Filipino", "Established Year" : "2009", "Website or Contact" : "www.mesa.ph"},
                          {"ID" : "4", "Name" : "Manam Comfort Filipino", "Location" : "Quezon City", "Cuisine Type" : "Filipino", "Established Year" : "2013", "Website or Contact" : "www.manam.ph"},
                          {"ID" : "5", "Name" : "Ramen Nagi", "Location" : "Various locations", "Cuisine Type" : "Japanese", "Established Year" : "2013", "Website or Contact" : "www.ramennagi.com.ph"}
                      ]

for restaurant in restaurants_listDict:
    print(f"ID: {restaurant['ID']}, Name: {restaurant['Name']}, Location: {restaurant['Location']}, Established Year: {restaurant['Established Year']}, Website or Contact: {restaurant['Website or Contact']}")