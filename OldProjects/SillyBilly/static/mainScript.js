

function SendMessage(){
var wow = document.getElementById("Text").value;
var name = document.getElementById("Name").value;
var webHookLink = document.getElementById("WebHookBox").value;
//const defaultToken = ( webHook | tojson );

var token = "https://discord.com/api/webhooks/1300834375268700250/Tccdaw6uN5jkNxx8-SbG4RvtZyTxrcZ-tNaM9caZghox0VH5-1WPKTHIGlXsViEKQAjo"

/*if (webHookLink == "no") {
  token = defaultToken
} else {
  token = webHookLink;
} */
    
  
var request = new XMLHttpRequest();
      request.open("POST", token);

      request.setRequestHeader('Content-type', 'application/json');


      var params = {
        username: name,
        avatar_url: "https://cc-prod.scene7.com/is/image/CCProdAuthor/how_to_cut_out_images_photoshop_P1_mobile_360x270?$pjpeg$&jpegSize=200&wid=720",
        content: wow
      }

      request.send(JSON.stringify(params));
    
}

