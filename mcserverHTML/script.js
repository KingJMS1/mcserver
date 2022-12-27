/*https://c1adb8msah.execute-api.us-east-2.amazonaws.com
/McServerStart
/McServerStatus
/McServerStop
*/

// initialization



function Status()
{
	var xhrStatus = new XMLHttpRequest();
	// gets the status of the server
	xhrStatus.open("GET", "https://c1adb8msah.execute-api.us-east-2.amazonaws.com/Two/McServerStatus", true);
	document.getElementById("resetButton").onclick = HardReset;
	xhrStatus.onload = function (e){
	if (xhrStatus.readyState === 4) {
		// 
		if (xhrStatus.status === 200) {
			document.getElementById("statusDescription").innerHTML = xhrStatus.responseText;
			
			if (xhrStatus.responseText === "The server is closed"){
				document.getElementById("powerButton").innerHTML = "Turn On";
				document.getElementById("powerButton").onclick = TurnOn;
			}
			else{
				document.getElementById("powerButton").innerHTML = "Turn Off";
				document.getElementById("powerButton").onclick = TurnOff;
			}
				
			console.log(xhrStatus.responseText);
		} else {
			console.error(xhr.statusText);
		}
	}
	};
	xhrStatus.send(null);
}

function TurnOn()
{
	var xhrOn = new XMLHttpRequest(); 
	xhrOn.open("GET", "https://c1adb8msah.execute-api.us-east-2.amazonaws.com/Two/McServerStart", true);
	document.getElementById("statusDescription").innerHTML = "The server is turning on. Please wait at least 5 minutes before annoying Mahlon";
	xhrOn.send(null);
	document.getElementById("powerButton").disabled = true;
	document.getElementById("powerButton").style.opacity = 0;
	document.getElementById("powerButton").onclick = null;
}
function TurnOff()
{
	var xhrOff = new XMLHttpRequest();
	xhrOff.open("GET", "https://c1adb8msah.execute-api.us-east-2.amazonaws.com/Two/McServerStop", true);
	document.getElementById("statusDescription").innerHTML = "Server is turning off";
	xhrOff.send(null);
	document.getElementById("powerButton").disabled = true;
	document.getElementById("powerButton").style.opacity = 0;
	document.getElementById("powerButton").onclick = null;
}

function HardReset()
{
	var xhrHardReset = new XMLHttpRequest();
	xhrHardReset.open("GET", "https://c1adb8msah.execute-api.us-east-2.amazonaws.com/Two/HardShutdown", true);
	document.getElementById("statusDescription").innerHTML = "Hard reset is being performed.";
	xhrHardReset.send(null);
	document.getElementById("resetButton").disabled = true;
	document.getElementById("resetButton").style.opacity = 0;
	document.getElementById("resetButton").onclick = null;
}