const request = require("request-promise");

module.exports = {
    test: function(){
        return "Hello";
    },
    payload_in_text: function(key_index){
        var payload = [
            {
              type: "text",
              text: key_index,
            }
        ]
        return payload
    },
    flex_world: async function(key_index){
        var day = new Date().toDateString();
        var cases = await this.world_api(key_index)
        console.log(cases);
        var payload = [
            {
                type: "flex",
                altText: "World status",
                contents:{
                    "type": "bubble",
                    "header": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "image",
                          "url": "https://drive.google.com/uc?id=1KXtlSCHhqkP_dS8N-cTm7xzjWJhm6Iq_",
                          "align": "start"
                        },
                        {
                          "type": "text",
                          "text": "World",
                          "align": "center",
                          "gravity": "center",
                          "size": "25px",
                          "weight": "bold",
                          "style": "normal"
                        }
                      ]
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "World status",
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Type",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": key_index,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Cases",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": cases.toString(),
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Time",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": day,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            }
                          ],
                          "margin": "md"
                        }
                      ]
                    }
                  }
            }
        ]
        return payload
    },
    flex_province: async function(province_name){
        var day = new Date().toDateString();
        var cases = await this.today_api2(province_name);
        console.log(cases);
        var payload = [
            {
                type: "flex",
                altText: "Thailand Province status",
                contents: {
                    "type": "bubble",
                    "header": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "image",
                          "url": "https://drive.google.com/uc?id=1Ovl5O6hfv4XkXPZMtlSO64uULLakGhdM",
                          "align": "start"
                        },
                        {
                          "type": "text",
                          "text": "Thailand",
                          "align": "center",
                          "gravity": "center",
                          "size": "25px",
                          "weight": "bold",
                          "style": "normal"
                        }
                      ]
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": province_name,
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Province",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": province_name,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Cases",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": cases.toString(),
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Time",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": day,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            }
                          ],
                          "margin": "md"
                        }
                      ]
                    }
                  }
            }
        ]
        return payload
    },
    flex_thailand: async function(type){
        var day = new Date().toDateString();
        var cases = await this.today_api(type);
        console.log(cases);
        var payload = [
            {
                type: "flex",
                altText: "Thailand status",
                contents: {
                    "type": "bubble",
                    "header": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "image",
                          "url": "https://drive.google.com/uc?id=1_2XpnbCb72wKbZCLkkNW8iXWFvSRnaAg",
                          "align": "start"
                        },
                        {
                          "type": "text",
                          "text": "Thailand",
                          "align": "center",
                          "gravity": "center",
                          "size": "25px",
                          "weight": "bold",
                          "style": "normal"
                        }
                      ]
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": type,
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Type",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": type,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Cases",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": cases.toString(),
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Time",
                                  "flex": 2,
                                  "size": "sm",
                                  "color": "#aaaaaa",
                                  "wrap": true
                                },
                                {
                                  "type": "text",
                                  "text": day,
                                  "flex": 5,
                                  "color": "#666666",
                                  "size": "sm",
                                  "wrap": true
                                }
                              ]
                            }
                          ],
                          "margin": "md"
                        }
                      ]
                    }
                  }
            }
        ]
        return payload
    },
    today_api: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/today")
        const response_json = JSON.parse(response);
        return response_json[key_index];
    },
    today_api2: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/cases/sum")
        const response_json = JSON.parse(response);
        return response_json.Province[key_index];
    },
    world_api: async function(key_index){
        const response = await request.get("https://corona.lmao.ninja/v2/all")
        const response_json = JSON.parse(response)
        const key_in = key_index.slice(6);
        return response_json[key_in];
    },
    payload_help: function(){
        var payload = [
            {
                type: "text",
                text: "Google Doc: https://docs.google.com/document/d/1yZ44ohLjBxY3xdxLnVfxUchmPmGIvRqF8OUgX0xgOpg/edit?usp=sharing",
            },
            {
                "type": "image",
                "originalContentUrl": "https://drive.google.com/uc?id=1H-Mhqx2q1N53uT1xGV1VubOmbZQfRIxc",
                "previewImageUrl": "https://drive.google.com/uc?id=1H-Mhqx2q1N53uT1xGV1VubOmbZQfRIxc",
            },
            {
                "type": "image",
                "originalContentUrl": "https://drive.google.com/uc?id=19KwDgIIkL-2A57258hP3XwLKIbsKTgNq",
                "previewImageUrl": "https://drive.google.com/uc?id=19KwDgIIkL-2A57258hP3XwLKIbsKTgNq",
            },
        ]
        return payload
    },
    payload_collaborator: function(key_index){
        var payload = [
            {
                type: "text",
                text: key_index,
            },
            {
                "type": "image",
                "originalContentUrl": "https://avatars3.githubusercontent.com/u/58279552?s=400&u=3c903ea892ac60dc6cf0cc38ad1e42e7729da2df&v=4",
                "previewImageUrl": "https://avatars3.githubusercontent.com/u/58279552?s=400&u=3c903ea892ac60dc6cf0cc38ad1e42e7729da2df&v=4",
            },
            {
                "type": "image",
                "originalContentUrl": "https://avatars3.githubusercontent.com/u/53256241?s=400&u=f7f0ac9fe9ec2e8bc4ed9de44c27fafc0f2492fc&v=4",
                "previewImageUrl": "https://avatars3.githubusercontent.com/u/53256241?s=400&u=f7f0ac9fe9ec2e8bc4ed9de44c27fafc0f2492fc&v=4",
            },
            {
                "type": "image",
                "originalContentUrl": "https://avatars0.githubusercontent.com/u/59830751?s=400&u=85306431e5f8267eebb283d20205e2650bc99c68&v=4",
                "previewImageUrl": "https://avatars0.githubusercontent.com/u/59830751?s=400&u=85306431e5f8267eebb283d20205e2650bc99c68&v=4",
            },
            {
                "type": "image",
                "originalContentUrl": "https://avatars2.githubusercontent.com/u/58396402?s=400&u=cd900acf499696a5bbe67b66b1d31c8e9f975754&v=4",
                "previewImageUrl": "https://avatars2.githubusercontent.com/u/58396402?s=400&u=cd900acf499696a5bbe67b66b1d31c8e9f975754&v=4",
            }
        ]
        return payload
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
        var overview_array = ["Confirmed", "Recovered", "Hospitalized", "Deaths", "NewConfirmed", "NewRecovered", "NewHospitalized", "NewDeaths"]
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
            "Chumphon","Krabi",
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
        return province_th_array.includes(key_index);
    }

}