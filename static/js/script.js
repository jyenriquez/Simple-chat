
let inputVal = document.getElementById("chatMessage");
if(inputVal){
    inputVal.addEventListener("keydown", function (e) {
        if(e.code === "Enter") {
            saveData(e);
        }
    })
}

//TODO: figure out local storage bug, only displays numbers
//TODO: figure out how to update page asynchronously
let list = allStorage();
for(let test in list) {
    document.getElementById('message-board').innerHTML += '<li>' + test + '</li>';
    console.log(test);
}


//Tests the message
function validate(e){
    let text = e.target.value;
    alert(text);
}

//Temp localStorage implementation
function saveData(message) {
    let text = message.target.value;

    //Puts message and time onto localStorage
    localStorage.setItem(text, Date.now);
}

function allStorage() {

    var values = [],
        keys = Object.keys(localStorage),
        i = keys.length;

    while ( i-- ) {
        values.push( localStorage.getItem(keys[i]) );
    }

    return values;
}
