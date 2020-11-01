const functions = require("firebase-functions")
const request = require("request-promise")
const requester = require("./covid_api_request")

exports.webhook = functions.https.onRequest(async(req, res) => {
    const lah = require("lineapihelper")
    lah.setrequest(req);
    lah.cat("mxTbtvHPryhqG+u/VERR9uHe29UQbPdqonkX8QTfZjBAQii7ul7g5Ks/OBuyWSnOgsbE1JviwYrHv4816RLNbr3XyIBOeUh5GJPdswBMlu5ewAYNtK3Fz5sXhD0vJvLV9dZ688FL+sj+LZeJR2KCLQdB04t89/1O/w1cDnyilFU=");
    var input_text = lah.message().text;
    var out_text = ""
    var payload
    
    if(requester.overview_command(input_text)){
        out_text = input_text + " cases in Thailand: " + await requester.today_api(input_text) + " Persons.";
        payload = requester.payload_in_text(out_text)
    }else if(requester.province(input_text)){
        out_text = input_text + ", Thailand total cases: " + await requester.today_api2(input_text) + " Persons.";
        payload = requester.payload_in_text(out_text)
    }
    else if(requester.world_command(input_text)){
        out_text = input_text + ": " + await requester.world_api(input_text) + " cases.";
        payload = requester.payload_in_text(out_text)
    }
    else if(input_text === "BOOM"){
        out_text = "God Boom, Welcome Sir!! Have a nice day.";
        payload = requester.payload_in_text(out_text)
    }
    else if(input_text === "Contact"){
        out_text = "contact FB: Puvana Swatvanith";
        payload = requester.payload_in_text(out_text)
    }
    else if(input_text === "Collaborator"){
        out_text = "Collaborator:" + "\n" + "lisbono2001" + "\n" + "Noboomta" + "\n" + "Bhatara007" + "\n" + "toey10112";
        payload = requester.payload_collaborator(out_text);
    }
    else if(input_text === "help"){
        out_text = "help mode" + "\n"
        out_text += "3 ways of command" + "\n"
        out_text += "   1) Province with Capitalize (ex. Bangkok, Chiang Mai)" + "\n"
        out_text += "   2) Overview command (Confirmed, Recovered, Hospitalized, Deaths, NewConfirmed, NewRecovered, NewHospitalized, NewDeaths)" + "\n"
        out_text += "   3) World command (World +(cases, todayCases, deaths, todayDeaths, recovered, todayRecovered, active, critical, casesPerOneMillion, deathsPerOneMillion, tests, testsPerOneMillion, population, oneCasePerPeople, oneDeathPerPeople, oneTestPerPeople, activePerOneMillion, recoveredPerOneMillion, criticalPerOneMillion, affectedCountries))" + "\n"
        payload = requester.payload_in_text(out_text)
    }
    else{
        out_text = "No command try 'help' for more guide." ;
        payload = requester.payload_in_text(out_text)
    }


    // var payload = [
    //     {
    //       type: "text",
    //       text: out_text,
    //     }
    // ]

    return lah.reply(lah.replyToken(), payload)

    .then((response) => {
        console.log(response)
        return res.status(200).send();
    }).catch((e) => {
        console.log(e)
        return res.status(500).send();
    })

    
})