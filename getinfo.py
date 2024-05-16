from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
from PySide2.QtWidgets import *

# json_data = '''
# {
#   "type": "service_account",
#   "project_id": "readwrite-382017",
#   "private_key_id": "0360781022506ddc6c0455c63288bca1bf97dbb2",
#   "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCguPAOjF7+YRfT\\n00z2R8YYaBVVmQnqAUcghvF6hUXA/Tt0XGhGUxRMQ62IQIskuBAJNEkteDFT1Tka\\nWJm55ZFqHmSJeI6Q/bUaU47lVfeBy/jT/k61o9qQvnLyuta+dhMX51shntfbqcrn\\nK+HXO9fzkgyGXgzsP35uSGxt3DOkRfls8TCgeqkHxHzhGw+HcXB78TqakdWpPTj2\\nla4K5vPceNXbXi87Taty8HgzyF+YEotWkxGwiGouG2JydFN9NT5ID5G1LFQR1rQU\\nFlYfftTZZ0/YxQpmF0NC+R6GYL/v+68zrR+sCQalP/+DhFt1kK5prnYOLe7VrKHW\\npLzMxeiJAgMBAAECggEAAqf6ETsywqGUQlHYowiwBVQPdTOQ3eWKZwuyKRAl946N\\niW9RmFk4iaNWVmZH9UQ7ilOv1NfGHevwmNAZyiTLfd+1muTwGzwAuhXQ5gShI2cP\\nzDz29Up99lfjIEJIr7kVpoR2yiZKsMkljtEX5POGJYmx7AuiHW8M1w1IUr9Cwt5Z\\nHTQ06EWjsKOUwiFq/ubvfD0BKWRoArAoj08VDEgkZ4go4xNc5IiPjxgBt7ddNFKc\\nJP+DBDiJke8ZA2xCaZXjs0j9X7Qna7wWgLE+mI3+bzhwAQyhcbWFVUaXwM+KCkAV\\nRcIj7eVCtIOjTiM/A2RGqzvoiINsc4RquC8vegisYQKBgQDSKMzpac4pnFEkTaYp\\ndJeuvMG0jJpMoAhUjjGP/cpJWWjzWdo5s111xZqw3DnCziHu+iFkKvQK87DthaAh\\nfZ0s6dQ6hc1LxRlaw/xH85XeKHR8U62Uci4EVrYT4Xp5gpJR1WBSY8lBvpXeqDSc\\n2SjseYaQlEmcfABPGlEsifZ7oQKBgQDDx5nLhp7MOvZI4TYj7+17SX0dqqDtg3Mf\\nh/MeuqhBqWAW437cCGLbTeOJ3F06QQERFLwgyR6hFjiucuUgJt5JwgyjeswsFHMt\\nPcapWy6czE3GvzEh/VtghpobwbZ+ZLRkKckA0TryRbKZjhs9sbKy/6HEEyx3cGys\\naSQyyqyD6QKBgQCqou4d5wa5ym4np9RufHhcLG6rBi6SYK3i2cFsRIhmne4VCLOj\\nffs4kMVVLLrJbU0oGHfcOPQFoG/bq0+lYbSorwLesZ1LFDHN/KtuUF0zEG3kNJ0P\\nltW+OBmGcuFan6XmQ/X9b4ANnY1aSADQCZKszs9vvLc4E4a8s4WNQEedgQKBgHFi\\n9IuPWADoVSM4a+a8WkoA8dlwrOtiKhak4gV2DWSZ9/DJqPs+UCK7JYD+g2/tnfSK\\nkbpbQMYC3KkMGe9ZE3ycSj2ULROKdHpLQPdsu75MBO+KY6ZP2dA5pJ9WvZ7OLDum\\nh6dVhlIyU5HjX5uHgvtwWfv5LtOt5QKlkjVodCmhAoGBAMu1moG4uANvjZUVs/6Z\\nCiCwecRlP9M0TofPn4ycLMumV091rZwqvL8/sMH1noKJ6N7yu6gxPZ/HZA5qW+VR\\nk9nbb4fi27wl4JkguVbhoWD6P8OvXAybh3VzDL+Oh929xo8DuryFerh72gAgYKWF\\nMtiZp3Ejwgw0scsgJDHswkyK\\n-----END PRIVATE KEY-----\\n",
#   "client_email": "sxcmt-879@readwrite-382017.iam.gserviceaccount.com",
#   "client_id": "104746371805781563913",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sxcmt-879%40readwrite-382017.iam.gserviceaccount.com"
# }
# '''

