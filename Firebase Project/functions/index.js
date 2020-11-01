const functions = require("firebase-functions")
const request = require("request-promise")
const requester = require("./covid_api_request")

exports.webhook = functions.https.onRequest(async(req, res) => {
    const lah = require("lineapihelper")
    lah.setrequest(req);
    lah.cat("mxTbtvHPryhqG+u/VERR9uHe29UQbPdqonkX8QTfZjBAQii7ul7g5Ks/OBuyWSnOgsbE1JviwYrHv4816RLNbr3XyIBOeUh5GJPdswBMlu5ewAYNtK3Fz5sXhD0vJvLV9dZ688FL+sj+LZeJR2KCLQdB04t89/1O/w1cDnyilFU=");
    var out_text = ""
    
    if(requester.overview_command(lah.message().text)){
        out_text = lah.message().text + " today cases: " + await requester.today_api(lah.message().text) + " Persons.";
    }else if(requester.province(lah.message().text)){
        out_text = lah.message().text + " total cases: " + await requester.today_api2(lah.message().text) + " Persons.";
    }
    else if(lah.message().text === "help"){
        out_text = "help mode" + "\n"
        out_text += "2 ways of command" + "\n"
        out_text += "   1) Province with Capitalize (ex. Bangkok, Chiang Mai)" + "\n"
        out_text += "   2) Overview command (Confirmed, Recovered, Hospitalized, Deaths, NewConfirmed, NewRecovered, NewHospitalized, NewDeaths)" + "\n"
    }
    else{
        out_text = "No command try 'help' for more guide." ;
    }


    var payload = [
        {
          type: "text",
          text: out_text,
        }
      ]

    return lah.reply(lah.replyToken(), payload)

    .then((response) => {
        console.log(response)
        return res.status(200).send();
    }).catch((e) => {
        console.log(e)
        return res.status(500).send();
    })

    
})