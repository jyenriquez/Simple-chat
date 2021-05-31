//Kinda hacky way to scroll down
setTimeout(printSomething, 250);

function printSomething(){
    window.scrollTo(0,document.body.scrollHeight);
    setTimeout(printSomething, 10000);
}