file_path = 'Assests/json/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
with open(file_path) as f:
    credentials_info = json.load(f)
# credentials_info = json.loads('Assests/json/keys.json')
creds = service_account.Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1cVvWPTNWRRmxcPkA872LdXikqQoMm5-93lq3MiqYygw'
service = build('sheets', 'v4', credentials=creds, static_discovery=False)


def readdata(roll):
    sheet = service.spreadsheets()
    # import json

    # Open the JSON file
    # with open('Assests/json/getInfoYear.json', 'r') as file:
    #     data = json.load(file)
    #     print(data,'\n',data['YearData'][0]['BCAI'])
    if(roll[0:3]=="BCA"):
        sheettoaccess = ["BCAI","BCAII","BCAIII"]
    if(roll[0:3]=="BBA"):
        sheettoaccess = ["BBAI","BBAII","BBAIII"]
    if(roll[0:3]=="BCP"):
        sheettoaccess = ["BCPI","BCPII","BCPIII"]

    if(roll[0:3]=="BMC"):
        sheettoaccess = ["BMCI","BMCII","BMCIII"]
    if(roll[0:3]=="BBE"):
        sheettoaccess = ["BBEI","BBEII","BBEIII"]
    # if(roll[0:7]==data['YearData'][1]['BBAIII']):
    #     sheettoaccess = "BBAIII"

    # if(roll[0:7]==data['YearData'][2]['BCPI']):
    #     sheettoaccess = "BCPI"
    # if(roll[0:7]==data['YearData'][2]['BCPII']):
    #     sheettoaccess = "BCPII"
    # if(roll[0:7]==data['YearData'][2]['BCPIII']):
    #     sheettoaccess = "BCPIII"

    # if(roll[0:7]==data['YearData'][3]['BBA(IB)I']):
    #     sheettoaccess = "BBA(IB)I"
    # if(roll[0:7]==data['YearData'][3]['BBA(IB)II']):
    #     sheettoaccess = "BBA(IB)II"
    # if(roll[0:7]==data['YearData'][3]['BBA(IB)III']):
    #     sheettoaccess = "BBA(IB)III"

    # if(roll[0:7]==data['YearData'][4]['BA(JMC)I']):
    #     sheettoaccess = "BA(JMC)I"
    # if(roll[0:7]==data['YearData'][4]['BA(JMC)II']):
    #     sheettoaccess = "BA(JMC)II"
    # if(roll[0:7]==data['YearData'][4]['BA(JMC)III']):
    #     sheettoaccess = "BA(JMC)III"
    print(sheettoaccess)
    for n in range(0,3):
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheettoaccess[n]+"!A2:A200").execute()
        try:
            print(sheettoaccess[n])
            values = result.get('values')
            print(values)
            values_length = len(values)
            lst=[] 
            roll_row={}
            i=0
            roll_found_flag=0
            rowstart=2
            while(i<values_length):
                try:
                    roll_row[values[i][0]] = rowstart
                    if(values[i][0]==roll):
                        print("Matched at ",rowstart)
                        roll_found_flag=1
                        break
                except:
                    print("No Element")
                i=i+1
                rowstart=rowstart+1
            print(roll_found_flag)
            if(roll_found_flag==0):
                print("not found")
                # QMessageBox.warning(None, "Student's Data", "Data Not Found")
                return False
                


            if(roll_found_flag==1):
                print("yy")
                print(sheettoaccess[n]+"!A"+str(rowstart)+":AK"+str(rowstart))
                result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheettoaccess[n]+"!A"+str(rowstart)+":AK"+str(rowstart)).execute()
                print(result)
                values = result.get('values')
                print(values)
                values = values[0]
                print(values)
                print("yy")
                return values
            
        except:
            pass
            
        

    # readdata('BCA202201')
        # ['BCA202201', 'Ayush', 'Vishnu', 'Vishnu', '9210310383', '9009765581', 'Patna', 'ijk@gmail.com', '80%', '88%', '99%', '100%', '79%', '80%', 'Paid', 'Paid', 'Not Paid', 'Not Paid', 'Not Paid', 'Not Paid', '8.23', '6.8', '10', '1.2', '', '5.9']