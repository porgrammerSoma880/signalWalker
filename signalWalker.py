


import requests as req   #for using the api
import os       #for getting the api key, which we stored as environment variable
import logging  #for creating log file






#changing the directory to the current directory, so that logfile creates in the correct place,
#easily avoids errors/bugs right away
path=os.path.dirname(os.path.abspath(__file__))
os.chdir(path)






#creating a logfile for the program to keep logs in runtimes
#opening it in append (a) mode to store all logs continiously as follows
logging.basicConfig(level=logging.DEBUG, filename="signalWalker_logfile.log",
                    filemode="a", format="%(levelname)s log:   %(asctime)s | %(message)s",
                    datefmt="%I:%M:%S %p  %d/%m/%Y")













def track_location(username: str, phone_number: str) ->bool:
    """function to track the location of the phone number given, using api"""
   
    #Creating a debug log, of our own (other than the default logs created by the api.)
    #this log is used to take the log of the user's own identity, 
    #and the info (phone_number) they wanted to check
    logging.debug(f"User info successfully collected: username: {username} (the one who's using the program) phone_number_provided: {phone_number}")




     

    if not phone_number.startswith("+") or len(phone_number)<8 or not phone_number.replace("+","").isdigit():
        print("Please enter a valid phone number to track its primary location info! (Example: +12025550143) ")       

        #creating a error log, of our own (other than the default logs created by the api.)
        #this log is used to take a log of this situation
        logging.error(f"Program stopped due to user, '{username}' provided a invalid format phone number, ' {phone_number} '.")
        
        
        #new
        return False
    
 

    #else when everything is alright, terminate/run the program successfully as below
    else:
        
            #exception handled to provide a better performance at production-level
            try:

                #getting the environment variable from the operating system
                #where we stored the api key
                api_key=os.getenv("num_verify_API_key")



                #in case the api key does not exist inside the operating system, 
                #for whatever reason
                if not api_key:
                    print("API key not found! Please set 'num_verify_API_key' as the API key in your environment variable")
               
                
                    #Creating a info log, of our own (other than the default logs created by the api.)
                    #this log is used to create an error log when the environment variable is missing.
                    logging.error("Missing API key in environment variable.")

                    #new
                    return False
                
        
                



                else:

                    #get the api response data from the api call, which contains the info about the phone number 
                    url: str = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
                    response = req.get(url, timeout=10)
                    data_from_api: dict = response.json()
    
            


                    #in case api call fails for any reason
                    if response.status_code != 200:
                        print("API request failed! Please check the phone number or your API key.")
                        logging.error(f"API request failed with status code: {response.status_code}")
                        #new
                        return False
                    
                    else:




                        #printing the api response info in a human-readable format
                        print("Primary Information about this phone number: ")
                        print("\n")   #print a blank line for more readibility

                        for key,value in data_from_api.items():
                            print(f"{key}: {value}")
                            print(" ")    #print a blank line for more readibility




                        #Creating a info log, of our own (other than the default logs created by the api.)
                        #this log is used to make sure that the program is successfully terminated
                        logging.info(f"Program successfully terminated, phone_number_info: {data_from_api}")

                        return True


            except Exception as err:
                print(f"Error occured: {err}")

                #Creating an error log, of our own (other than the default logs created by the api.)
                #this log is used to take a log of any exception raised
                logging.error(f"Program failed due to the error: {err}  ; phone number provided by user: {phone_number}")


                return False

















#starting the program, by running the main test
if __name__=="__main__":


    #take the user's own name from the CLI, using input()
    input_username: str = input("Enter your name: ").strip().capitalize()



    #take the user's own name from the CLI, using input()
    input_phone_number: str = input("Enter a phone number, along with the country code to track it's location: ").strip()

    print("\n")    #print a blank line for better code readability



    #now run the location tracker function to track the phone number's primary location info
    track_location(input_username, input_phone_number)




