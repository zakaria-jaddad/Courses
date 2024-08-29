def is_valid(title,
            bid, 
            description, 
                ):
    for data in [title, bid, description]:
        if data == "":
            return False
    
    return True