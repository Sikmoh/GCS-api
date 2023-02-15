async function login(){
    let login_details = {
        let x = document.forms['login']['username'].value;
        let y = document.forms['login']['password'].value;
        if(x == ""){
        alert("username must be filled")
        return false;
        }

    }
    let options = {
        method: 'POST',
        headers: {
            'Content-Type':
                'application/json;charset=utf-8'
        },
        body: JSON.stringify(login_details)
    }
    const response = await fetch("http://192.168.247.223:5000/login", options);
    var res = await response.json()
    console.log(res)
}




//async function api(){
//
//
//    let url = "http://192.168.247.223:5003/telemetry";
//    const response = await fetch(url);
//    //var telemetry = await response.json();
//
//    //console.log(telemetry)
//    let d = new Date();
//      document.getElementById("clock").innerHTML=
//      d.getHours() + ":" +
//      d.getMinutes() + ":" +
//      d.getSeconds();
////    window.location = window.location.href;
//
//}


    //console.log('removed')




//setInterval(api, 2000)