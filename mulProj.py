from XLParser import xl
from CI_lib_v1 import revision
import time

obj1 = xl()
count, lis = obj1.xl_Parse()

print("Count: ",count)
print(lis)
global val
val = 0
#while val != count:
while True:
    for l in range(0, count):
        #print ("Inside")
        #print(lis[l])
        val = val+1
        appName = lis[l][0]
        env = lis[l][1]
        user = lis[l][2]
        apiKey = lis[l][3]
        ut_pwd = lis[l][4]
        jk_tkn = lis[l][5]
        print("------------------------------------------------")
        print("Application Name : ", appName)
        print("Environment : ", env)
        print("User : ", user)
        print("Mendix API Key : ", apiKey)
        print("Unit Test Password : ", ut_pwd)
        print("Jenkins Token : ", jk_tkn)
        print("********************Placeholder for Multiple projects******************************")
        obj = revision(appName, user, apiKey, env, ut_pwd, jk_tkn)
        build_required, latest_rev = obj.revision_api()
        if build_required:
            print("Proceeding with next steps...")
            #Creating a new build
            packageID = obj.api_call(latest_rev)
            print("************----------***********",packageID)
            #trigger Environment stop API
            stopEnv_Res = obj.stop_EnvApi()
            if stopEnv_Res == 200:
                print("Build Sucessfull :",packageID)
                print ("Validating status of environments...")
                env_stat = obj.env_StatusApi()
                if env_stat == "Stopped":
                    print("Environment Stopped!!!")
                    #Validating Response for Transport Build
                    res_tb = obj.transport_build(packageID)
                    """Need to wait for some time- approx 1 mins 10 secs for Package ID to get build"""
                    while res_tb !=200:
                        print("Waiting for Package Build...")
                        time.sleep(30)
                        res_tb = obj.transport_build(packageID)
                    if res_tb == 200:
                        print("Transport Build Sucessful, proceeding to next steps...")
                        print("Starting Environment...")
                        envFlag = obj.start_EnvApi()
                        if envFlag:
                            """Placeholder for Triggering Unit Tests"""
                            print("Unit Testing Module")
                            res_UTTrigger = obj.trigger_UT()
                            print("Response for Triggering Unit Tests: ",res_UTTrigger)
                            if res_UTTrigger == 204:
                                time.sleep(5)
                                print ("Fetching Unit Test Results...")
                                res_UTRes, res_UT = obj.ut_Results()
                                print("Unit Test Results: \n",res_UT)
                                print("Proceeding to Trigger Jenkins Functional Suite...")
                                obj.triggerFT()
                                print("Functional Execution Completed.....!!!!")
                    else:
                        print("Check details for Error code: ",str(res_tb))
            else:
                print("Unable to Stop the Environment, trying again...")
        else:
            time.sleep(5)
    
