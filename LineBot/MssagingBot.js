function doPost(e) {
  
    Logger.log("Hello from BetterLog :)");
  
    var requestJSON = e.postData.contents;
    Logger.log(requestJSON);
    
    var requestObj = JSON.parse(requestJSON).events[0];
    var userMessage = requestObj.message.text;
    Logger.log(userMessage);
    
    var token = requestObj.replyToken;
    var replyText = "unsuccess";
    
    // Copy userMessage to Message Array
    var message_Array = userMessage.split(",");
    
    if(userMessage === "admin"){
    //   Logger.log
    }
    
    else if(userMessage === "help"){
      replyText = "contact me at FB: Puvana Swatvanith";
    }
    
  //  ss.appendRow(["Test1", "Test2"]);
    if (requestObj.message.type === "text") {
    
      replyMessage(token, replyText);
      
    }
}

function replyMessage(token, replyText) {
    var url = "https://api.line.me/v2/bot/message/reply";
    var lineHeader = {
      "Content-Type": "application/json",
      "Authorization": "Bearer xv5fNQob97Bf2zKSyXL5eWEGOWPsUMVHEkxm4axrlU1L4WMVl9d9rRaLtkuZCzHvTu353GGzdspNX6YEheEpH/7u58/Mh38qMnfLBFkKLdmuRNYttrfUQoU8XxuQpfsxpUvSFc9AuVRZQ/lVJmW7rQdB04t89/1O/w1cDnyilFU="
    };
  
    var postData = {
      "replyToken" : token,
      "messages" : [{
        "type" : "text",
        "text" : replyText
      }]
    };
  
    var options = {
      "method" : "POST",
      "headers" : lineHeader,
      "payload" : JSON.stringify(postData)
    };
  
    try {
      var response = UrlFetchApp.fetch(url, options);
    }
    
    catch (error) {
      Logger.log(error.name + "：" + error.message);
      return;
    }
      
    if (response.getResponseCode() === 200) {
      Logger.log("Sending message completed.");
    }
  }