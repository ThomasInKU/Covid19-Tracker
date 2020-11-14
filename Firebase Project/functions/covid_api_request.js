const request = require("request-promise")

module.exports = {
    test: function(){
        return "Hello"
    },
    today_api: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/today")
        const response_json = JSON.parse(response)
        return response_json[key_index]
    },
    today_api2: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/cases/sum")
        const response_json = JSON.parse(response)
        return response_json.Province[key_index]
    },
    world_api: async function(key_index){
        const response = await request.get("https://corona.lmao.ninja/v2/all")
        const response_json = JSON.parse(response)
        const key_in = key_index.slice(6);
        return response_json[key_in]
    },
    world_command: function(key_index){
        var world_command_array = [
            "World updated",
            "World cases",
            "World todayCases",
            "World deaths",
            "World todayDeaths",
            "World recovered",
            "World todayRecovered",
            "World active",
            "World critical",
            "World casesPerOneMillion",
            "World deathsPerOneMillion",
            "World tests",
            "World testsPerOneMillion",
            "World population",
            "World oneCasePerPeople",
            "World oneDeathPerPeople",
            "World oneTestPerPeople",
            "World activePerOneMillion",
            "World recoveredPerOneMillion",
            "World criticalPerOneMillion",
            "World affectedCountries"
        ]
        return world_command_array.includes(key_index)
    },
    overview_command: function(key_index){
        var overview_array = ["Confirmed", "Recovered", "Hospitalized", 
                            "Deaths", "NewConfirmed", "NewRecovered", 
                            "NewHospitalized", "NewDeaths"]
        return overview_array.includes(key_index)
    },
    province: function(key_index){
        var province_th_array = [
            "Bangkok",
            "Chonburi",
            "Phuket",
            "Samut Prakan",
            "Nonthaburi",
            "Yala",
            "Songkhla",
            "Pattani",
            "Narathiwat",
            "Chiang Mai",
            "Pathum Thani",
            "Chachoengsao",
            "Nakhon Pathom",
            "Chumphon",
            "Krabi",
            "Nakhon Ratchasima",
            "Surat Thani",
            "Satun",
            "Prachuap Khiri Khan",
            "Ubon Ratchathani",
            "Phatthalung",
            "Samut Sakhon",
            "Buriram",
            "Nakhon Si Thammarat",
            "Udon Thani",
            "Sa Kaeo",
            "Prachinburi",
            "Kanchanaburi",
            "Surin",
            "Chiang Rai",
            "Nakhon Sawan",
            "Sisaket",
            "Trang",
            "Ratchaburi",
            "Phitsanulok",
            "Khon Kaen",
            "Suphan Buri",
            "Rayong",
            "Loei",
            "Mae Hong Son",
            "Saraburi",
            "Mukdahan",
            "Phra Nakhon Si Ayutthaya",
            "Lamphun",
            "Lampang",
            "Phetchabun",
            "Sukhothai",
            "Uttaradit",
            "Chanthaburi",
            "Roi Et",
            "Tak",
            "Nong Bua Lamphu",
            "Nong Khai",
            "Chaiyaphum",
            "Phayao",
            "Kalasin",
            "Nakhon Nayok",
            "Amnat Charoen",
            "Phang Nga",
            "Lopburi",
            "Nakhon Phanom",
            "Phetchaburi",
            "Phrae",
            "Yasothon",
            "Uthai Thani",
            "Unknown",
            "Samut Songkhram",
            "Sakon Nakhon",
            "Maha Sarakham"
        ]
        return province_th_array.includes(key_index)
    }
}
