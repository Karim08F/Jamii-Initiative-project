from flask import Flask, request, jsonify
import africastalking


app = Flask(__name__)


username = "sandbox"
api_key = ""

africastalking.initialize(username, api_key)
ussd = africastalking.USSD


@app.route('/ussd', methods=['POST'])
def ussd_menu():
    session_id = request.values.get('sessionId', None)
    service_code = request.values.get('serviceCode', None)
    phone_number = request.values.get('phoneNumber', None)
    text = request.values.get('text', None)

    
    text_array = text.split('*')
    user_response = text_array[-1]
    
 
    if text == "":
       
        response = "CON Welcome to the Community Support Service.\n"
        response += "1. Request Information\n"
        response += "2. Report an Issue\n"
        response += "3. Request a Service"
    
    elif text == "1":
       
        response = "CON What information do you need?\n"
        response += "1. Health\n"
        response += "2. Education\n"
        response += "3. Security\n"
        response += "4. Other"
    
    elif text == "1*1":
    
        response = "END You have requested information on Health. You will receive updates shortly."
      

    elif text == "2":
        
        response = "CON What issue are you reporting?\n"
        response += "1. Road Damage\n"
        response += "2. Water Supply\n"
        response += "3. Power Outage\n"
        response += "4. Other"

    elif text == "2*1":
        
        response = "END Your report on road damage has been received. We will look into it."

    elif text == "3":
       
        response = "CON What service do you need?\n"
        response += "1. Health Service\n"
        response += "2. Educational Assistance\n"
        response += "3. Other"
    
    elif text == "3*1":
        
        response = "END Your health service request has been submitted. We will contact you soon."

    else:
        
        response = "END Invalid option selected. Please try again."

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)