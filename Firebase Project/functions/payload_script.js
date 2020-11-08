const request = require("request-promise");
const requester = require("./covid_api_request")

module.exports = {
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
        var cases = await requester.world_api(key_index)
        // console.log(cases);
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
        var cases = await requester.today_api2(province_name);
        // console.log(cases);
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
                          "align": "start",
                          "size": "full",
                          "aspectMode": "cover",
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
        var cases = await requester.today_api(type);
        // console.log(cases);
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
                          "align": "start",
                          "size": "full",
                          "aspectMode": "cover",
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
                "originalContentUrl": "https://drive.google.com/uc?id=1rlezKXRP-UovUIYPtkSvlFr0o3w30piy",
                "previewImageUrl": "https://drive.google.com/uc?id=1rlezKXRP-UovUIYPtkSvlFr0o3w30piy",
            },
        ]
        return payload
    },
    payload_collaborator: function(){
        var payload = [
          {
              type: "flex",
              altText: "Thailand status",
              contents: {
                "type": "carousel",
                "contents": [
                  {
                    "type": "bubble",
                    "direction": "ltr",
                    "hero": {
                      "type": "image",
                      "url": "https://drive.google.com/uc?id=12YPWCY36g_zeZaL9Vn8i9vrq3JbvSzNa",
                      "size": "full",
                      "aspectMode": "cover"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "CovidTracker Collaborator",
                          "position": "relative",
                          "align": "center",
                          "gravity": "center",
                          "weight": "bold",
                          "size": "lg"
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "uri",
                            "label": "WEBSITE",
                            "uri": "https://github.com/lisbono2001/Covid19-Tracker"
                          },
                          "height": "sm",
                          "style": "link"
                        }
                      ]
                    }
                  },
                  {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://avatars3.githubusercontent.com/u/58279552?s=400&u=3c903ea892ac60dc6cf0cc38ad1e42e7729da2df&v=4",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "5:4"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Lisbono2001",
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "Theetouch Kasemarnontana",
                              "color": "#666666",
                              "size": "sm",
                              "flex": 5,
                              "wrap": true
                            },
                            {
                              "type": "text",
                              "text": "Ske17 Ku79",
                              "flex": 5,
                              "size": "sm",
                              "color": "#666666",
                              "wrap": true
                            }
                          ]
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "uri",
                            "label": "Github",
                            "uri": "https://github.com/lisbono2001"
                          },
                          "height": "sm",
                          "style": "link"
                        }
                      ]
                    }
                  },
                  {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://avatars3.githubusercontent.com/u/53256241?s=400&u=f7f0ac9fe9ec2e8bc4ed9de44c27fafc0f2492fc&v=4",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "5:4"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Noboomta",
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "Puvana Swatvanith",
                              "color": "#666666",
                              "size": "sm",
                              "flex": 5,
                              "wrap": true
                            },
                            {
                              "type": "text",
                              "text": "Ske17 Ku79",
                              "flex": 5,
                              "size": "sm",
                              "color": "#666666",
                              "wrap": true
                            }
                          ]
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "uri",
                            "label": "Github",
                            "uri": "https://github.com/Noboomta"
                          },
                          "height": "sm",
                          "style": "link"
                        }
                      ]
                    }
                  },
                  {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://avatars0.githubusercontent.com/u/59830751?s=400&u=85306431e5f8267eebb283d20205e2650bc99c68&v=4",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "5:4"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Bhatara007",
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "Bhatara Chaemchan",
                              "color": "#666666",
                              "size": "sm",
                              "flex": 5,
                              "wrap": true
                            },
                            {
                              "type": "text",
                              "text": "Ske17 Ku79",
                              "flex": 5,
                              "size": "sm",
                              "color": "#666666",
                              "wrap": true
                            }
                          ]
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "uri",
                            "label": "Github",
                            "uri": "https://github.com/bhatara007"
                          },
                          "height": "sm",
                          "style": "link"
                        }
                      ]
                    }
                  },
                  {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://avatars2.githubusercontent.com/u/58396402?s=400&u=cd900acf499696a5bbe67b66b1d31c8e9f975754&v=4",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "5:4"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Toey10112",
                          "size": "xl",
                          "weight": "bold"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "Suchon Prasert",
                              "color": "#666666",
                              "size": "sm",
                              "flex": 5,
                              "wrap": true
                            },
                            {
                              "type": "text",
                              "text": "Ske17 Ku79",
                              "flex": 5,
                              "size": "sm",
                              "color": "#666666",
                              "wrap": true
                            }
                          ]
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "uri",
                            "label": "Github",
                            "uri": "https://github.com/toey10112"
                          },
                          "height": "sm",
                          "style": "link"
                        }
                      ]
                    }
                  }
                ]
              }
          }
        ]
        return payload
    },
}
