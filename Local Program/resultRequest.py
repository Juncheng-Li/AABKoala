import pandas as pd
import json
import http.client
import mimetypes

class resultRequest:

    def parseExcel(self) -> str:
        filename = "upload/uploadingData.xlsx"
        df = pd.read_excel(filename)

        unested = df.loc[0,"AuditID":"Phantom"].to_json()
        facilityOutput = df.loc[0,"fac_6":"fac_10FFF"].to_json().replace("fac","energy")
        trp = df.loc[0,"TRP_6":"TRP_10FFF"].to_json().replace("TRP","energy")
        readings = df.loc[0,"Reading_101106":"Reading_305109"].to_json()
        misdelivery = df.loc[0,"Misdelivery_101106":"Misdelivery_305109"].to_json()

        result = json.loads(unested)
        result.update({"facilityOutput":json.loads(facilityOutput)})
        result.update({"TRP":json.loads(trp)})
        result.update({"Reading":json.loads(readings)})
        result.update({"Misdelivery":json.loads(misdelivery)})

        return result

